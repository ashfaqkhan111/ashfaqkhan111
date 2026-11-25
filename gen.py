#!/usr/bin/env python3
"""Generates the animated SVG cards used by README.md."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"

LANG_COLORS = {
    "Java": "#f89820", "CSS": "#a259ff", "PHP": "#8892bf",
    "Shell": "#89e051", "HTML": "#e34c26", "C": "#5c9dff",
}

# Shared backdrop: dark glass panel, drifting aurora blobs, animated gradient border
def backdrop(w, h, uid):
    return f"""
  <defs>
    <linearGradient id="bg{uid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#070b14"/>
    </linearGradient>
    <linearGradient id="bd{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#38bdf8"><animate attributeName="stop-color" values="#38bdf8;#a78bfa;#34d399;#38bdf8" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset="1" stop-color="#a78bfa"><animate attributeName="stop-color" values="#a78bfa;#34d399;#38bdf8;#a78bfa" dur="8s" repeatCount="indefinite"/></stop>
    </linearGradient>
    <filter id="blur{uid}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>
    <clipPath id="clip{uid}"><rect width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#clip{uid})">
    <rect width="{w}" height="{h}" fill="url(#bg{uid})"/>
    <g filter="url(#blur{uid})" opacity=".55">
      <circle cx="{w*0.15:.0f}" cy="{h*0.2:.0f}" r="{min(w,h)*0.35:.0f}" fill="#1d4ed8">
        <animate attributeName="cx" values="{w*0.15:.0f};{w*0.35:.0f};{w*0.15:.0f}" dur="14s" repeatCount="indefinite"/>
      </circle>
      <circle cx="{w*0.85:.0f}" cy="{h*0.85:.0f}" r="{min(w,h)*0.32:.0f}" fill="#7c3aed">
        <animate attributeName="cx" values="{w*0.85:.0f};{w*0.6:.0f};{w*0.85:.0f}" dur="17s" repeatCount="indefinite"/>
      </circle>
      <circle cx="{w*0.55:.0f}" cy="{h*0.1:.0f}" r="{min(w,h)*0.22:.0f}" fill="#059669" opacity=".7">
        <animate attributeName="cy" values="{h*0.1:.0f};{h*0.6:.0f};{h*0.1:.0f}" dur="12s" repeatCount="indefinite"/>
      </circle>
    </g>
  </g>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="17" fill="none" stroke="url(#bd{uid})" stroke-width="1.5" stroke-opacity=".85"/>"""


def header():
    w, h = 900, 270
    chips = ["Java", "CSS", "PHP", "HTML", "Shell"]
    chip_svg, x = "", 210
    for i, c in enumerate(chips):
        cw = 30 + len(c) * 8
        chip_svg += f"""
    <g class="chip" style="animation-delay:{0.9 + i*0.15:.2f}s">
      <rect x="{x}" y="186" width="{cw}" height="28" rx="14" fill="#0f172a" stroke="{LANG_COLORS[c]}" stroke-opacity=".7"/>
      <circle cx="{x+12}" cy="200" r="4" fill="{LANG_COLORS[c]}"/>
      <text x="{x+21}" y="205" font-family="{MONO}" font-size="12.5" fill="#e2e8f0">{c}</text>
    </g>"""
        x += cw + 22
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>
    .fade {{ opacity:0; animation: up .8s ease-out forwards; }}
    .chip {{ opacity:0; animation: up .6s ease-out forwards; }}
    @keyframes up {{ from {{ opacity:0; transform: translateY(10px); }} to {{ opacity:1; transform: translateY(0); }} }}
    .spin {{ transform-origin: 110px 135px; animation: spin 10s linear infinite; }}
    .spin2 {{ transform-origin: 110px 135px; animation: spin 16s linear infinite reverse; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    .caret {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity:0; }} }}
    .type {{ clip-path: inset(0 100% 0 0); animation: type 2.4s steps(30) .4s forwards; }}
    @keyframes type {{ to {{ clip-path: inset(0 0 0 0); }} }}
    .pulse {{ animation: pulse 2.4s ease-in-out infinite; transform-origin: 790px 112px; }}
    @keyframes pulse {{ 0%,100% {{ opacity:.35; transform: scale(1); }} 50% {{ opacity:.9; transform: scale(1.12); }} }}
  </style>{backdrop(w, h, "h")}
  <!-- monogram -->
  <circle class="spin" cx="110" cy="135" r="62" fill="none" stroke="url(#bdh)" stroke-width="2.5" stroke-dasharray="120 40 30 40"/>
  <circle class="spin2" cx="110" cy="135" r="72" fill="none" stroke="#38bdf8" stroke-opacity=".35" stroke-width="1" stroke-dasharray="4 8"/>
  <circle cx="110" cy="135" r="52" fill="#0f172a" stroke="#1e293b"/>
  <text x="110" y="149" text-anchor="middle" font-family="{FONT}" font-weight="800" font-size="38" fill="url(#bdh)">AK</text>
  <!-- identity -->
  <g class="type"><text x="210" y="74" font-family="{MONO}" font-size="15" fill="#94a3b8">@ashfaqkhan111</text></g>
  <rect class="caret" x="342" y="61" width="8" height="16" fill="#38bdf8"/>
  <g class="fade" style="animation-delay:.3s"><text x="208" y="128" font-family="{FONT}" font-weight="800" font-size="46" fill="#f8fafc">Ashfaq Khan</text></g>
  <g class="fade" style="animation-delay:.6s"><text x="210" y="160" font-family="{FONT}" font-size="16" fill="#cbd5e1">Building with <tspan fill="#f89820" font-weight="700">Java</tspan> · crafting the web · exploring Linux</text></g>
  {chip_svg}
  <!-- right badge -->
  <g class="fade" style="animation-delay:1s">
    <circle class="pulse" cx="790" cy="112" r="46" fill="none" stroke="#38bdf8" stroke-width="1.2"/>
    <circle cx="790" cy="112" r="36" fill="#0f172a" stroke="#1e293b"/>
    <text x="790" y="121" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#38bdf8">&lt;/&gt;</text>
    <text x="790" y="186" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="2" fill="#94a3b8">OPEN TO COLLAB</text>
    <circle cx="712" cy="182" r="4" fill="#34d399"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
  </g>
  <text x="{w-20}" y="{h-14}" text-anchor="end" font-family="{MONO}" font-size="10" fill="#475569">github.com/ashfaqkhan111</text>
</svg>"""
    open(os.path.join(OUT, "header.svg"), "w").write(svg)


def terminal():
    w, h = 900, 300
    lines = [
        ("$", "whoami", "#e2e8f0"),
        ("", "ashfaq khan — developer &amp; student", "#94a3b8"),
        ("$", "cat stack.txt", "#e2e8f0"),
        ("", "languages : Java · PHP · JavaScript · Shell", "#f89820"),
        ("", "frontend  : HTML · CSS · responsive UI", "#a78bfa"),
        ("", "tools     : Git · Linux · VS Code · IntelliJ", "#34d399"),
        ("$", "echo $CURRENT_FOCUS", "#e2e8f0"),
        ("", "data structures, simulations &amp; full-stack web", "#38bdf8"),
    ]
    body, t = "", 0.4
    for i, (p, txt, col) in enumerate(lines):
        y = 82 + i * 26
        n = max(len(txt.replace("&amp;", "&")), 6)
        dur = 0.9 if p else 0.35
        prompt = f'<tspan fill="#34d399">❯ </tspan>' if p else '<tspan fill="#475569">  </tspan>'
        body += f"""
  <clipPath id="ln{i}"><rect x="30" y="{y-18}" height="26" width="0">
    <animate attributeName="width" from="0" to="{30 + n*9.2:.0f}" dur="{dur}s" begin="{t:.2f}s" fill="freeze" calcMode="discrete" values="{';'.join(str(round(k*(30+n*9.2)/n)) for k in range(n+1))}"/>
  </rect></clipPath>
  <g clip-path="url(#ln{i})">
    <text xml:space="preserve" x="34" y="{y}" font-family="{MONO}" font-size="15" fill="{col}">{prompt}{txt}</text>
  </g>"""
        t += dur + (0.25 if p else 0.15)
    cy = 82 + len(lines) * 26
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>
    @keyframes type {{ to {{ clip-path: inset(0 0 0 0); }} }}
    .caret {{ opacity:0; animation: show 0s {t:.2f}s forwards, blink 1s steps(1) {t:.2f}s infinite; }}
    @keyframes show {{ to {{ opacity:1; }} }}
    @keyframes blink {{ 50% {{ opacity:0; }} }}
  </style>{backdrop(w, h, "t")}
  <rect x="1" y="1" width="{w-2}" height="40" rx="17" fill="#0f172a" opacity=".85"/>
  <rect x="1" y="24" width="{w-2}" height="17" fill="#0f172a" opacity=".85"/>
  <circle cx="26" cy="21" r="6" fill="#ff5f57"/><circle cx="46" cy="21" r="6" fill="#febc2e"/><circle cx="66" cy="21" r="6" fill="#28c840"/>
  <text x="{w/2:.0f}" y="26" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#64748b">ashfaq@github: ~/profile — zsh</text>
  {body}
  <text class="caret" x="34" y="{cy}" font-family="{MONO}" font-size="15" fill="#34d399" style="animation: show 0s {t:.2f}s forwards">❯ </text>
  <rect class="caret" x="52" y="{cy-13}" width="9" height="17" fill="#38bdf8"/>
</svg>"""
    open(os.path.join(OUT, "terminal.svg"), "w").write(svg)


PROJECTS = [
    # slug, title, owner/repo, lang, description, stars, forks
    ("tracevault", "TraceVault", "ashfaqkhan111/TraceVault", "CSS", "Front-end web project", 1, 0),
    ("portfolio", "khan-dev-portfolio", "ashfaqkhan111/khan-dev-portfolio", "Java", "Personal developer portfolio", 0, 0),
    ("simulation", "simulation", "ashfaqkhan111/simulation", "Java", "Java simulation project", 0, 0),
    ("barbershop", "barbershop", "MuhammadRayyan01/barbershop", "PHP", "Barbershop website design (collab)", 1, 2),
    ("linux", "linux-projects", "ashfaqkhan111/linux-projects", "Shell", "Shell scripts &amp; Linux experiments", 0, 0),
    ("datastructure", "DataStructure", "ashfaqkhan111/DataStructure", "Java", "Data structures implemented in Java", 0, 0),
]


def project_card(i, slug, title, repo, lang, desc, stars, forks):
    w, h = 440, 170
    col = LANG_COLORS[lang]
    circ = 2 * 3.14159 * 30
    delay = 0.15 * i
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <style>
    .in {{ opacity:0; animation: up .7s ease-out {delay:.2f}s forwards; }}
    @keyframes up {{ from {{ opacity:0; transform: translateY(8px); }} to {{ opacity:1; transform: none; }} }}
    .ring {{ stroke-dasharray: {circ:.1f}; stroke-dashoffset: {circ:.1f}; animation: draw 1.6s ease-out {delay+0.4:.2f}s forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    .orbit {{ transform-origin: 370px 92px; animation: spin 6s linear infinite; }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    .caret {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity:0; }} }}
  </style>{backdrop(w, h, slug)}
  <g class="in">
    <text x="20" y="30" font-family="{MONO}" font-size="11" fill="#64748b">▸ {repo.split('/')[0]} /</text>
    <circle cx="{w-22}" cy="26" r="4" fill="#34d399"><animate attributeName="opacity" values="1;.25;1" dur="2s" begin="{delay:.2f}s" repeatCount="indefinite"/></circle>
    <line x1="20" y1="42" x2="{w-20}" y2="42" stroke="#1e293b"/>
    <text x="20" y="72" font-family="{MONO}" font-weight="700" font-size="19" fill="#f1f5f9">{title}</text>
    <rect class="caret" x="{24 + len(title)*11.6:.0f}" y="58" width="9" height="17" fill="{col}"/>
    <text x="20" y="98" font-family="{FONT}" font-size="13" fill="#94a3b8">{desc}</text>
    <rect x="20" y="118" width="{20 + len(lang)*8}" height="22" rx="11" fill="#0f172a" stroke="{col}" stroke-opacity=".7"/>
    <text x="{30}" y="133" font-family="{MONO}" font-size="11" fill="#e2e8f0">{lang}</text>
    <text x="{58 + len(lang)*8}" y="133" font-family="{MONO}" font-size="12" fill="#fbbf24">★ <tspan fill="#cbd5e1">{stars}</tspan></text>
    <text x="{100 + len(lang)*8}" y="133" font-family="{MONO}" font-size="12" fill="#94a3b8">⑂ <tspan fill="#cbd5e1">{forks}</tspan></text>
  </g>
  <circle cx="370" cy="92" r="30" fill="none" stroke="#1e293b" stroke-width="7"/>
  <circle class="ring" cx="370" cy="92" r="30" fill="none" stroke="{col}" stroke-width="7" stroke-linecap="round" transform="rotate(-90 370 92)"/>
  <g class="orbit"><circle cx="370" cy="52" r="3" fill="#38bdf8"/></g>
  <text x="370" y="97" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" fill="{col}">{lang}</text>
</svg>"""
    open(os.path.join(OUT, f"project-{slug}.svg"), "w").write(svg)


def divider(name, label):
    w, h = 900, 46
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#38bdf8" stop-opacity="0"/><stop offset=".5" stop-color="#38bdf8"/><stop offset="1" stop-color="#a78bfa" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .scan {{ animation: scan 3.5s ease-in-out infinite; }}
    @keyframes scan {{ 0% {{ transform: translateX(-300px); }} 100% {{ transform: translateX(900px); }} }}
  </style>
  <line x1="0" y1="30" x2="{w}" y2="30" stroke="#1e293b"/>
  <rect class="scan" x="0" y="29" width="300" height="2" fill="url(#g)"/>
  <rect x="0" y="12" width="{40 + len(label)*10}" height="26" rx="6" fill="#0b1220" stroke="#1e293b"/>
  <text x="14" y="30" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="1.5" fill="#38bdf8">{label}<tspan fill="#64748b"> _</tspan></text>
</svg>"""
    open(os.path.join(OUT, f"divider-{name}.svg"), "w").write(svg)


def footer():
    w, h = 900, 120
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="fw" x1="0" x2="1">
      <stop offset="0" stop-color="#1d4ed8"/><stop offset=".5" stop-color="#7c3aed"/><stop offset="1" stop-color="#059669"/>
    </linearGradient>
  </defs>
  <path fill="url(#fw)" opacity=".35">
    <animate attributeName="d" dur="9s" repeatCount="indefinite" values="
      M0 60 Q225 20 450 60 T900 60 V120 H0Z;
      M0 60 Q225 100 450 60 T900 60 V120 H0Z;
      M0 60 Q225 20 450 60 T900 60 V120 H0Z"/>
  </path>
  <path fill="url(#fw)" opacity=".6">
    <animate attributeName="d" dur="7s" repeatCount="indefinite" values="
      M0 80 Q225 110 450 80 T900 80 V120 H0Z;
      M0 80 Q225 50 450 80 T900 80 V120 H0Z;
      M0 80 Q225 110 450 80 T900 80 V120 H0Z"/>
  </path>
  <text x="450" y="34" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#94a3b8">thanks for stopping by — keep building <tspan fill="#38bdf8">⚡</tspan></text>
</svg>"""
    open(os.path.join(OUT, "footer.svg"), "w").write(svg)


if __name__ == "__main__":
    header()
    terminal()
    for i, p in enumerate(PROJECTS):
        project_card(i, *p)
    divider("projects", "PROJECTS.LIST")
    divider("stats", "PROFILE.SIGNAL")
    divider("activity", "CONTRIBUTION.ACTIVITY")
    footer()
    print("\n".join(sorted(os.listdir(OUT))))
