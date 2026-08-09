#!/usr/bin/env python3
"""
001ZK // LIVING SYSTEM
generate_web.py

Gera index.html na raiz do repositório — a página que o GitHub Pages
serve em https://001zk.github.io assim que o Pages for habilitado
em Settings > Pages > Source: Deploy from a branch (main / root).

A página é HTML puro + CSS, sem dependência de build (Node, etc).
Reaproveita os mesmos assets/living-system-{light,dark}.svg e os
mesmos dados de data/*.json usados no README, então README e Pages
nunca ficam dessincronizados quando você roda o pipeline completo:

    python3 scripts/generate_system.py
    python3 scripts/generate_web.py
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")


def load(name, default=None):
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def esc(s):
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render(profile, projects, links):
    modules = profile["modules"]
    research = profile["research"]
    certs = profile["certifications"]
    prev = profile["previous_experience"]
    curr = profile["current_role"]

    module_rows = "\n".join(
        f'<tr><td class="mono accent">{esc(m["id"])}</td>'
        f'<td>{esc(m["name"])}</td>'
        f'<td class="mono dim">{" · ".join(esc(i) for i in m["items"])}</td></tr>'
        for m in modules
    )

    cert_rows = "\n".join(
        f'<div class="cert"><span class="mono accent">{esc(c["id"])}</span>'
        f'<span>{esc(c["name"])}</span><span class="dim">{esc(c["issuer"])}</span></div>'
        for c in certs
    )

    project_rows = "\n".join(
        f'<div class="project">'
        f'<div class="project-name">{esc(p["name"])}</div>'
        f'<div class="dim">{esc(p["description"])}</div>'
        f'<div class="mono dim small">{" · ".join(esc(s) for s in p.get("stack", []))} — {esc(p.get("status",""))}</div>'
        f'</div>'
        for p in projects.get("projects", [])
    )

    gh = links.get("github", "#")
    gh_alt = links.get("github_alt")
    gh_alt_html = f' · <a href="{esc(gh_alt)}">alt</a>' if gh_alt else ""

    doi = links.get("research_doi")
    research_title_html = (
        f'<a href="{esc(doi)}">{esc(research["title"])}</a>' if doi else esc(research["title"])
    )

    contact_links = [f'<a href="{esc(gh)}">GitHub</a>']
    if gh_alt:
        contact_links.append(f'<a href="{esc(gh_alt)}">GitHub (alt)</a>')
    if links.get("linkedin"):
        contact_links.append(f'<a href="{esc(links["linkedin"])}">LinkedIn</a>')
    if links.get("portfolio"):
        contact_links.append(f'<a href="{esc(links["portfolio"])}">Portfolio</a>')
    contact_html = " · ".join(contact_links)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>001ZK // LIVING SYSTEM</title>
<meta name="description" content="Arquitetura de sistema — rede, infraestrutura, automação, engenharia de software e pesquisa.">
<style>
  :root {{
    --bg: #F7F7F5; --panel: #FFFFFF; --line: #E3E3DE; --text: #171714;
    --text-dim: #5B5B55; --accent: #0B5FFF; --mono: 'JetBrains Mono','SF Mono',Consolas,monospace;
    --display: 'Space Grotesk',Inter,Helvetica,Arial,sans-serif;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #0B0C0B; --panel: #131412; --line: #23241F; --text: #F2F2EC;
      --text-dim: #A7A79E; --accent: #4C8DFF;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font-family: var(--display); line-height: 1.5;
  }}
  .wrap {{ max-width: 920px; margin: 0 auto; padding: 0 24px 80px; }}
  .hero img {{ width: 100%; height: auto; display: block; }}
  .mono {{ font-family: var(--mono); }}
  .accent {{ color: var(--accent); }}
  .dim {{ color: var(--text-dim); }}
  .small {{ font-size: 0.8em; }}
  h2 {{
    font-family: var(--mono); font-size: 13px; letter-spacing: 2px;
    text-transform: uppercase; color: var(--text-dim);
    margin: 56px 0 16px; padding-bottom: 8px; border-bottom: 1px solid var(--line);
  }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  td {{ padding: 8px 8px 8px 0; border-bottom: 1px solid var(--line); vertical-align: top; }}
  .cert, .project {{ padding: 12px 0; border-bottom: 1px solid var(--line); }}
  .cert {{ display: flex; gap: 12px; align-items: baseline; font-size: 14px; }}
  .project-name {{ font-weight: 600; margin-bottom: 4px; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  footer {{ margin-top: 64px; font-size: 12px; color: var(--text-dim); font-family: var(--mono); }}
  .back {{ display: inline-block; margin: 24px 0; font-family: var(--mono); font-size: 12px; }}
</style>
</head>
<body>
  <div class="hero">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/living-system-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/living-system-light.svg">
      <img alt="001ZK Living System" src="assets/living-system-light.svg">
    </picture>
  </div>

  <div class="wrap">
    <a class="back" href="{esc(gh)}">← README no GitHub</a>

    <h2>System</h2>
    <p>001ZK // LIVING SYSTEM representa como rede, infraestrutura, automação, software e pesquisa se conectam — não como timeline, mas como arquitetura.</p>

    <h2>Experience</h2>
    <p><strong>Current node</strong> — {esc(curr["company"])} · {esc(curr["title"])}</p>
    <p><strong>Previous node</strong> — {esc(prev["company"])} · {esc(prev["role"])}<br>
    <span class="mono dim small">{" · ".join(esc(s) for s in prev["skills"])}</span></p>

    <h2>Engineering</h2>
    <table>{module_rows}</table>

    <h2>Research</h2>
    <p class="mono accent small">{esc(research["id"])} / RESEARCH NODE — {esc(research["codename"])}</p>
    <p><strong>{research_title_html}</strong></p>
    <p class="mono dim small">{" · ".join(esc(t) for t in research["themes"])}</p>

    <h2>Certifications</h2>
    {cert_rows}

    <h2>Projects</h2>
    {project_rows}

    <h2>Contact</h2>
    <p>{contact_html}</p>

    <footer>SYSTEM REV. {esc(profile["system"]["revision"])} · BUILD {esc(profile["system"]["build"])}</footer>
  </div>
</body>
</html>
"""


def main():
    profile = load("profile.json")
    projects = load("projects.json", {"projects": []})
    links = load("links.json", {})

    if profile is None:
        raise SystemExit("data/profile.json não encontrado — abortando geração.")

    html = render(profile, projects, links)
    out_path = os.path.join(ROOT, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[generate_web] {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")


if __name__ == "__main__":
    main()