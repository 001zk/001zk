<div align="center">

<svg width="900" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#06090d"/>
      <stop offset="100%" style="stop-color:#0c1a28"/>
    </linearGradient>
    <linearGradient id="line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:0"/>
      <stop offset="30%" style="stop-color:#f59e0b;stop-opacity:1"/>
      <stop offset="70%" style="stop-color:#f59e0b;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#f59e0b;stop-opacity:0"/>
    </linearGradient>
    <linearGradient id="nameglow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#ffffff"/>
      <stop offset="100%" style="stop-color:#c8d8e8"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="900" height="200" fill="url(#bg)" rx="12"/>

  <!-- Border -->
  <rect width="900" height="200" fill="none" stroke="#1c2b3a" stroke-width="1" rx="12"/>

  <!-- Amber accent left bar -->
  <rect x="0" y="0" width="3" height="200" fill="#f59e0b" rx="2"/>

  <!-- Decorative grid dots -->
  <g opacity="0.06">
    <circle cx="700" cy="40"  r="1.5" fill="#f59e0b"/>
    <circle cx="730" cy="40"  r="1.5" fill="#f59e0b"/>
    <circle cx="760" cy="40"  r="1.5" fill="#f59e0b"/>
    <circle cx="790" cy="40"  r="1.5" fill="#f59e0b"/>
    <circle cx="820" cy="40"  r="1.5" fill="#f59e0b"/>
    <circle cx="850" cy="40"  r="1.5" fill="#f59e0b"/>
    <circle cx="700" cy="70"  r="1.5" fill="#f59e0b"/>
    <circle cx="730" cy="70"  r="1.5" fill="#f59e0b"/>
    <circle cx="760" cy="70"  r="1.5" fill="#f59e0b"/>
    <circle cx="790" cy="70"  r="1.5" fill="#f59e0b"/>
    <circle cx="820" cy="70"  r="1.5" fill="#f59e0b"/>
    <circle cx="850" cy="70"  r="1.5" fill="#f59e0b"/>
    <circle cx="700" cy="100" r="1.5" fill="#f59e0b"/>
    <circle cx="730" cy="100" r="1.5" fill="#f59e0b"/>
    <circle cx="760" cy="100" r="1.5" fill="#f59e0b"/>
    <circle cx="790" cy="100" r="1.5" fill="#f59e0b"/>
    <circle cx="820" cy="100" r="1.5" fill="#f59e0b"/>
    <circle cx="850" cy="100" r="1.5" fill="#f59e0b"/>
    <circle cx="700" cy="130" r="1.5" fill="#f59e0b"/>
    <circle cx="730" cy="130" r="1.5" fill="#f59e0b"/>
    <circle cx="760" cy="130" r="1.5" fill="#f59e0b"/>
    <circle cx="790" cy="130" r="1.5" fill="#f59e0b"/>
    <circle cx="820" cy="130" r="1.5" fill="#f59e0b"/>
    <circle cx="850" cy="130" r="1.5" fill="#f59e0b"/>
    <circle cx="700" cy="160" r="1.5" fill="#f59e0b"/>
    <circle cx="730" cy="160" r="1.5" fill="#f59e0b"/>
    <circle cx="760" cy="160" r="1.5" fill="#f59e0b"/>
    <circle cx="790" cy="160" r="1.5" fill="#f59e0b"/>
    <circle cx="820" cy="160" r="1.5" fill="#f59e0b"/>
    <circle cx="850" cy="160" r="1.5" fill="#f59e0b"/>
  </g>

  <!-- Status indicator -->
  <circle cx="42" cy="44" r="4" fill="#22d3a0" filter="url(#glow)"/>
  <text x="54" y="49" font-family="monospace" font-size="11" fill="#22d3a0" letter-spacing="2">ONLINE · NOC ATIVO</text>

  <!-- Main name -->
  <text x="40" y="110" font-family="'Arial Black', sans-serif" font-size="52" font-weight="900" fill="url(#nameglow)" letter-spacing="-2">LUIZ</text>
  <text x="40" y="162" font-family="'Arial Black', sans-serif" font-size="52" font-weight="900" fill="#f59e0b" letter-spacing="-2" filter="url(#softglow)">GUSTAVO.</text>

  <!-- Role text -->
  <text x="340" y="110" font-family="monospace" font-size="13" fill="#8fa8be" letter-spacing="1">Analista de NOC &amp; Infraestrutura</text>
  <text x="340" y="132" font-family="monospace" font-size="13" fill="#8fa8be" letter-spacing="1">de Redes · Arroba Banda Larga</text>

  <!-- Tags -->
  <rect x="340" y="148" width="72"  height="20" rx="3" fill="#1c2b3a" stroke="#263a4d" stroke-width="1"/>
  <text x="352" y="162" font-family="monospace" font-size="10" fill="#f59e0b">GPON/EPON</text>

  <rect x="420" y="148" width="44"  height="20" rx="3" fill="#1c2b3a" stroke="#263a4d" stroke-width="1"/>
  <text x="431" y="162" font-family="monospace" font-size="10" fill="#f59e0b">VPN</text>

  <rect x="472" y="148" width="68"  height="20" rx="3" fill="#1c2b3a" stroke="#263a4d" stroke-width="1"/>
  <text x="481" y="162" font-family="monospace" font-size="10" fill="#f59e0b">Apps Script</text>

  <rect x="548" y="148" width="56"  height="20" rx="3" fill="#1c2b3a" stroke="#263a4d" stroke-width="1"/>
  <text x="557" y="162" font-family="monospace" font-size="10" fill="#f59e0b">MikroTik</text>

  <!-- Bottom line -->
  <rect x="0" y="192" width="900" height="1" fill="url(#line)"/>

  <!-- Bottom info -->
  <text x="40"  y="184" font-family="monospace" font-size="10" fill="#4a6070" letter-spacing="1">$ ping luizgustavobarros32@gmail.com</text>
  <text x="750" y="184" font-family="monospace" font-size="10" fill="#4a6070">Campos dos Goytacazes, RJ</text>
</svg>

</div>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luiz-gustavo-de-barros/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/lzk001/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:luizgustavobarros32@gmail.com)
[![Portfólio](https://img.shields.io/badge/Portfólio-f59e0b?style=flat-square&logo=vercel&logoColor=black)](https://portfolio-luizs-projects-9a2b01d1.vercel.app/)

![Status](https://img.shields.io/badge/Status-Disponível-22d3a0?style=flat-square)
![Localização](https://img.shields.io/badge/Localização-Campos%20dos%20Goytacazes%2C%20RJ-1c2b3a?style=flat-square)
![Aberto a](https://img.shields.io/badge/Aberto%20a-NOC%20·%20Redes%20·%20Automação%20·%20Projetos-f59e0b?style=flat-square)

</div>

---

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=3000&pause=1000&color=F59E0B&center=true&vCenter=true&multiline=false&repeat=true&width=500&lines=Analista+de+NOC+%26+Infraestrutura+de+Redes;GPON+%2F+EPON+%7C+VPN+%7C+Virtualização;Automação+com+Python+%26+Google+Apps+Script;Monitoramento+%7C+Troubleshooting+L2%2FL3)](https://git.io/typing-svg)

</div>

---

## `whoami`

```yaml
nome      : Luiz Gustavo de Barros
cargo     : Analista de NOC & TI Interno
empresa   : Arroba Banda Larga
local     : Campos dos Goytacazes, RJ — Brasil
foco      : GPON/EPON · VPN · Automação · Troubleshooting L2/L3
automação : Python · Google Apps Script · Node.js
portfólio : https://portfolio-luizs-projects-9a2b01d1.vercel.app/
formação  : Técnico em Informática — Estácio de Sá
aberto a  : NOC · Redes · Infraestrutura · Automação · Projetos
```

Atuo na operação de redes ópticas **GPON/EPON**, monitoramento de infraestrutura, provisionamento de ONU/ONT, configuração de VPNs e troubleshooting avançado de camadas 2 e 3. Complementarmente, desenvolvo scripts de automação com **Python** e **Google Apps Script** — integrando Sheets, Forms e APIs internas para eliminar trabalho manual em processos operacionais. Tenho interesse em colaborar com projetos de automação, ferramentas internas e webapps leves.

🔗 **[Ver portfólio completo →](https://portfolio-luizs-projects-9a2b01d1.vercel.app/)**

---

## Stack

**Redes & Infraestrutura**

![GPON](https://img.shields.io/badge/GPON%20%2F%20EPON-0d1117?style=for-the-badge&logo=cisco&logoColor=f59e0b)
![MikroTik](https://img.shields.io/badge/MikroTik-0d1117?style=for-the-badge&logo=mikrotik&logoColor=f59e0b)
![NOC](https://img.shields.io/badge/NOC%20%2F%20Monitoramento-0d1117?style=for-the-badge&logo=statuspage&logoColor=f59e0b)
![VPN](https://img.shields.io/badge/VPN%20%2F%20Firewall-0d1117?style=for-the-badge&logo=wireguard&logoColor=f59e0b)
![TCP/IP](https://img.shields.io/badge/TCP%2FIP%20%2F%20Roteamento-0d1117?style=for-the-badge&logo=cloudflare&logoColor=f59e0b)
![Zabbix](https://img.shields.io/badge/Zabbix-0d1117?style=for-the-badge&logo=zabbix&logoColor=f59e0b)
![IXC](https://img.shields.io/badge/IXC%20Soft-0d1117?style=for-the-badge&logo=databricks&logoColor=f59e0b)

**Sistemas & Virtualização**

![Linux](https://img.shields.io/badge/Linux%20%2F%20CLI-0d1117?style=for-the-badge&logo=linux&logoColor=f59e0b)
![VMware](https://img.shields.io/badge/VMware-0d1117?style=for-the-badge&logo=vmware&logoColor=f59e0b)
![Proxmox](https://img.shields.io/badge/Proxmox-0d1117?style=for-the-badge&logo=proxmox&logoColor=f59e0b)
![Windows Server](https://img.shields.io/badge/Windows%20Server-0d1117?style=for-the-badge&logo=windows&logoColor=f59e0b)

**Desenvolvimento & Automação**

![Python](https://img.shields.io/badge/Python-0d1117?style=for-the-badge&logo=python&logoColor=f59e0b)
![JavaScript](https://img.shields.io/badge/JavaScript-0d1117?style=for-the-badge&logo=javascript&logoColor=f59e0b)
![Node.js](https://img.shields.io/badge/Node.js-0d1117?style=for-the-badge&logo=node.js&logoColor=f59e0b)
![Apps Script](https://img.shields.io/badge/Google%20Apps%20Script-0d1117?style=for-the-badge&logo=google&logoColor=f59e0b)
![Discord.js](https://img.shields.io/badge/Discord.js-0d1117?style=for-the-badge&logo=discord&logoColor=f59e0b)

---

## Trajetória

<div align="center">

| Período | Cargo | Empresa |
|:-------:|-------|---------|
| `2025 – presente` | **Analista de NOC & TI Interno** | Arroba Banda Larga |
| `2024 – 2025` | Estagiário de NOC N3 / TI Interno | Arroba Banda Larga |
| `2023 – 2024` | Estagiário de Suporte N2 | Arroba Banda Larga |
| `2022 – 2023` | Estagiário de TI | Microlins |

</div>

---

## Formação Complementar

<div align="center">

| | Curso | Área |
|-|-------|------|
| 🔒 | Cibersegurança: Anatomia Clássica de um Ciberataque | Segurança |
| 🌐 | Redes, Lógica e Estruturação | Redes |
| 🌐 | Internet das Coisas — IoT | Redes |
| 🐍 | Python Básico | Dev |
| 🐍 | Python: Programação Orientada a Objetos | Dev |
| 📊 | Fundamentos de Ciência de Dados — FM2S | Dados |
| 📊 | Governança de Dados | Dados |
| 🏢 | TI como Elemento Estratégico nas Organizações | Gestão |
| 🖥️ | Fundamentos de TI: Hardware e Software | Infraestrutura |
| 📈 | Excel Avançado | Ferramentas |
| 📈 | Excel 2021 | Ferramentas |

</div>

---

## Estatísticas

<div align="center">
  <img src="http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=001zk&theme=github_dark" width="100%"/>
</div>

<br/>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=001zk&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=f59e0b&icon_color=f59e0b&text_color=c8d8e8&ring_color=f59e0b" height="165"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=001zk&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=f59e0b&text_color=c8d8e8" height="165"/>
</div>

---

## Contato

Aberto a oportunidades em **redes, NOC e infraestrutura**, colaborações em **projetos de automação** e desenvolvimento de soluções com **Google Apps Script** — webapps internas, integrações com Sheets/Forms e scripts de operação.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Luiz%20Gustavo%20de%20Barros-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luiz-gustavo-de-barros/)
[![Portfólio](https://img.shields.io/badge/Portfólio-Ver%20agora-f59e0b?style=for-the-badge&logo=vercel&logoColor=black)](https://portfolio-luizs-projects-9a2b01d1.vercel.app/)
[![Instagram](https://img.shields.io/badge/Instagram-@lzk001-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/lzk001/)
[![Email](https://img.shields.io/badge/Email-luizgustavobarros32@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:luizgustavobarros32@gmail.com)

</div>

---

<div align="center">
  <sub>Campos dos Goytacazes, RJ · Brasil · 2026</sub>
</div>
