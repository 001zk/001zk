<picture>
<source media="(prefers-color-scheme: dark)" srcset="assets/living-system-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/living-system-light.svg">
  <img alt="Mapa de projetos públicos de Luiz Gustavo" src="assets/living-system-light.svg">
</picture> <div align="center">

[**VER MAPA DE PROJETOS ↗**](https://001zk.github.io/001zk/)

</div>

---

## SOBRE

Sou Luiz Gustavo, estudante de Engenharia de Software e Analista de Suporte de TI Jr. Trabalho com suporte, redes, infraestrutura, automação e desenvolvimento de soluções web.

O mapa acima seleciona automaticamente cinco repositórios públicos da minha conta no GitHub. O tamanho de cada planeta acompanha o tamanho real do repositório, enquanto a página interativa permite abrir cada projeto diretamente.

---

## EXPERIÊNCIA

**Minsait / Indra Company** — Analista de Suporte de TI Jr

**Arroba Banda Larga** — Analista de NOC / TI Interno

Experiência com `GPON` `EPON` `OLT` `ONU` `Zabbix` `IXC` `Proxmox` `VPN`, troubleshooting de redes, infraestrutura corporativa e suporte N2/N3.

---

## PROJETOS

Os repositórios do mapa são detectados automaticamente pela API do GitHub e registrados em [`data/repos.json`](data/repos.json). O sistema seleciona os cinco maiores repositórios públicos próprios e atualiza os assets por meio do [workflow automático](.github/workflows/update-system.yml).

Projetos adicionais ou selecionados manualmente podem ser consultados em [`data/projects.json`](data/projects.json).

---

## PESQUISA

**R-01 — REUSABLE COMPUTING**

[*Manual de Montagem de um Computador Reciclável Utilizando Peças Reaproveitadas*](https://zenodo.org/records/18135901)

`HARDWARE` `REUSE` `SUSTAINABILITY` · publicado no Zenodo

---

## FORMAÇÃO

Engenharia de Software — Estácio de Sá, cursando

Técnico em Informática — concluído

---

## CERTIFICAÇÕES

**OCNA Wireless** — TP-Link

**Ignite Brasil — Empreendedorismo** — Wadhwani Foundation

---

## TECNOLOGIAS

`Python` `Node.js` `JavaScript` `Google Apps Script` `Linux` `Git` `GitHub`

---

## CONTATO

[GitHub](https://github.com/001zk) · [GitHub alternativo](https://github.com/Luiz-alt001) · [LinkedIn](https://www.linkedin.com/in/luiz-gustavo-de-barros/) · [Portfólio](https://portfolio-luizs-projects-9a2b01d1.vercel.app/)

---

<sub>Sistema atualizado automaticamente a partir dos dados públicos do GitHub. A geração usa <a href="scripts/fetch_repos.py">scripts/fetch_repos.py</a>, <a href="scripts/generate_system.py">scripts/generate_system.py</a> e <a href="scripts/generate_web.py">scripts/generate_web.py</a>.</sub>

---

<details>
<summary><sub>Execução manual</sub></summary>

```bash
python3 scripts/fetch_repos.py
python3 scripts/generate_system.py
python3 scripts/generate_web.py
python3 scripts/validate_assets.py
```

O workflow do GitHub Actions executa esse processo automaticamente todos os dias e também pode ser iniciado manualmente em **Actions → update-system → Run workflow**.

</details>
