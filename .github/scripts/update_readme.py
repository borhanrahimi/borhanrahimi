import hashlib
import json
import os
import re
import shutil
import urllib.request

import readme_svgs

USERNAME = os.environ["GITHUB_USERNAME"]
TOKEN = os.environ.get("GITHUB_TOKEN", "")

README_PATH = "README.md"
ASSETS_DIR = "assets"
ASSETS_URL = f"https://raw.githubusercontent.com/{USERNAME}/{USERNAME}/main/{ASSETS_DIR}"

# Any repo with this topic shows up in Featured Projects
FEATURED_TOPIC = "featured"

# Shown when no repo has the featured topic yet
DEFAULT_FEATURED = ["linkwell", "file_organizer", "borhan-portfolio"]

MAX_RECENT_PROJECTS = 3

# Section titles in the README: (number, title, file name)
SECTIONS = [
    (1, "About Me", "about"),
    (2, "Tech Stack", "tech-stack"),
    (3, "Featured Projects", "projects"),
    (4, "Recently Worked On", "recent"),
    (5, "GitHub Activity", "activity"),
    (6, "Words I Build By", "words"),
]

# GitHub topic -> label shown on a project card
TOPIC_LABELS = {
    "python": "Python",
    "java": "Java",
    "kotlin": "Kotlin",
    "c": "C",
    "cpp": "C++",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "html": "HTML",
    "css": "CSS",
    "react": "React",
    "nextjs": "Next.js",
    "vite": "Vite",
    "tailwind": "Tailwind",
    "tailwindcss": "Tailwind",
    "nodejs": "Node.js",
    "node": "Node.js",
    "express": "Express",
    "fastapi": "FastAPI",
    "flask": "Flask",
    "django": "Django",
    "tauri": "Tauri",
    "android": "Android",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "mysql": "MySQL",
    "mongodb": "MongoDB",
    "redis": "Redis",
    "prisma": "Prisma",
    "supabase": "Supabase",
    "firebase": "Firebase",
    "graphql": "GraphQL",
    "stripe": "Stripe",
    "docker": "Docker",
    "aws": "AWS",
    "vercel": "Vercel",
    "vitest": "Vitest",
    "jest": "Jest",
    "pytest": "pytest",
}

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": USERNAME,
}

if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"


def github_get(url):
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        return json.load(response)


def display_name(repo_name):
    # "file_organizer" -> "File Organizer", but keep "PicPick" and "RCP" as they are
    words = repo_name.replace("-", " ").replace("_", " ").split()
    return " ".join(word[0].upper() + word[1:] for word in words)


def write_svg(path, svg):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(svg)


def write_themed(path_without_theme, make_svg):
    for theme in readme_svgs.THEMES:
        write_svg(f"{path_without_theme}-{theme}.svg", make_svg(theme))


def themed_picture(path_without_theme, alt, width):
    dark = f"{ASSETS_URL}/{path_without_theme}-dark.svg"
    light = f"{ASSETS_URL}/{path_without_theme}-light.svg"

    return (
        "<picture>"
        f'<source media="(prefers-color-scheme: dark)" srcset="{dark}">'
        f'<source media="(prefers-color-scheme: light)" srcset="{light}">'
        f'<img src="{dark}" width="{width}" alt="{alt}">'
        "</picture>"
    )


def replace_section(content, name, new_block):
    start_marker = f"<!--{name}:start-->"
    end_marker = f"<!--{name}:end-->"

    if start_marker not in content:
        raise RuntimeError(f"{start_marker} not found in README.")

    if end_marker not in content:
        raise RuntimeError(f"{end_marker} not found in README.")

    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]

    return before + start_marker + "\n" + new_block + "\n" + end_marker + after


all_repos = github_get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=pushed"
)

own_repos = [
    repo for repo in all_repos
    if not repo.get("fork") and repo["name"].lower() != USERNAME.lower()
]

repos_by_name = {repo["name"]: repo for repo in own_repos}


# ---------- Header and section titles ----------

write_themed(f"{ASSETS_DIR}/header", readme_svgs.header)

for number, title, file_name in SECTIONS:
    write_themed(
        f"{ASSETS_DIR}/sections/{file_name}",
        lambda theme: readme_svgs.section_title(number, title, theme),
    )


# ---------- Featured Projects ----------

def card_tags(repo):
    tags = []
    for topic in repo.get("topics", []):
        label = TOPIC_LABELS.get(topic)
        if label and label not in tags:
            tags.append(label)

    # Fall back to the repo's main language when no topics match
    if not tags and repo.get("language"):
        tags.append(repo["language"])

    return tags


def project_cell(repo):
    name = display_name(repo["name"])
    picture = themed_picture(f"projects/{repo['name']}", f"{name} project card", "100%")

    links = []
    if repo.get("homepage"):
        links.append(f'<a href="{repo["homepage"]}">Live demo</a>')
    links.append(f'<a href="{repo["html_url"]}">Code</a>')

    return (
        '    <td width="50%" valign="top">\n'
        f'      <a href="{repo["html_url"]}">{picture}</a>\n'
        f'      <p align="center">{" · ".join(links)}</p>\n'
        "    </td>"
    )


featured_repos = [repo for repo in own_repos if FEATURED_TOPIC in repo.get("topics", [])]

if not featured_repos:
    print(f"No repos tagged '{FEATURED_TOPIC}', showing the default projects.")
    featured_repos = [repos_by_name[name] for name in DEFAULT_FEATURED if name in repos_by_name]

# Start fresh so cards for repos that are no longer featured get removed
shutil.rmtree(f"{ASSETS_DIR}/projects", ignore_errors=True)

for repo in featured_repos:
    write_themed(
        f"{ASSETS_DIR}/projects/{repo['name']}",
        lambda theme: readme_svgs.project_card(
            display_name(repo["name"]),
            repo.get("description") or "",
            card_tags(repo),
            bool(repo.get("homepage")),
            theme,
        ),
    )

rows = []

# Two cards per row
for i in range(0, len(featured_repos), 2):
    cells = [project_cell(repo) for repo in featured_repos[i:i + 2]]
    rows.append("  <tr>\n" + "\n".join(cells) + "\n  </tr>")

featured_block = "<table>\n" + "\n".join(rows) + "\n</table>"


# ---------- Recently Worked On ----------

events = github_get(
    f"https://api.github.com/users/{USERNAME}/events/public?per_page=100"
)

recent_repositories = []

for event in events:
    # Only look at pushes
    if event.get("type") != "PushEvent":
        continue

    repo_full_name = event.get("repo", {}).get("name")

    if not repo_full_name:
        continue

    repo_name = repo_full_name.split("/")[-1]

    # Don't show the GitHub profile repository itself
    if repo_name.lower() == USERNAME.lower():
        continue

    # Avoid duplicates
    if repo_name not in recent_repositories:
        recent_repositories.append(repo_name)

    if len(recent_repositories) >= MAX_RECENT_PROJECTS:
        break

project_lines = []

for repo_name in recent_repositories:
    repo_url = f"https://github.com/{USERNAME}/{repo_name}"
    language = repos_by_name.get(repo_name, {}).get("language")

    if language:
        project_lines.append(f"**[{display_name(repo_name)}]({repo_url})** · {language}")
    else:
        project_lines.append(f"**[{display_name(repo_name)}]({repo_url})**")

# If there are no recent public pushes
if not project_lines:
    project_lines.append("No recent public project activity.")

recent_block = "\n".join(line + "  " for line in project_lines).rstrip()


# ---------- Write README ----------

with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.read()

content = replace_section(content, "FEATURED_PROJECTS", featured_block)
content = replace_section(content, "RECENT_PROJECTS", recent_block)


def add_version(match):
    # GitHub caches images, so give each link a version that changes with the file
    path = match.group(1)

    with open(f"{ASSETS_DIR}/{path}", "rb") as file:
        version = hashlib.sha1(file.read()).hexdigest()[:8]

    return f"{ASSETS_URL}/{path}?v={version}"


content = re.sub(re.escape(ASSETS_URL) + r"/([\w./-]+\.svg)(?:\?v=\w+)?", add_version, content)

with open(README_PATH, "w", encoding="utf-8") as file:
    file.write(content)

print("README updated successfully.")
print("Featured repositories:")
for repo in featured_repos:
    print(f"- {repo['name']}")
print("Recent repositories:")
for repo in recent_repositories:
    print(f"- {repo}")
