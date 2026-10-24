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


# The gang from How I Met Your Mother, drawn as simple busts in a 100 x 130 box
GANG = [
    {
        # Barney: blond side part, suit with pocket square, red tie, smirk and a raised eyebrow
        "skin": "#F3CFB3",
        "shade": "#D9A988",
        "eyes": "#3B6EA8",
        "hair_back": "",
        "hair": '<path d="M26 52 C24 30 36 22 52 22 C68 22 78 30 74 52 C72 42 66 36 58 34 C50 40 36 38 30 44 Z" fill="#E3C16F"/>'
                '<path d="M34 34 C42 28 54 27 62 30 M58 34 C64 34 70 38 72 44" fill="none" stroke="#C9A24C" stroke-width="1.6" stroke-linecap="round"/>'
                '<path d="M40 30 C48 26 56 26 62 28" fill="none" stroke="#F5DC98" stroke-width="2" stroke-linecap="round"/>',
        "body": '<path d="M5 130 C8 100 26 92 50 92 C74 92 92 100 95 130 Z" fill="#1C1F2B"/>'
                '<path d="M38 92 L50 116 L62 92 Z" fill="#FFFFFF"/>'
                '<path d="M47 98 H53 L55 118 L50 125 L45 118 Z" fill="#7A1F33"/>'
                '<path d="M46 93 H54 L53 99 H47 Z" fill="#5E1627"/>'
                '<path d="M48 104 L52 108 M47 112 L53 117" stroke="#9B2C45" stroke-width="1.4"/>'
                '<path d="M38 92 L50 116 M62 92 L50 116" stroke="#2C3142" stroke-width="3"/>'
                '<path d="M30 98 L42 118 M70 98 L58 118" stroke="#2C3142" stroke-width="2"/>'
                '<path d="M66 108 L76 106 L74 112 Z" fill="#FFFFFF"/>'
                '<circle cx="50" cy="128" r="1.6" fill="#3A3F52"/>',
        "brows": '<path d="M37 48 Q42 45 47 48" fill="none" stroke="#B8963E" stroke-width="2.4" stroke-linecap="round"/>'
                 '<path d="M53 45 Q58 40 63 44" fill="none" stroke="#B8963E" stroke-width="2.4" stroke-linecap="round"/>',
        "mouth": '<path d="M43 71 Q52 76 60 67" fill="none" stroke="#8A4B3A" stroke-width="2.6" stroke-linecap="round"/>'
                 '<path d="M59 66 L61 69" stroke="#8A4B3A" stroke-width="1.6" stroke-linecap="round"/>',
        "lashes": False,
        "extras": "",
    },
    {
        # Robin: long dark hair with highlights, beige blazer, earrings
        "skin": "#F1CBB0",
        "shade": "#D6A68A",
        "eyes": "#5A3A22",
        "hair_back": '<path d="M22 60 C18 26 36 18 52 18 C70 18 84 30 80 62 C82 86 78 100 72 106 L28 106 C22 96 20 80 22 60 Z" fill="#3B2519"/>'
                     '<path d="M25 70 C24 84 27 96 31 104 M76 70 C78 84 75 96 71 104" fill="none" stroke="#5A3A26" stroke-width="2" stroke-linecap="round"/>',
        "hair": '<path d="M26 54 C28 30 46 24 60 26 C72 28 78 40 75 54 C68 40 54 34 42 38 C34 41 29 47 26 54 Z" fill="#3B2519"/>'
                '<path d="M36 32 C44 27 56 27 64 31" fill="none" stroke="#6E4A31" stroke-width="2" stroke-linecap="round"/>',
        "body": '<path d="M5 130 C8 100 26 92 50 92 C74 92 92 100 95 130 Z" fill="#D9C7A4"/>'
                '<path d="M38 93 Q50 110 62 93 Z" fill="#F4EBDD"/>'
                '<path d="M36 94 L46 126 M64 94 L54 126" stroke="#BFAA84" stroke-width="3"/>'
                '<circle cx="50" cy="124" r="1.8" fill="#A8926B"/>',
        "brows": '<path d="M37 49 Q42 46 47 48 M53 48 Q58 46 63 49" fill="none" stroke="#3B2519" stroke-width="2.2" stroke-linecap="round"/>',
        "mouth": '<path d="M42 69 Q50 77 58 69 Q50 72 42 69 Z" fill="#C2525A"/>'
                 '<path d="M42 69 Q50 77 58 69" fill="none" stroke="#A33C45" stroke-width="2" stroke-linecap="round"/>',
        "lashes": True,
        "extras": '<circle cx="26" cy="65" r="2" fill="#E8C35A"/><circle cx="74" cy="65" r="2" fill="#E8C35A"/>',
    },
    {
        # Ted: dark spiky hair, brown jacket, big happy grin
        "skin": "#EEC6A6",
        "shade": "#D29E7E",
        "eyes": "#4A2F1C",
        "hair_back": "",
        "hair": '<path d="M26 50 C22 30 32 20 44 18 L46 10 L53 17 L59 9 L62 18 L70 14 L69 23 C78 28 80 40 74 52 C70 40 62 34 50 35 C40 35 31 40 26 50 Z" fill="#2F1E14"/>'
                '<path d="M36 30 L42 22 M50 28 L54 18 M60 28 L64 20 M68 34 L72 28" fill="none" stroke="#4E3524" stroke-width="1.8" stroke-linecap="round"/>',
        "body": '<path d="M5 130 C8 100 26 92 50 92 C74 92 92 100 95 130 Z" fill="#4A3527"/>'
                '<path d="M39 92 L50 112 L61 92 Z" fill="#2A2A33"/>'
                '<path d="M32 95 L44 118 L36 120 Z M68 95 L56 118 L64 120 Z" fill="#5E4635"/>'
                '<path d="M39 92 L50 112 M61 92 L50 112" stroke="#6B5140" stroke-width="2.4"/>',
        "brows": '<path d="M36 46 Q42 42 47 45 M53 45 Q58 42 64 46" fill="none" stroke="#2F1E14" stroke-width="2.6" stroke-linecap="round"/>',
        "mouth": '<path d="M40 68 Q50 81 60 68 Z" fill="#FFFFFF" stroke="#8A4B3A" stroke-width="2" stroke-linejoin="round"/>'
                 '<path d="M41 69 H59" stroke="#E5D6CC" stroke-width="1"/>',
        "lashes": False,
        "extras": '<path d="M38 63 Q36 66 37 68 M62 63 Q64 66 63 68" fill="none" stroke="#D29E7E" stroke-width="1.2" stroke-linecap="round"/>',
    },
    {
        # Marshall: light brown hair, broad face with a chin dimple, grey jacket over a white tee
        "skin": "#F2CDB2",
        "shade": "#D8A98C",
        "eyes": "#5E6B3A",
        "hair_back": "",
        "hair": '<path d="M25 52 C22 30 36 21 52 21 C68 21 80 30 76 52 C72 39 62 33 50 33 C39 33 30 39 25 52 Z" fill="#8A5A35"/>'
                '<path d="M34 30 C42 25 56 24 66 28 M30 40 C36 34 44 31 52 31" fill="none" stroke="#A8744A" stroke-width="1.8" stroke-linecap="round"/>',
        "body": '<path d="M1 130 C4 96 26 89 50 89 C74 89 96 96 99 130 Z" fill="#4B5563"/>'
                '<path d="M36 91 Q50 104 64 91 L60 130 H40 Z" fill="#E9EDF2"/>'
                '<path d="M36 91 L42 130 M64 91 L58 130" stroke="#3A424F" stroke-width="3"/>'
                '<path d="M28 96 L40 116 L33 118 Z M72 96 L60 116 L67 118 Z" fill="#5A6475"/>',
        "brows": '<path d="M36 48 Q42 45 47 47 M53 47 Q58 45 64 48" fill="none" stroke="#7A4E2E" stroke-width="2.8" stroke-linecap="round"/>',
        "mouth": '<path d="M41 69 Q50 78 59 69" fill="none" stroke="#8A4B3A" stroke-width="2.8" stroke-linecap="round"/>'
                 '<path d="M50 79 V81" stroke="#D8A98C" stroke-width="1.4" stroke-linecap="round"/>',
        "lashes": False,
        "extras": "",
    },
    {
        # Lily: auburn hair with side-swept bangs, teal top, necklace, grin
        "skin": "#F5D3BC",
        "shade": "#DDAE93",
        "eyes": "#4E7A3A",
        "hair_back": '<path d="M23 60 C20 28 36 20 52 20 C70 20 82 30 79 60 C80 78 76 90 70 96 L30 96 C24 88 22 76 23 60 Z" fill="#B5472A"/>'
                     '<path d="M26 72 C26 82 28 90 32 95 M75 72 C76 82 73 90 69 95" fill="none" stroke="#D0623F" stroke-width="2" stroke-linecap="round"/>',
        "hair": '<path d="M26 52 C30 30 50 24 64 28 C74 32 78 42 76 52 C70 42 62 38 54 38 C44 38 32 44 26 52 Z" fill="#B5472A"/>'
                '<path d="M30 46 C38 34 52 30 66 32" fill="none" stroke="#D96B45" stroke-width="2" stroke-linecap="round"/>',
        "body": '<path d="M5 130 C8 100 26 92 50 92 C74 92 92 100 95 130 Z" fill="#1F8A8A"/>'
                '<path d="M38 93 Q50 108 62 93 Z" fill="#F5D3BC"/>'
                '<path d="M40 94 Q50 106 60 94" fill="none" stroke="#E8C35A" stroke-width="1.2"/>'
                '<circle cx="50" cy="104" r="2.2" fill="#E8C35A"/>'
                '<path d="M24 104 Q30 112 28 122 M76 104 Q70 112 72 122" fill="none" stroke="#18706F" stroke-width="2"/>',
        "brows": '<path d="M37 49 Q42 46 47 48 M53 48 Q58 46 63 49" fill="none" stroke="#8E3A22" stroke-width="2.2" stroke-linecap="round"/>',
        "mouth": '<path d="M42 69 Q50 79 58 69 Z" fill="#FFFFFF" stroke="#B34B4B" stroke-width="2" stroke-linejoin="round"/>',
        "lashes": True,
        "extras": "",
    },
]


def gang_member(person, x, y, scale):
    p = person

    eyes = "".join(
        f'<ellipse cx="{ex}" cy="56" rx="4.2" ry="3.4" fill="#FFFFFF"/>'
        f'<circle cx="{ex + 0.4}" cy="56.3" r="2.4" fill="{p["eyes"]}"/>'
        f'<circle cx="{ex + 0.4}" cy="56.3" r="1.2" fill="#1A120C"/>'
        f'<circle cx="{ex + 1.2}" cy="55.4" r="0.7" fill="#FFFFFF"/>'
        for ex in (42, 58)
    )

    lashes = ""
    if p["lashes"]:
        lashes = '<path d="M37.8 54.4 Q42 51.6 46.2 54 M53.8 54 Q58 51.6 62.2 54.4 M37.8 54.4 L35.8 53 M62.2 54.4 L64.2 53" fill="none" stroke="#2A1A10" stroke-width="1.3" stroke-linecap="round"/>'

    return f"""    <g transform="translate({x} {y}) scale({scale})">
      {p["hair_back"]}
      {p["body"]}
      <rect x="43" y="74" width="14" height="22" fill="{p["skin"]}"/>
      <path d="M43 80 Q50 86 57 80 V84 Q50 90 43 84 Z" fill="{p["shade"]}" opacity="0.6"/>
      <circle cx="26" cy="58" r="5" fill="{p["skin"]}"/>
      <circle cx="74" cy="58" r="5" fill="{p["skin"]}"/>
      <path d="M27 55 Q24 58 27 61 M73 55 Q76 58 73 61" fill="none" stroke="{p["shade"]}" stroke-width="1.4" stroke-linecap="round"/>
      <ellipse cx="50" cy="56" rx="24" ry="28" fill="{p["skin"]}"/>
      {p["hair"]}
      {p["brows"]}
      {eyes}
      {lashes}
      <path d="M50 58 Q47 65 49 67 Q52 68 54 66" fill="none" stroke="{p["shade"]}" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="35" cy="65" r="4" fill="#F2A08A" opacity="0.35"/>
      <circle cx="65" cy="65" r="4" fill="#F2A08A" opacity="0.35"/>
      {p["mouth"]}
      {p["extras"]}
    </g>"""


def beer_mug(x, y, angle, side):
    # A mug 24 wide and 30 tall, its bottom center at (x, y), tilted toward the middle
    return f"""    <g transform="translate({x} {y}) rotate({angle})">
      <g class="clink-{side}">
        <path d="M12 -22 C20 -22 22 -8 12 -6" fill="none" stroke="#F7E7C6" stroke-width="3.5" stroke-opacity="0.9"/>
        <rect x="-12" y="-30" width="24" height="30" rx="3" fill="#F2A93B"/>
        <rect x="-12" y="-30" width="24" height="30" rx="3" fill="none" stroke="#FFFFFF" stroke-opacity="0.55" stroke-width="2"/>
        <rect x="-8" y="-24" width="3" height="20" rx="1.5" fill="#FFFFFF" fill-opacity="0.45"/>
        <circle cx="3" cy="-12" r="1.6" fill="#FFF3D6" fill-opacity="0.8"/>
        <circle cx="6" cy="-19" r="1.2" fill="#FFF3D6" fill-opacity="0.8"/>
        <path d="M-14 -28 C-16 -36 -6 -40 -2 -35 C2 -41 12 -39 12 -33 C18 -34 18 -26 13 -26 Z" fill="#FFFFFF"/>
      </g>
    </g>"""


def beer_toast():
    # Five mugs meeting above Ted's head
    mugs = [(818, 152, 28, "left"), (842, 138, 14, "left"), (868, 132, 0, "middle"), (894, 138, -14, "right"), (918, 152, -28, "right")]
    sparkle = """    <g class="sparkle" stroke="#FFE680" stroke-width="3" stroke-linecap="round">
      <path d="M868 82 V70 M852 88 L844 80 M884 88 L892 80 M846 102 H836 M890 102 H900"/>
    </g>"""
    return "\n".join(beer_mug(*mug) for mug in mugs) + "\n" + sparkle


def gang():
    # (x, y, scale) for Barney, Robin, Ted, Marshall, Lily; Ted leans in, Marshall is the tallest
    spots = [(590, 168, 1.17), (698, 172, 1.14), (800, 152, 1.24), (916, 150, 1.32), (1040, 176, 1.12)]
    people = "\n".join(gang_member(person, *spot) for person, spot in zip(GANG, spots))
    return people + "\n" + beer_toast()


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
        sky = f"""    <circle cx="660" cy="62" r="90" fill="url(#glow)"/>
    <circle cx="660" cy="62" r="26" fill="{s["moon"]}"/>
    <circle cx="650" cy="54" r="5" fill="{s["sky_top"]}" opacity="0.12"/>
    <circle cx="668" cy="72" r="3.5" fill="{s["sky_top"]}" opacity="0.12"/>"""

        rain = "\n".join(
            f'    <line class="drop" x1="{dx}" y1="{dy}" x2="{dx - 4}" y2="{dy + 16}" stroke="{s["rain"]}" stroke-opacity="{rng.uniform(0.25, 0.6):.2f}" stroke-width="1.4" style="animation-delay: -{rng.uniform(0, 1.4):.2f}s; animation-duration: {rng.uniform(0.9, 1.4):.2f}s"/>'
            for dx, dy in ((rng.randint(0, 1220), rng.randint(-340, 300)) for _ in range(110))
        )

        # No rain under the umbrella
        weather = f"""  <mask id="dry">
    <rect width="1200" height="320" fill="#FFFFFF"/>
    <path transform="translate(1100 14) scale(0.52) translate(-1000 -42)" d="M906 150 Q1000 140 1094 150 L1110 320 L890 320 Z" fill="#000000"/>
  </mask>
  <g mask="url(#dry)">
{rain}
  </g>"""

        # The yellow umbrella
        prop = """  <g class="sway"><g transform="translate(1100 14) scale(0.52) translate(-1000 -42)">
    <path d="M1000 150 V250 A12 12 0 0 1 976 250" fill="none" stroke="#3B2A1A" stroke-width="5" stroke-linecap="round"/>
    <path d="M906 150 A94 94 0 0 1 1094 150 Q1070.5 134 1047 150 Q1023.5 134 1000 150 Q976.5 134 953 150 Q929.5 134 906 150 Z" fill="url(#canopy)"/>
    <path d="M1000 56 Q972 90 953 150 M1000 56 Q1028 90 1047 150" fill="none" stroke="#D99A00" stroke-width="2"/>
    <path d="M1000 56 Q960 76 930 120" fill="none" stroke="#FFF3A8" stroke-width="3" stroke-opacity="0.6" stroke-linecap="round"/>
    <line x1="1000" y1="56" x2="1000" y2="42" stroke="#3B2A1A" stroke-width="4" stroke-linecap="round"/>
  </g></g>"""
    else:
        glow_color = s["sun"]
        sky = f"""    <circle cx="660" cy="62" r="110" fill="url(#glow)"/>
    <circle cx="660" cy="62" r="30" fill="{s["sun"]}"/>"""

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
        prop = """  <g class="sway"><g transform="translate(1100 78) scale(0.5) translate(-1015 -185)">
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
  </g></g>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320" role="img" aria-label="hey, i'm borhan. Kids, let me tell you about the apps I built. Barney, Robin, Ted, Marshall and Lily from How I Met Your Mother raising a toast.">
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
    .sway {{ transform-box: view-box; transform-origin: 1100px 128px; animation: sway 5s ease-in-out infinite; }}
    @keyframes sway {{ 0%, 100% {{ transform: rotate(-4deg); }} 50% {{ transform: rotate(4deg); }} }}
    .twinkle {{ animation: twinkle 4s ease-in-out infinite; }}
    @keyframes twinkle {{ 50% {{ opacity: 0.15; }} }}
    .cloud {{ animation: drift 60s linear infinite alternate; }}
    .clink-left, .clink-right, .clink-middle {{ transform-box: fill-box; transform-origin: 50% 100%; animation: 2.4s ease-in-out infinite; }}
    .clink-left {{ animation-name: clinkLeft; }}
    .clink-right {{ animation-name: clinkRight; }}
    .clink-middle {{ animation-name: clinkMiddle; }}
    @keyframes clinkLeft {{ 0%, 60%, 100% {{ transform: rotate(0); }} 75% {{ transform: rotate(7deg); }} }}
    @keyframes clinkRight {{ 0%, 60%, 100% {{ transform: rotate(0); }} 75% {{ transform: rotate(-7deg); }} }}
    @keyframes clinkMiddle {{ 0%, 60%, 100% {{ transform: translateY(0); }} 75% {{ transform: translateY(-4px); }} }}
    .sparkle {{ opacity: 0; animation: sparkle 2.4s ease-out infinite; }}
    @keyframes sparkle {{ 0%, 70% {{ opacity: 0; }} 78% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
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
{gang()}
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
