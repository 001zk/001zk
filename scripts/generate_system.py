#!/usr/bin/env python3
"""
001ZK // LIVING SYSTEM
generate_system.py

Gera assets/living-system-light.svg e assets/living-system-dark.svg
a partir de data/profile.json, data/projects.json e (opcionalmente)
data/telemetry.json (produzido pelo pipeline da GitHub API).

Regra de ouro: nenhum dado é inventado. Quando um valor de telemetria
não está disponível, o gerador escreve "N/A" em vez de um número.

Uso:
    python3 scripts/generate_system.py
"""

import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
ASSETS_DIR = os.path.join(ROOT, "assets")

VIEWBOX_W = 1200
VIEWBOX_H = 880

FONT_MONO = "'JetBrains Mono','IBM Plex Mono','SF Mono',Consolas,monospace"
FONT_DISPLAY = "'Space Grotesk','IBM Plex Sans',Inter,Helvetica,Arial,sans-serif"

THEMES = {
    "light": {
        "bg": "#F7F7F5",
        "panel": "#FFFFFF",
        "grid": "#E7E7E3",
        "line": "#C9C9C4",
        "line_strong": "#33332E",
        "text_primary": "#171714",
        "text_secondary": "#5B5B55",
        "text_dim": "#9A9A92",
        "accent": "#0B5FFF",
        "accent_soft": "#DCE7FF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#33332E",
        "core_fill": "#171714",
        "core_text": "#F7F7F5",
    },
    "dark": {
        "bg": "#0B0C0B",
        "panel": "#131412",
        "grid": "#1E1F1C",
        "line": "#2B2C28",
        "line_strong": "#D8D8D2",
        "text_primary": "#F2F2EC",
        "text_secondary": "#A7A79E",
        "text_dim": "#63635C",
        "accent": "#4C8DFF",
        "accent_soft": "#16233F",
        "node_fill": "#131412",
        "node_stroke": "#D8D8D2",
        "core_fill": "#F2F2EC",
        "core_text": "#0B0C0B",
    },
}


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


# ---------------------------------------------------------------------------
# Layout: core node + five module nodes, asymmetric, non-grid placement.
# ---------------------------------------------------------------------------

CORE = {"x": 330, "y": 400, "r": 62}

MODULES_LAYOUT = [
    # id matches data/profile.json modules[].id
    {"id": "NODE/NET", "x": 640, "y": 160, "r": 40},
    {"id": "NODE/INF", "x": 960, "y": 270, "r": 40},
    {"id": "NODE/AUT", "x": 560, "y": 530, "r": 40},
    {"id": "NODE/SWE", "x": 900, "y": 530, "r": 40},
    {"id": "NODE/RES", "x": 1090, "y": 410, "r": 36},
]

STATE_GLYPH = {
    "ACTIVE": "\u25CF",       # ●
    "OPERATIONAL": "\u25CF",  # ●
    "STANDBY": "\u25CB",      # ○
    "GENERATED": "\u25C7",    # ◇
}


def bezier_path(x1, y1, x2, y2, bend=0.35):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    nx = -dy * bend
    ny = dx * bend
    cx, cy = mx + nx, my + ny
    return f"M {x1:.1f},{y1:.1f} Q {cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"


def build_svg(theme_name, profile, projects, telemetry):
    t = THEMES[theme_name]
    modules = {m["id"]: m for m in profile["modules"]}
    parts = []

    parts.append(
        f'<svg viewBox="0 0 {VIEWBOX_W} {VIEWBOX_H}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-labelledby="svgTitle svgDesc" font-family="{FONT_DISPLAY}">'
    )
    parts.append(
        "<title id=\"svgTitle\">001ZK // LIVING SYSTEM</title>"
    )
    parts.append(
        "<desc id=\"svgDesc\">Arquitetura de sistema interconectando rede, "
        "infraestrutura, automação, engenharia de software e pesquisa, "
        "representando a atuação de Luiz Gustavo (001zk).</desc>"
    )

    # ---- defs -------------------------------------------------------
    parts.append("<defs>")
    parts.append(
        f'<radialGradient id="coreGlow-{theme_name}" cx="50%" cy="50%" r="60%">'
        f'<stop offset="0%" stop-color="{t["accent"]}" stop-opacity="0.35"/>'
        f'<stop offset="100%" stop-color="{t["accent"]}" stop-opacity="0"/>'
        f"</radialGradient>"
    )
    parts.append(
        f'<pattern id="grid-{theme_name}" width="28" height="28" patternUnits="userSpaceOnUse">'
        f'<path d="M 28 0 L 0 0 0 28" fill="none" stroke="{t["grid"]}" stroke-width="1"/>'
        f"</pattern>"
    )
    parts.append("</defs>")

    # Interatividade só tem efeito quando o SVG é embutido inline (site externo).
    # Como <img> no README, o navegador ignora hover/focus de imagens — inofensivo.
    parts.append(
        f"<style>.ls-node{{cursor:pointer}}"
        f".ls-node circle:first-child{{transition:stroke .15s,filter .15s}}"
        f".ls-node:hover circle:first-child,.ls-node:focus circle:first-child"
        f"{{stroke:{t['accent']};filter:drop-shadow(0 0 6px {t['accent']})}}"
        f".ls-node:focus{{outline:none}}</style>"
    )

    # ---- background ---------------------------------------------------
    parts.append(f'<rect width="{VIEWBOX_W}" height="{VIEWBOX_H}" fill="{t["bg"]}"/>')
    parts.append(
        f'<rect width="{VIEWBOX_W}" height="{VIEWBOX_H}" fill="url(#grid-{theme_name})"/>'
    )

    # ---- connective paths (core -> modules) ---------------------------
    for i, m in enumerate(MODULES_LAYOUT):
        bend = 0.28 if i % 2 == 0 else -0.22
        d = bezier_path(CORE["x"], CORE["y"], m["x"], m["y"], bend=bend)
        path_id = f"path-{theme_name}-{i}"
        parts.append(
            f'<path id="{path_id}" d="{d}" fill="none" stroke="{t["line"]}" '
            f'stroke-width="1.4"/>'
        )
        # midpoint relay node
        parts.append(
            f'<circle cx="{(CORE["x"]+m["x"])/2:.1f}" cy="{(CORE["y"]+m["y"])/2 - 20*bend:.1f}" '
            f'r="3" fill="{t["line_strong"]}" opacity="0.55"/>'
        )
        # traveling particle
        parts.append(
            f'<circle r="3.2" fill="{t["accent"]}">'
            f'<animateMotion dur="{6 + i}s" repeatCount="indefinite" '
            f'path="{d}"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" '
            f'dur="{6+i}s" repeatCount="indefinite"/>'
            f"</circle>"
        )

    # ---- module nodes ---------------------------------------------------
    for m in MODULES_LAYOUT:
        meta = modules.get(m["id"], {})
        name = meta.get("name", m["id"])
        state = meta.get("state", "OPERATIONAL")
        glyph = STATE_GLYPH.get(state, "\u25CF")
        r = m["r"]
        x, y = m["x"], m["y"]
        parts.append(
            f'<g class="ls-node" data-node-id="{esc(m["id"])}" tabindex="0" '
            f'role="button" aria-label="{esc(name)} — {esc(state)}">'
        )
        parts.append(
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{t["node_fill"]}" '
            f'stroke="{t["node_stroke"]}" stroke-width="1.6"/>'
        )
        parts.append(
            f'<circle cx="{x}" cy="{y}" r="{r-9}" fill="none" '
            f'stroke="{t["line"]}" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{x}" y="{y-4}" text-anchor="middle" font-family="{FONT_MONO}" '
            f'font-size="9" fill="{t["text_dim"]}" letter-spacing="1">{esc(m["id"])}</text>'
        )
        parts.append(
            f'<text x="{x}" y="{y+10}" text-anchor="middle" font-family="{FONT_DISPLAY}" '
            f'font-size="12.5" font-weight="600" fill="{t["text_primary"]}">{esc(name)}</text>'
        )
        parts.append(
            f'<text x="{x}" y="{y+r+16}" text-anchor="middle" font-family="{FONT_MONO}" '
            f'font-size="8.5" fill="{t["accent"]}" letter-spacing="0.5">{glyph} {esc(state)}</text>'
        )
        # module item chips (small technical labels beneath, alternating side)
        items = meta.get("items", [])[:4]
        item_y = y + r + 32
        for j, it in enumerate(items):
            parts.append(
                f'<text x="{x}" y="{item_y + j*13}" text-anchor="middle" '
                f'font-family="{FONT_MONO}" font-size="8" fill="{t["text_secondary"]}">{esc(it)}</text>'
            )
        parts.append("</g>")

    # ---- core --------------------------------------------------------
    cx, cy, cr = CORE["x"], CORE["y"], CORE["r"]
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{cr+55}" fill="url(#coreGlow-{theme_name})"/>')
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{cr}" fill="{t["core_fill"]}" '
        f'stroke="{t["accent"]}" stroke-width="1.6"/>'
    )
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{cr+14}" fill="none" stroke="{t["line"]}" '
        f'stroke-width="1" stroke-dasharray="2 4"/>'
    )
    parts.append(
        f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="{FONT_DISPLAY}" '
        f'font-size="17" font-weight="700" fill="{t["core_text"]}" letter-spacing="1">001ZK</text>'
    )
    parts.append(
        f'<text x="{cx}" y="{cy+13}" text-anchor="middle" font-family="{FONT_MONO}" '
        f'font-size="8.5" fill="{t["core_text"]}" letter-spacing="1" opacity="0.75">SYSTEM CORE</text>'
    )

    # ---- header block --------------------------------------------------
    hx, hy = 60, 90
    parts.append(
        f'<text x="{hx}" y="{hy}" font-family="{FONT_DISPLAY}" font-size="44" '
        f'font-weight="700" fill="{t["text_primary"]}" letter-spacing="0.5">001ZK</text>'
    )
    parts.append(
        f'<text x="{hx}" y="{hy+30}" font-family="{FONT_MONO}" font-size="14" '
        f'fill="{t["accent"]}" letter-spacing="3">README</text>'
    )
    tagline = ["SOFTWARE ENGINEERING", "INFRASTRUCTURE", "AUTOMATION", "NETWORK SYSTEMS"]
    for i, line in enumerate(tagline):
        parts.append(
            f'<text x="{hx}" y="{hy+58 + i*16}" font-family="{FONT_MONO}" font-size="10.5" '
            f'fill="{t["text_secondary"]}" letter-spacing="1">{esc(line)}</text>'
        )

    # ---- build/revision micro-detail -----------------------------------
    parts.append(
        f'<text x="{VIEWBOX_W-40}" y="40" text-anchor="end" font-family="{FONT_MONO}" '
        f'font-size="9" fill="{t["text_dim"]}" letter-spacing="0.5">'
        f'SYSTEM REV. {esc(profile["system"]["revision"])} · BUILD {esc(profile["system"]["build"])}</text>'
    )
    parts.append(
        f'<text x="{VIEWBOX_W-40}" y="54" text-anchor="end" font-family="{FONT_MONO}" '
        f'font-size="9" fill="{t["text_dim"]}">{esc(profile["identity"]["location"])}</text>'
    )

    # ---- research node (R-01) ------------------------------------------
    rx, ry = 60, 670
    rw, rh = 1080, 78
    research = profile.get("research", {})
    parts.append(
        f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="4" fill="{t["panel"]}" '
        f'stroke="{t["line"]}" stroke-width="1"/>'
    )
    parts.append(
        f'<text x="{rx+16}" y="{ry+22}" font-family="{FONT_MONO}" font-size="9" '
        f'fill="{t["accent"]}" letter-spacing="1">{esc(research.get("id","R-01"))} / RESEARCH NODE — '
        f'{esc(research.get("codename",""))}</text>'
    )
    parts.append(
        f'<text x="{rx+16}" y="{ry+42}" font-family="{FONT_DISPLAY}" font-size="12.5" '
        f'font-weight="600" fill="{t["text_primary"]}">{esc(research.get("title",""))[:64]}</text>'
    )
    themes_line = "  ·  ".join(research.get("themes", []))
    parts.append(
        f'<text x="{rx+16}" y="{ry+62}" font-family="{FONT_MONO}" font-size="9" '
        f'fill="{t["text_secondary"]}" letter-spacing="0.5">{esc(themes_line)}</text>'
    )

    # ---- telemetry strip (bottom) --------------------------------------
    ty = VIEWBOX_H - 88
    parts.append(
        f'<line x1="60" y1="{ty}" x2="{VIEWBOX_W-60}" y2="{ty}" stroke="{t["line"]}" stroke-width="1"/>'
    )
    parts.append(
        f'<text x="60" y="{ty+22}" font-family="{FONT_MONO}" font-size="10" '
        f'fill="{t["text_dim"]}" letter-spacing="2">SYSTEM TELEMETRY</text>'
    )
    tele_fields = [
        ("REPOSITORIES", telemetry.get("public_repos", "N/A")),
        ("FOLLOWERS", telemetry.get("followers", "N/A")),
        ("LANGUAGES", telemetry.get("language_count", "N/A")),
        ("ACTIVITY", telemetry.get("activity_state", "N/A")),
    ]
    fx = 60
    for label, value in tele_fields:
        parts.append(
            f'<text x="{fx}" y="{ty+46}" font-family="{FONT_MONO}" font-size="9" '
            f'fill="{t["text_secondary"]}" letter-spacing="0.5">{esc(label)}</text>'
        )
        parts.append(
            f'<text x="{fx}" y="{ty+68}" font-family="{FONT_DISPLAY}" font-size="20" '
            f'font-weight="700" fill="{t["text_primary"]}">{esc(value)}</text>'
        )
        fx += 260

    parts.append("</svg>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Painéis compactos adicionais — mesma linguagem visual, dados reais via
# data/telemetry.json (fetch_telemetry.py). Sem dado real = "N/A", nunca
# um valor inventado.
# ---------------------------------------------------------------------------

PANEL_W = 560
PANEL_H = 220


def panel_shell(theme_name, title, t):
    slug = title.lower().replace(" ", "-")
    parts = [
        f'<svg viewBox="0 0 {PANEL_W} {PANEL_H}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-labelledby="pTitle-{theme_name}-{slug}" font-family="{FONT_DISPLAY}">',
        f'<title id="pTitle-{theme_name}-{slug}">{esc(title)}</title>',
        f'<rect width="{PANEL_W}" height="{PANEL_H}" fill="{t["bg"]}"/>',
        f'<text x="24" y="34" font-family="{FONT_MONO}" font-size="11" '
        f'fill="{t["text_dim"]}" letter-spacing="2">{esc(title)}</text>',
        f'<line x1="24" y1="46" x2="{PANEL_W-24}" y2="46" stroke="{t["line"]}" stroke-width="1"/>',
    ]
    return parts


def build_panel_languages(theme_name, telemetry):
    t = THEMES[theme_name]
    parts = panel_shell(theme_name, "LANGUAGE DISTRIBUTION", t)
    data = telemetry.get("language_breakdown")

    if not data:
        parts.append(
            f'<text x="24" y="100" font-family="{FONT_MONO}" font-size="12" '
            f'fill="{t["text_dim"]}">N/A</text>'
        )
    else:
        bar_x = 140
        bar_w = PANEL_W - bar_x - 24
        row_h = 30
        y0 = 68
        for i, lang in enumerate(data):
            y = y0 + i * row_h
            pct = lang["percent"]
            parts.append(
                f'<text x="24" y="{y+11}" font-family="{FONT_MONO}" font-size="10.5" '
                f'fill="{t["text_primary"]}">{esc(lang["name"])}</text>'
            )
            parts.append(
                f'<rect x="{bar_x}" y="{y}" width="{bar_w}" height="10" rx="2" '
                f'fill="none" stroke="{t["line"]}" stroke-width="1"/>'
            )
            parts.append(
                f'<rect x="{bar_x}" y="{y}" width="{bar_w*pct/100:.1f}" height="10" rx="2" '
                f'fill="{t["accent"]}"/>'
            )
            parts.append(
                f'<text x="{PANEL_W-24}" y="{y+9}" text-anchor="end" font-family="{FONT_MONO}" '
                f'font-size="9.5" fill="{t["text_dim"]}">{pct}%</text>'
            )

    parts.append("</svg>")
    return "\n".join(parts)


def build_panel_activity(theme_name, telemetry):
    t = THEMES[theme_name]
    parts = panel_shell(theme_name, "RECENT ACTIVITY", t)
    data = telemetry.get("recent_activity")

    if not data:
        parts.append(
            f'<text x="24" y="100" font-family="{FONT_MONO}" font-size="12" '
            f'fill="{t["text_dim"]}">N/A</text>'
        )
    else:
        row_h = 30
        y0 = 70
        for i, repo in enumerate(data):
            y = y0 + i * row_h
            days = repo["days_ago"]
            when = "today" if days == 0 else (f"{days}d ago" if days < 30 else f"{days//30}mo ago")
            parts.append(
                f'<circle cx="30" cy="{y-4}" r="3" fill="{t["accent"]}"/>'
            )
            parts.append(
                f'<text x="44" y="{y}" font-family="{FONT_MONO}" font-size="10.5" '
                f'fill="{t["text_primary"]}">{esc(repo["name"])}</text>'
            )
            lang = repo.get("language") or ""
            parts.append(
                f'<text x="{PANEL_W-24}" y="{y}" text-anchor="end" font-family="{FONT_MONO}" '
                f'font-size="9.5" fill="{t["text_dim"]}">{esc(lang)} · {esc(when)}</text>'
            )

    parts.append("</svg>")
    return "\n".join(parts)


def build_panel_streak(theme_name, telemetry):
    t = THEMES[theme_name]
    parts = panel_shell(theme_name, "CONTRIBUTION STREAK", t)
    streak = telemetry.get("contribution_streak")

    cx, cy, r = PANEL_W / 2, 140, 52
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{t["line"]}" stroke-width="1.4"/>'
    )
    if streak is None:
        parts.append(
            f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-family="{FONT_MONO}" '
            f'font-size="14" fill="{t["text_dim"]}">N/A</text>'
        )
    else:
        parts.append(
            f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="{FONT_DISPLAY}" '
            f'font-size="30" font-weight="700" fill="{t["text_primary"]}">{streak}</text>'
        )
        parts.append(
            f'<text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="{FONT_MONO}" '
            f'font-size="9" fill="{t["accent"]}" letter-spacing="1">DAYS</text>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


PANEL_BUILDERS = {
    "panel-languages": build_panel_languages,
    "panel-activity": build_panel_activity,
    "panel-streak": build_panel_streak,
}


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    profile = load("profile.json")
    projects = load("projects.json", {"projects": []})
    telemetry = load("telemetry.json", {})

    if profile is None:
        raise SystemExit("data/profile.json não encontrado — abortando geração.")

    for theme_name in THEMES:
        svg = build_svg(theme_name, profile, projects, telemetry)
        out_path = os.path.join(ASSETS_DIR, f"living-system-{theme_name}.svg")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg)
        size_kb = os.path.getsize(out_path) / 1024
        print(f"[generate_system] {out_path} ({size_kb:.1f} KB)")

        for panel_name, builder in PANEL_BUILDERS.items():
            svg = builder(theme_name, telemetry)
            out_path = os.path.join(ASSETS_DIR, f"{panel_name}-{theme_name}.svg")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(svg)
            size_kb = os.path.getsize(out_path) / 1024
            print(f"[generate_system] {out_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()