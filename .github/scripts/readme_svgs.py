"""SVG designs used in the profile README. Every function returns SVG text for one theme."""

from xml.sax.saxutils import escape

THEMES = {
    "dark": {
        "bg": "#0D1117",
        "surface": "#161B22",
        "border": "#30363D",
        "text": "#E6EDF3",
        "muted": "#8B949E",
        "accent": "#58A6FF",
        "accent2": "#A371F7",
        "green": "#7EE787",
        "orange": "#FFA657",
        "string": "#A5D6FF",
    },
    "light": {
        "bg": "#FFFFFF",
        "surface": "#F6F8FA",
        "border": "#D0D7DE",
        "text": "#1F2328",
        "muted": "#59636E",
        "accent": "#0969DA",
        "accent2": "#8250DF",
        "green": "#116329",
        "orange": "#953800",
        "string": "#0A3069",
    },
}

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

def text_width(text, size, bold=False):
    # Rough width of sans-serif text, good enough for laying things out
    return len(text) * size * (0.6 if bold else 0.55)


def wrap(text, max_chars, max_lines):
    lines = []
    current = ""

    for word in text.split():
        if len(current) + len(word) + 1 > max_chars and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()

    if current:
        lines.append(current)

    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".,") + "…"

    return lines


def header(theme):
    t = THEMES[theme]
    taglines = ["I love building apps", "Always working on a new project", "Web · Desktop · Mobile"]

    tagline_text = "\n".join(
        f'  <text class="tag tag{i}" x="72" y="222" font-family="{SANS}" font-size="24" fill="{t["muted"]}">{escape(line)}</text>'
        for i, line in enumerate(taglines)
    )

    code = [
        [("const ", t["accent2"]), ("borhan", t["orange"]), (" = {", t["text"])],
        [("  loves", t["text"]), (": ", t["text"]), ('"building apps"', t["string"]), (",", t["text"])],
        [("  stack", t["text"]), (": [", t["text"]), ('"TS"', t["string"]), (", ", t["text"]), ('"Python"', t["string"]), (", ", t["text"]), ('"Java"', t["string"]), ("],", t["text"])],
        [("  basedIn", t["text"]), (": ", t["text"]), ('"San Antonio, TX"', t["string"]), (",", t["text"])],
        [("  shipping", t["text"]), (": ", t["text"]), ("true", t["accent"]), (",", t["text"])],
        [("};", t["text"])],
    ]

    code_text = "\n".join(
        f'    <text x="24" y="{76 + i * 26}" font-family="{MONO}" font-size="15" xml:space="preserve">'
        + "".join(f'<tspan fill="{color}">{escape(part)}</tspan>' for part, color in line)
        + "</text>"
        for i, line in enumerate(code)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-label="Hey, I'm Borhan. Software developer who loves building apps.">
  <style>
    .tag {{ opacity: 0; animation: cycle 9s infinite; }}
    .tag1 {{ animation-delay: 3s; }}
    .tag2 {{ animation-delay: 6s; }}
    @keyframes cycle {{
      0% {{ opacity: 0; }}
      4%, 30% {{ opacity: 1; }}
      34%, 100% {{ opacity: 0; }}
    }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .glow {{ animation: pulse 6s ease-in-out infinite; }}
    @keyframes pulse {{ 50% {{ opacity: 0.55; }} }}
  </style>
  <defs>
    <clipPath id="frame"><rect width="1200" height="320" rx="20"/></clipPath>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0 H0 V40" fill="none" stroke="{t["accent"]}" stroke-opacity="0.08"/>
    </pattern>
    <radialGradient id="glow1"><stop offset="0" stop-color="{t["accent"]}" stop-opacity="0.35"/><stop offset="1" stop-color="{t["accent"]}" stop-opacity="0"/></radialGradient>
    <radialGradient id="glow2"><stop offset="0" stop-color="{t["accent2"]}" stop-opacity="0.3"/><stop offset="1" stop-color="{t["accent2"]}" stop-opacity="0"/></radialGradient>
    <linearGradient id="name" x1="0" x2="1"><stop offset="0" stop-color="{t["text"]}"/><stop offset="1" stop-color="{t["accent"]}"/></linearGradient>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="320" fill="{t["bg"]}"/>
    <rect width="1200" height="320" fill="url(#grid)"/>
    <circle class="glow" cx="930" cy="70" r="340" fill="url(#glow1)"/>
    <circle class="glow" cx="1150" cy="330" r="300" fill="url(#glow2)" style="animation-delay: 3s"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="319" rx="20" fill="none" stroke="{t["border"]}"/>

  <text x="72" y="96" font-family="{MONO}" font-size="15" letter-spacing="3" fill="{t["accent"]}">SOFTWARE DEVELOPER · CS GRAD</text>
  <text x="70" y="168" font-family="{SANS}" font-size="64" font-weight="700" fill="url(#name)">Hey, I'm Borhan</text>
{tagline_text}
  <g transform="translate(72 251) scale(1.3)">
    <clipPath id="flag"><rect width="24" height="16" rx="2.5"/></clipPath>
    <g clip-path="url(#flag)">
      <rect width="24" height="8" fill="#FFFFFF"/>
      <rect y="8" width="24" height="8" fill="#BF0A30"/>
      <rect width="8" height="16" fill="#002868"/>
      <polygon points="4.00,4.80 4.76,6.95 7.04,7.01 5.24,8.40 5.88,10.59 4.00,9.30 2.12,10.59 2.76,8.40 0.96,7.01 3.24,6.95" fill="#FFFFFF"/>
    </g>
    <rect x="0.5" y="0.5" width="23" height="15" rx="2.5" fill="none" stroke="{t["border"]}"/>
  </g>
  <text x="114" y="268" font-family="{SANS}" font-size="16" fill="{t["muted"]}">San Antonio, TX</text>

  <g transform="translate(730 58)">
    <rect width="400" height="204" rx="12" fill="{t["surface"]}" fill-opacity="0.92" stroke="{t["border"]}"/>
    <circle cx="22" cy="22" r="5" fill="#FF5F57"/>
    <circle cx="40" cy="22" r="5" fill="#FEBC2E"/>
    <circle cx="58" cy="22" r="5" fill="#28C840"/>
    <text x="200" y="27" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{t["muted"]}">borhan.ts</text>
    <path d="M0 42 H400" stroke="{t["border"]}"/>
{code_text}
    <rect class="cursor" x="48" y="194" width="9" height="3" fill="{t["accent"]}"/>
  </g>
</svg>
"""


def section_title(number, title, theme):
    t = THEMES[theme]
    line_start = 44 + text_width(title, 22, bold=True) + 20

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 44" width="900" height="44" role="img" aria-label="{escape(title)}">
  <defs>
    <linearGradient id="line" x1="0" x2="1"><stop offset="0" stop-color="{t["accent"]}" stop-opacity="0.8"/><stop offset="1" stop-color="{t["accent2"]}" stop-opacity="0"/></linearGradient>
  </defs>
  <text x="0" y="29" font-family="{MONO}" font-size="14" fill="{t["accent"]}">{number:02d}</text>
  <text x="34" y="30" font-family="{SANS}" font-size="22" font-weight="700" fill="{t["text"]}">{escape(title)}</text>
  <rect x="{line_start:.0f}" y="21" width="{900 - line_start:.0f}" height="1.5" fill="url(#line)"/>
</svg>
"""


def project_card(name, description, tags, is_live, theme):
    t = THEMES[theme]

    description_lines = "\n".join(
        f'  <text x="28" y="{108 + i * 22}" font-family="{SANS}" font-size="15" fill="{t["muted"]}">{escape(line)}</text>'
        for i, line in enumerate(wrap(description, 52, 3))
    )

    # Tech pills along the bottom, as many as fit
    pills = []
    x = 28
    for tag in tags:
        width = len(tag) * 7.6 + 22
        if x + width > 440 - 28:
            break
        pills.append(
            f'  <rect x="{x:.0f}" y="186" width="{width:.0f}" height="26" rx="13" fill="{t["bg"]}" stroke="{t["border"]}"/>\n'
            f'  <text x="{x + width / 2:.0f}" y="203.5" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{t["text"]}">{escape(tag)}</text>'
        )
        x += width + 8

    live_badge = ""
    if is_live:
        live_badge = f"""  <rect x="352" y="30" width="60" height="26" rx="13" fill="{t["green"]}" fill-opacity="0.12" stroke="{t["green"]}" stroke-opacity="0.5"/>
  <circle cx="368" cy="43" r="3.5" fill="{t["green"]}"/>
  <text x="392" y="47.5" text-anchor="middle" font-family="{SANS}" font-size="12" font-weight="600" fill="{t["green"]}">Live</text>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 240" width="440" height="240" role="img" aria-label="{escape(name)}: {escape(description)}">
  <defs>
    <linearGradient id="mark" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["accent"]}"/><stop offset="1" stop-color="{t["accent2"]}"/></linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="439" height="239" rx="16" fill="{t["surface"]}" stroke="{t["border"]}"/>
  <rect x="28" y="24" width="38" height="38" rx="10" fill="url(#mark)"/>
  <text x="47" y="50" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="700" fill="#FFFFFF">{escape(name[:1])}</text>
  <text x="80" y="50" font-family="{SANS}" font-size="21" font-weight="700" fill="{t["text"]}">{escape(name)}</text>
{live_badge}
{description_lines}
{chr(10).join(pills)}
</svg>
"""
