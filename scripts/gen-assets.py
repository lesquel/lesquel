"""Generate the profile README's SVG assets.

Single source of truth for every file in ../assets. Each asset is emitted in a
light and a dark variant from one shared definition, so the two themes cannot
drift apart. Edit this file and re-run it -- never hand-edit the SVGs.

    python3 scripts/gen-assets.py

SVG text does not wrap and is clipped at the canvas edge, so line lengths must
stay within the canvas: monospace advances about 0.6em per character, Georgia
italic about 0.45em.
"""

import html
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SERIF = "Georgia, 'Times New Roman', serif"

THEMES = {
    "dark":  {"fg": "#e6edf3", "muted": "#8b949e", "accent": "#58a6ff", "dim": "#6e7681", "rule": "#21262d"},
    "light": {"fg": "#1f2328", "muted": "#57606a", "accent": "#0969da", "dim": "#6e7781", "rule": "#d0d7de"},
}

def e(s):
    return html.escape(s, quote=True)

def write(name, body):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", path)

# ---------------------------------------------------------------- header
HEADER_LABEL = "MIQUEL — ECUADOR"
HEADER_L1_PRE, HEADER_L1_EM, HEADER_L1_POST = "Builds it, ", "ships it,", ""
HEADER_L2 = "runs it."
HEADER_SUB = "Full stack software engineer — backend & cloud infrastructure. Now: Go, FastAPI, CI/CD on GCP."
HEADER_ALT = ("Miquel — Ecuador. Builds it, ships it, runs it. Full stack software engineer: "
              "backend and cloud infrastructure; now building with Go, FastAPI and CI/CD on GCP.")

def header(theme):
    c = THEMES[theme]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="196" viewBox="0 0 820 196" role="img" aria-label="{e(HEADER_ALT)}">
  <text x="2" y="22" font-family="{MONO}" font-size="11" letter-spacing="3" fill="{c['muted']}">{e(HEADER_LABEL)}</text>
  <text x="0" y="80" font-family="{SERIF}" font-size="52" fill="{c['fg']}">{e(HEADER_L1_PRE)}<tspan font-style="italic" fill="{c['accent']}">{e(HEADER_L1_EM)}</tspan></text>
  <text x="0" y="134" font-family="{SERIF}" font-size="52" fill="{c['fg']}">{e(HEADER_L2)}</text>
  <text x="2" y="170" font-family="{SERIF}" font-style="italic" font-size="16" fill="{c['muted']}">{e(HEADER_SUB)}</text>
  <rect x="2" y="186" width="120" height="2" fill="{c['accent']}"/>
</svg>
'''

# ---------------------------------------------------------------- works
WORKS = [
    ("01", "Your coding agent, from your phone.", "open-remote-control · typescript · opencode",
     ["A remote control plugin for OpenCode — monitor sessions, send prompts and approve",
      "permissions from a web dashboard, over a tunnel, by QR pairing or from Telegram."]),
    ("02", "An ERP across three clouds.", "erp-cross-cfc · angular · go",
     ["Crossworlds CFC ERP: an Angular front end and a Go backend in one monorepo,",
      "deployed to Vercel, Cloud Run and Neon from a single pipeline."]),
    ("03", "Restaurant management, as a service.", "multi-rest · go · angular",
     ["A multi-restaurant SaaS — a Go API and an Angular 21 front end, split into",
      "dedicated backend and frontend repositories around one shared domain."]),
    ("04", "Nutrition, with a little help from AI.", "nutricia · python · typescript",
     ["A nutrition platform built end to end: Python backend, TypeScript front end",
      "and an Android build published straight from the repository."]),
    ("05", "Surgical pre-authorization, digitised.", "pre-autorizacion-quirurgica · python",
     ["The paperwork path between clinic and insurer, turned into software —",
      "requests, approvals and traceability in one system."]),
    ("06", "Insurance fraud, flagged by AI.", "centinela-ia · angular · fastapi · langgraph",
     ["An AI agent that flags possible fraud in insurance claims — hackIAthon 2026,",
      "Aseguradora del Sur challenge. It alerts, never accuses. With StevSant and DweskZ."]),
]

def works(num, title, meta, lines, theme):
    c = THEMES[theme]
    alt = f"{num} — {title} {meta}: {' '.join(lines)}"
    body = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="118" viewBox="0 0 820 118" role="img" aria-label="{e(alt)}">
  <text x="2" y="30" font-family="{MONO}" font-size="13" fill="{c['accent']}">{num}</text>
  <text x="44" y="32" font-family="{SERIF}" font-size="26" fill="{c['fg']}">{e(title)}</text>
  <text x="810" y="30" text-anchor="end" font-family="{MONO}" font-size="11" fill="{c['dim']}">{e(meta)}</text>''']
    for i, ln in enumerate(lines):
        body.append(f'''  <text x="44" y="{64 + i * 22}" font-family="{SERIF}" font-style="italic" font-size="15" fill="{c['muted']}">{e(ln)}</text>''')
    body.append(f'''  <rect x="2" y="114" width="816" height="1" fill="{c['rule']}"/>
</svg>
''')
    return "\n".join(body)

# ---------------------------------------------------------------- stack
STACK = [
    "languages  go · typescript · python · php · c#      frontend  angular · react · next.js · tailwind",
    "backend  go · fastapi · nestjs · laravel · postgresql      devops  docker · github actions · gcp · azure · linux",
]

def stack(theme):
    c = THEMES[theme]
    alt = "Stack — " + "; ".join(STACK)
    body = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="52" viewBox="0 0 820 52" role="img" aria-label="{e(alt)}">''']
    for i, ln in enumerate(STACK):
        body.append(f'''  <text x="2" y="{20 + i * 22}" font-family="{MONO}" font-size="10.5" fill="{c['muted']}" xml:space="preserve">{e(ln)}</text>''')
    body.append("</svg>\n")
    return "\n".join(body)

# ---------------------------------------------------------------- colophon
WORDMARK = [
    "██╗     ███████╗███████╗ ██████╗ ██╗   ██╗███████╗██╗     ",
    "██║     ██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝██║     ",
    "██║     █████╗  ███████╗██║   ██║██║   ██║█████╗  ██║     ",
    "██║     ██╔══╝  ╚════██║██║▄▄ ██║██║   ██║██╔══╝  ██║     ",
    "███████╗███████╗███████║╚██████╔╝╚██████╔╝███████╗███████╗",
    "╚══════╝╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝",
]
TAGLINE = "build it · ship it · run it"

def colophon(theme):
    c = THEMES[theme]
    body = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="460" height="152" viewBox="0 0 460 152" role="img" aria-label="LESQUEL — build it, ship it, run it">
  <g font-family="{MONO}" font-size="12" fill="{c['accent']}">''']
    for i, row in enumerate(WORDMARK):
        body.append(f'''    <text x="18" y="{22 + i * 16}" xml:space="preserve">{e(row)}</text>''')
    body.append(f'''  </g>
  <text x="230" y="138" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{c['muted']}">{e(TAGLINE)}</text>
</svg>
''')
    return "\n".join(body)

for theme in THEMES:
    write(f"header-{theme}.svg", header(theme))
    write(f"stack-{theme}.svg", stack(theme))
    write(f"colophon-{theme}.svg", colophon(theme))
    for num, title, meta, lines in WORKS:
        write(f"works-{num}-{theme}.svg", works(num, title, meta, lines, theme))
