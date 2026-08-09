#!/usr/bin/env python3
"""
001ZK // LIVING SYSTEM
validate_assets.py

Valida a integridade do repositório antes de um commit/deploy:
- JSON válido em data/
- SVG bem-formado em assets/
- tamanho dos SVGs dentro do orçamento (aviso > 300KB, falha > 500KB)
- arquivos obrigatórios presentes
- README referencia os dois temas de SVG

Retorna código de saída != 0 se houver um problema crítico,
para que o workflow do GitHub Actions falhe corretamente.
"""

import json
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "README.md",
    "index.html",
    "data/profile.json",
    "data/projects.json",
    "data/links.json",
    "assets/living-system-light.svg",
    "assets/living-system-dark.svg",
    "scripts/generate_system.py",
    "scripts/generate_web.py",
    ".github/workflows/update-system.yml",
]

WARN_KB = 300
FAIL_KB = 500

errors = []
warnings = []


def check_required_files():
    for rel in REQUIRED_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            errors.append(f"Arquivo obrigatório ausente: {rel}")


def check_json_files():
    data_dir = os.path.join(ROOT, "data")
    if not os.path.isdir(data_dir):
        return
    for name in os.listdir(data_dir):
        if not name.endswith(".json"):
            continue
        path = os.path.join(data_dir, name)
        try:
            with open(path, "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"JSON inválido em data/{name}: {e}")


def check_svg_files():
    assets_dir = os.path.join(ROOT, "assets")
    if not os.path.isdir(assets_dir):
        return
    for name in os.listdir(assets_dir):
        if not name.endswith(".svg"):
            continue
        path = os.path.join(assets_dir, name)
        size_kb = os.path.getsize(path) / 1024

        try:
            ET.parse(path)
        except ET.ParseError as e:
            errors.append(f"SVG malformado em assets/{name}: {e}")
            continue

        if size_kb > FAIL_KB:
            errors.append(
                f"assets/{name} tem {size_kb:.1f} KB — acima do limite crítico de {FAIL_KB} KB"
            )
        elif size_kb > WARN_KB:
            warnings.append(
                f"assets/{name} tem {size_kb:.1f} KB — acima do ideal de {WARN_KB} KB"
            )

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "<script" in content.lower():
            errors.append(f"assets/{name} contém <script> — não permitido em SVG embutido no README")


def check_readme_references():
    readme_path = os.path.join(ROOT, "README.md")
    if not os.path.exists(readme_path):
        return
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "living-system-light.svg" not in content and "living-system-dark.svg" not in content:
        errors.append("README.md não referencia os assets de living-system (light/dark)")
    if "<script" in content.lower():
        errors.append("README.md contém <script> — GitHub sanitiza e a experiência quebrará")
    if "<iframe" in content.lower():
        errors.append("README.md contém <iframe> — não suportado no GitHub README")


def main():
    check_required_files()
    check_json_files()
    check_svg_files()
    check_readme_references()

    print("=== 001ZK // LIVING SYSTEM — validate_assets ===")
    if warnings:
        print(f"\n{len(warnings)} aviso(s):")
        for w in warnings:
            print(f"  ! {w}")

    if errors:
        print(f"\n{len(errors)} erro(s) crítico(s):")
        for e in errors:
            print(f"  x {e}")
        print("\nValidação FALHOU.")
        sys.exit(1)

    print("\nValidação OK — nenhum problema crítico encontrado.")
    sys.exit(0)


if __name__ == "__main__":
    main()
