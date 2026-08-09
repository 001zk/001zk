# web/ — OPEN SYSTEM (experiência complementar)

Este diretório é reservado para uma futura versão interativa do
Living System, hospedada via GitHub Pages em `001zk.github.io`.

O README principal **nunca depende** deste diretório — ele funciona
sozinho, com Markdown e SVG estático.

## Escopo planejado

```text
README (estático, funciona sempre)
   │
   └──────► GitHub Pages (opcional, complementar)
                 │
                 ├── 2D SVG mode      — a mesma composição do README, em tela cheia
                 ├── interactive mode — nodes clicáveis, hover com detalhes de cada módulo
                 └── 3D mode          — exploração via Three.js (opcional, fase final)
```

## Regras

- Nada aqui deve contaminar a simplicidade do `README.md`.
- O link `[ OPEN SYSTEM ↗ ]` no README aponta para cá quando publicado.
- Se implementado, reutilize `data/profile.json` como fonte única de dados —
  não duplique identidade/experiência em código separado.
- WebGL, Canvas e JavaScript interativo só existem aqui, nunca no README.

## Status

`index.html` já é gerado por [`scripts/generate_web.py`](../scripts/generate_web.py)
a partir dos mesmos dados do README (`data/profile.json` etc.) — reaproveita
os SVGs de `assets/`. Para ficar no ar em `001zk.github.io`, falta apenas
habilitar o Pages nas configurações do repositório (veja o README principal).

O 2D/3D interativo com Three.js/Canvas descrito acima continua não
implementado — é a evolução futura sobre esta base estática atual.
