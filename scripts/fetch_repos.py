#!/usr/bin/env python3
"""
001ZK // LIVING SYSTEM
fetch_repos.py

Consulta os repositórios públicos da conta no GitHub e salva os cinco maiores
repositórios próprios em data/repos.json. O tamanho retornado pela API é em KB
e será usado pelo gerador para dimensionar os planetas do SVG.

Nenhum projeto é cadastrado manualmente: o workflow pode rodar diariamente ou
sob demanda e sempre reconstrói a seleção a partir do estado atual do GitHub.
"""

import json
import os
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
OUT_PATH = os.path.join(DATA_DIR, "repos.json")
HANDLE = os.environ.get("GITHUB_HANDLE", "001zk")
MAX_REPOS = 5


def fetch_repositories():
    url = f"https://api.github.com/users/{HANDLE}/repos?per_page=100&sort=updated"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "001zk-living-system",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def normalize(repo):
    return {
        "name": repo["name"],
        "url": repo["html_url"],
        "description": repo.get("description") or "Sem descrição no GitHub.",
        "language": repo.get("language") or "N/A",
        "size_kb": max(0, int(repo.get("size") or 0)),
        "updated_at": repo.get("pushed_at") or repo.get("updated_at"),
        "stars": int(repo.get("stargazers_count") or 0),
    }


def main():
    try:
        raw_repos = fetch_repositories()
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        if os.path.exists(OUT_PATH):
            print(f"[fetch_repos] API indisponível; mantendo {OUT_PATH}: {exc}")
            return
        raise SystemExit(f"[fetch_repos] não foi possível consultar o GitHub: {exc}")

    candidates = [
        repo for repo in raw_repos
        if not repo.get("private")
        and not repo.get("fork")
        and repo.get("name") != HANDLE
        and not repo.get("archived")
    ]
    candidates.sort(
        key=lambda repo: (
            int(repo.get("size") or 0),
            repo.get("pushed_at") or repo.get("updated_at") or "",
        ),
        reverse=True,
    )

    payload = {
        "source": f"https://github.com/{HANDLE}",
        "account": HANDLE,
        "selection": "top_5_by_repository_size",
        "total_public_repositories": len(candidates),
        "repositories": [normalize(repo) for repo in candidates[:MAX_REPOS]],
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as output:
        json.dump(payload, output, ensure_ascii=False, indent=2)
        output.write("\n")

    print(
        f"[fetch_repos] {len(payload['repositories'])} repositórios selecionados "
        f"de {len(candidates)} públicos em {OUT_PATH}"
    )
    for repo in payload["repositories"]:
        print(f"  - {repo['name']}: {repo['size_kb']} KB")


if __name__ == "__main__":
    main()
