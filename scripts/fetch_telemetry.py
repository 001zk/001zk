#!/usr/bin/env python3
"""
001ZK // LIVING SYSTEM
fetch_telemetry.py

Busca dados públicos reais do usuário na GitHub API e grava
data/telemetry.json. Nunca inventa valores: se um campo não puder
ser obtido, ele simplesmente não é escrito e os geradores exibirão
"N/A" para ele.

Uso:
    GITHUB_HANDLE=001zk python3 scripts/fetch_telemetry.py

Sem token, a API pública do GitHub funciona com um limite de taxa
menor. Em GitHub Actions, GITHUB_TOKEN é injetado automaticamente
e usado se presente (apenas para aumentar o limite de requisições e
habilitar a consulta GraphQL de contribuições — nenhum dado privado
é acessado).
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

HANDLE = os.environ.get("GITHUB_HANDLE", "001zk")
TOKEN = os.environ.get("GITHUB_TOKEN")

API_BASE = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"


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


def graphql(query, variables):
    if not TOKEN:
        print("[fetch_telemetry] aviso: sem GITHUB_TOKEN, pulando consulta GraphQL", file=sys.stderr)
        return None
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(GRAPHQL_URL, data=body, method="POST")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "001zk-living-system")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"[fetch_telemetry] aviso: falha na consulta GraphQL: {e}", file=sys.stderr)
        return None


def compute_streak(weeks):
    """Recebe as semanas do contributionCalendar e calcula o streak atual
    (dias consecutivos, até hoje, com pelo menos 1 contribuição)."""
    days = []
    for week in weeks:
        for day in week.get("contributionDays", []):
            days.append(day)
    days.sort(key=lambda d: d["date"])

    streak = 0
    for day in reversed(days):
        if day["contributionCount"] > 0:
            streak += 1
        else:
            # permite que o dia de hoje ainda esteja zerado sem quebrar o streak
            if day["date"] == days[-1]["date"]:
                continue
            break
    return streak


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
        telemetry["activity_state"] = "ACTIVE" if repos else "N/A"

        # distribuição de linguagens por número de repositórios (top 5)
        lang_counts = {}
        for r in repos:
            lang = r.get("language")
            if lang:
                lang_counts[lang] = lang_counts.get(lang, 0) + 1
        if lang_counts:
            total = sum(lang_counts.values())
            top = sorted(lang_counts.items(), key=lambda kv: kv[1], reverse=True)[:5]
            telemetry["language_breakdown"] = [
                {"name": name, "percent": round(count / total * 100)}
                for name, count in top
            ]

        # atividade recente: repositórios com push mais recente (top 5)
        pushed = [r for r in repos if r.get("pushed_at") and not r.get("fork")]
        pushed.sort(key=lambda r: r["pushed_at"], reverse=True)
        if pushed:
            now = datetime.now(timezone.utc)
            recent = []
            for r in pushed[:5]:
                pushed_at = datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00"))
                days_ago = (now - pushed_at).days
                recent.append({
                    "name": r.get("name"),
                    "days_ago": days_ago,
                    "language": r.get("language"),
                })
            telemetry["recent_activity"] = recent

    # streak de contribuição via GraphQL (requer GITHUB_TOKEN)
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            weeks { contributionDays { date contributionCount } }
          }
        }
      }
    }
    """
    gql = graphql(query, {"login": HANDLE})
    if gql and gql.get("data", {}).get("user"):
        try:
            weeks = gql["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
            telemetry["contribution_streak"] = compute_streak(weeks)
        except (KeyError, TypeError) as e:
            print(f"[fetch_telemetry] aviso: não foi possível calcular streak: {e}", file=sys.stderr)

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
