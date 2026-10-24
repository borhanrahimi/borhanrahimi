"""SVG designs used in the profile README. Every function returns SVG text for one theme."""

import random
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


# How I Met Your Mother style header: a rainy night with the yellow umbrella (dark)
# and a sunny day with the blue French horn (light)
HEADER_SCENES = {
    "dark": {
        "sky_top": "#0B1026",
        "sky_bottom": "#2A2350",
        "moon": "#F4F1DE",
        "building": "#060914",
        "building_far": "#141A35",
        "window": "#FFD86B",
        "rain": "#9DB4FF",
        "title": "#FFFFFF",
        "narration": "#C9D1E8",
        "tagline": "#FFD21F",
        "label": "#9DB4FF",
    },
    "light": {
        "sky_top": "#6FB7EE",
        "sky_bottom": "#E4F3FF",
        "sun": "#FFD54A",
        "building": "#34466B",
        "building_far": "#A3B8D8",
        "window": "#EAF3FF",
        "title": "#14213D",
        "narration": "#33415C",
        "tagline": "#1F5FBF",
        "label": "#2F4B7C",
    },
}


def header(theme):
    t = THEMES[theme]
    s = HEADER_SCENES[theme]
    rng = random.Random(7)  # same "random" scene on every run, so the file only changes when the design does

    taglines = [
        "I love building apps",
        "Always working on a new project",
        "It's going to be legen… wait for it… dary!",
    ]

    tagline_text = "\n".join(
        f'  <text class="tag tag{i}" x="72" y="236" font-family="{SANS}" font-size="20" font-weight="600" fill="{s["tagline"]}">{escape(line)}</text>'
        for i, line in enumerate(taglines)
    )

    # Skyline: low on the left so it stays behind the text, taller on the right
    far_buildings = []
    near_buildings = []
    windows = []

    x = 0
    while x < 1200:
        width = rng.randint(30, 60)
        height = rng.randint(50, 110) if x > 640 else rng.randint(20, 45)
        far_buildings.append(f'    <rect x="{x}" y="{300 - height}" width="{width}" height="{height + 20}" fill="{s["building_far"]}"/>')
        x += width + rng.randint(0, 6)

    x = -10
    while x < 1200:
        width = rng.randint(36, 74)
        height = rng.randint(40, 95) if x > 660 else rng.randint(10, 32)
        top = 320 - height
        near_buildings.append(f'    <rect x="{x}" y="{top}" width="{width}" height="{height}" fill="{s["building"]}"/>')

        for wy in range(top + 10, 312, 14):
            for wx in range(x + 7, x + width - 8, 11):
                if rng.random() < 0.22:
                    twinkle = ' class="twinkle"' if rng.random() < 0.25 else ""
                    delay = f' style="animation-delay: {rng.uniform(0, 6):.1f}s"' if twinkle else ""
                    windows.append(f'    <rect{twinkle}{delay} x="{wx}" y="{wy}" width="5" height="6" fill="{s["window"]}" opacity="0.85"/>')
        x += width + rng.randint(2, 10)

    # Empire State style spire
    spire = f"""    <path d="M1118 320 V214 H1128 V196 H1136 V170 H1140 V140 H1142 V170 H1146 V196 H1154 V214 H1164 V320 Z" fill="{s["building"]}"/>"""

    if theme == "dark":
        glow_color = s["moon"]
        sky = f"""    <circle cx="790" cy="70" r="90" fill="url(#glow)"/>
    <circle cx="790" cy="70" r="26" fill="{s["moon"]}"/>
    <circle cx="780" cy="62" r="5" fill="{s["sky_top"]}" opacity="0.12"/>
    <circle cx="798" cy="80" r="3.5" fill="{s["sky_top"]}" opacity="0.12"/>"""

        rain = "\n".join(
            f'    <line class="drop" x1="{dx}" y1="{dy}" x2="{dx - 4}" y2="{dy + 16}" stroke="{s["rain"]}" stroke-opacity="{rng.uniform(0.25, 0.6):.2f}" stroke-width="1.4" style="animation-delay: -{rng.uniform(0, 1.4):.2f}s; animation-duration: {rng.uniform(0.9, 1.4):.2f}s"/>'
            for dx, dy in ((rng.randint(0, 1220), rng.randint(-340, 300)) for _ in range(110))
        )

        # No rain under the umbrella
        weather = f"""  <mask id="dry">
    <rect width="1200" height="320" fill="#FFFFFF"/>
    <path d="M906 150 Q1000 140 1094 150 L1110 320 L890 320 Z" fill="#000000"/>
  </mask>
  <g mask="url(#dry)">
{rain}
  </g>"""

        # The yellow umbrella
        prop = """  <g class="sway">
    <path d="M1000 150 V250 A12 12 0 0 1 976 250" fill="none" stroke="#3B2A1A" stroke-width="5" stroke-linecap="round"/>
    <path d="M906 150 A94 94 0 0 1 1094 150 Q1070.5 134 1047 150 Q1023.5 134 1000 150 Q976.5 134 953 150 Q929.5 134 906 150 Z" fill="url(#canopy)"/>
    <path d="M1000 56 Q972 90 953 150 M1000 56 Q1028 90 1047 150" fill="none" stroke="#D99A00" stroke-width="2"/>
    <path d="M1000 56 Q960 76 930 120" fill="none" stroke="#FFF3A8" stroke-width="3" stroke-opacity="0.6" stroke-linecap="round"/>
    <line x1="1000" y1="56" x2="1000" y2="42" stroke="#3B2A1A" stroke-width="4" stroke-linecap="round"/>
  </g>"""
    else:
        glow_color = s["sun"]
        sky = f"""    <circle cx="790" cy="66" r="110" fill="url(#glow)"/>
    <circle cx="790" cy="66" r="30" fill="{s["sun"]}"/>"""

        clouds = []
        for cx, cy, size, speed in [(120, 52, 1.0, 60), (520, 34, 0.8, 75), (700, 120, 0.7, 90), (1080, 40, 0.9, 70)]:
            clouds.append(
                f'    <g class="cloud" style="animation-duration: {speed}s" opacity="0.9">'
                f'<g transform="translate({cx} {cy}) scale({size})">'
                '<ellipse cx="0" cy="12" rx="46" ry="14" fill="#FFFFFF"/>'
                '<circle cx="-16" cy="4" r="16" fill="#FFFFFF"/>'
                '<circle cx="10" cy="-2" r="21" fill="#FFFFFF"/>'
                '<circle cx="30" cy="8" r="13" fill="#FFFFFF"/>'
                "</g></g>"
            )
        weather = "  <g>\n" + "\n".join(clouds) + "\n  </g>"

        # The blue French horn
        prop = """  <g class="sway">
    <circle cx="990" cy="168" r="62" fill="none" stroke="#1E4FB8" stroke-width="13"/>
    <circle cx="990" cy="168" r="62" fill="none" stroke="#3C7BF0" stroke-width="7"/>
    <circle cx="982" cy="176" r="36" fill="none" stroke="#1E4FB8" stroke-width="10"/>
    <circle cx="982" cy="176" r="36" fill="none" stroke="#5B93F5" stroke-width="5"/>
    <path d="M1048 188 C1070 194 1092 192 1108 186 L1118 266 C1094 248 1068 226 1048 214 Z" fill="#2D6CDF"/>
    <path d="M1052 193 C1072 199 1090 198 1104 193" fill="none" stroke="#A8C6FA" stroke-width="2" stroke-opacity="0.7"/>
    <ellipse cx="1113" cy="226" rx="12" ry="41" transform="rotate(-7 1113 226)" fill="#1E4FB8"/>
    <ellipse cx="1113" cy="226" rx="7" ry="34" transform="rotate(-7 1113 226)" fill="#0F2F75"/>
    <rect x="955" y="118" width="8" height="16" rx="2" fill="#C9D3E3"/>
    <rect x="970" y="113" width="8" height="16" rx="2" fill="#C9D3E3"/>
    <rect x="985" y="110" width="8" height="16" rx="2" fill="#C9D3E3"/>
    <ellipse cx="959" cy="118" rx="7" ry="3.5" fill="#E6ECF5"/>
    <ellipse cx="974" cy="113" rx="7" ry="3.5" fill="#E6ECF5"/>
    <ellipse cx="989" cy="110" rx="7" ry="3.5" fill="#E6ECF5"/>
    <path d="M944 214 L912 246" stroke="#3C7BF0" stroke-width="6" stroke-linecap="round"/>
    <circle cx="909" cy="249" r="6" fill="#C9D3E3"/>
    <path d="M948 128 C936 150 938 190 960 206" fill="none" stroke="#A8C6FA" stroke-width="2.5" stroke-opacity="0.7" stroke-linecap="round"/>
  </g>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-label="hey, i'm borhan. Kids, let me tell you about the apps I built.">
  <style>
    .tag {{ opacity: 0; animation: cycle 12s infinite; }}
    .tag1 {{ animation-delay: 4s; }}
    .tag2 {{ animation-delay: 8s; }}
    @keyframes cycle {{
      0% {{ opacity: 0; }}
      3%, 30% {{ opacity: 1; }}
      33%, 100% {{ opacity: 0; }}
    }}
    .drop {{ animation: fall 1.2s linear infinite; }}
    @keyframes fall {{ to {{ transform: translate(-20px, 340px); }} }}
    .sway {{ transform-box: view-box; transform-origin: 1000px 262px; animation: sway 5s ease-in-out infinite; }}
    @keyframes sway {{ 0%, 100% {{ transform: rotate(-4deg); }} 50% {{ transform: rotate(4deg); }} }}
    .twinkle {{ animation: twinkle 4s ease-in-out infinite; }}
    @keyframes twinkle {{ 50% {{ opacity: 0.15; }} }}
    .cloud {{ animation: drift 60s linear infinite alternate; }}
    @keyframes drift {{ to {{ transform: translateX(80px); }} }}
  </style>
  <defs>
    <clipPath id="frame"><rect width="1200" height="320" rx="20"/></clipPath>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s["sky_top"]}"/><stop offset="1" stop-color="{s["sky_bottom"]}"/></linearGradient>
    <radialGradient id="glow"><stop offset="0" stop-color="{glow_color}" stop-opacity="0.45"/><stop offset="1" stop-color="{glow_color}" stop-opacity="0"/></radialGradient>
    <linearGradient id="canopy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE14D"/><stop offset="1" stop-color="#F5B800"/></linearGradient>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="320" fill="url(#sky)"/>
{sky}
  <g>
{chr(10).join(far_buildings)}
  </g>
  <g>
{chr(10).join(near_buildings)}
{spire}
{chr(10).join(windows)}
  </g>
{weather}

{prop}
  </g>
  <rect x="0.5" y="0.5" width="1199" height="319" rx="20" fill="none" stroke="{t["border"]}"/>

  <text x="72" y="84" font-family="{MONO}" font-size="14" letter-spacing="3" fill="{s["label"]}">SOFTWARE DEVELOPER · CS GRAD</text>
  <text x="68" y="152" font-family="{SANS}" font-size="66" font-weight="800" letter-spacing="-1.5" fill="{s["title"]}">hey, i'm borhan</text>
  <text x="72" y="194" font-family="Georgia, 'Times New Roman', serif" font-size="21" font-style="italic" fill="{s["narration"]}">Kids, let me tell you about the apps I built…</text>
{tagline_text}
  <g transform="translate(72 253) scale(1.3)">
    <clipPath id="flag"><rect width="24" height="16" rx="2.5"/></clipPath>
    <g clip-path="url(#flag)">
      <rect width="24" height="8" fill="#FFFFFF"/>
      <rect y="8" width="24" height="8" fill="#BF0A30"/>
      <rect width="8" height="16" fill="#002868"/>
      <polygon points="4.00,4.80 4.76,6.95 7.04,7.01 5.24,8.40 5.88,10.59 4.00,9.30 2.12,10.59 2.76,8.40 0.96,7.01 3.24,6.95" fill="#FFFFFF"/>
    </g>
  </g>
  <text x="114" y="270" font-family="{SANS}" font-size="16" font-weight="600" fill="{s["narration"]}">San Antonio, TX</text>
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
