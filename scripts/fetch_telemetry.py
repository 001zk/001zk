#!/usr/bin/env python3
"""
001ZK // LIVING SYSTEM
fetch_telemetry.py

Busca dados públicos reais do usuário na GitHub API e grava
data/telemetry.json. Nunca inventa valores: se um campo não puder
ser obtido, ele simplesmente não é escrito e o gerador de SVG
exibirá "N/A" para ele.

Uso:
    GITHUB_HANDLE=001zk python3 scripts/fetch_telemetry.py

Sem token, a API pública do GitHub funciona com um limite de taxa
menor. Em GitHub Actions, GITHUB_TOKEN é injetado automaticamente
e usado se presente (apenas para aumentar o limite de requisições —
nenhum dado privado é acessado).
"""

import json
import os
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

HANDLE = os.environ.get("GITHUB_HANDLE", "001zk")
TOKEN = os.environ.get("GITHUB_TOKEN")

API_BASE = "https://api.github.com"


def api_get(path):
    req = urllib.request.Request(f"{API_BASE}{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "001zk-living-system")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"[fetch_telemetry] aviso: falha ao buscar {path}: {e}", file=sys.stderr)
        return None


def main():
    telemetry = {}

    user = api_get(f"/users/{HANDLE}")
    if user:
        telemetry["public_repos"] = user.get("public_repos")
        telemetry["followers"] = user.get("followers")
        telemetry["following"] = user.get("following")

    repos = api_get(f"/users/{HANDLE}/repos?per_page=100&type=owner")
    if isinstance(repos, list):
        languages = {r.get("language") for r in repos if r.get("language")}
        telemetry["language_count"] = len(languages)
        telemetry["stars_total"] = sum(r.get("stargazers_count", 0) for r in repos)
        telemetry["forks_total"] = sum(r.get("forks_count", 0) for r in repos)

        recent = [r for r in repos if r.get("pushed_at")]
        telemetry["activity_state"] = "ACTIVE" if recent else "N/A"

    # Remove chaves com valor None para nunca gravar dado falso/vazio.
    telemetry = {k: v for k, v in telemetry.items() if v is not None}

    os.makedirs(DATA_DIR, exist_ok=True)
    out_path = os.path.join(DATA_DIR, "telemetry.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(telemetry, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"[fetch_telemetry] {out_path} atualizado com {len(telemetry)} campo(s).")


if __name__ == "__main__":
    main()
