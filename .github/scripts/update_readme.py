import json
import os
import urllib.request

USERNAME = os.environ["GITHUB_USERNAME"]
TOKEN = os.environ["GITHUB_TOKEN"]

README_PATH = "README.md"

# Any repo with this topic shows up in Featured Projects
FEATURED_TOPIC = "featured"

MAX_RECENT_PROJECTS = 3
MAX_ICONS = 6

# GitHub topic (or language) -> skillicons.dev icon id
ICONS = {
    "python": "py",
    "java": "java",
    "kotlin": "kotlin",
    "c": "c",
    "cpp": "cpp",
    "javascript": "js",
    "typescript": "ts",
    "html": "html",
    "css": "css",
    "react": "react",
    "nextjs": "nextjs",
    "vite": "vite",
    "tailwind": "tailwind",
    "tailwindcss": "tailwind",
    "nodejs": "nodejs",
    "node": "nodejs",
    "express": "express",
    "fastapi": "fastapi",
    "flask": "flask",
    "django": "django",
    "tauri": "tauri",
    "android": "androidstudio",
    "postgres": "postgres",
    "postgresql": "postgres",
    "mysql": "mysql",
    "mongodb": "mongodb",
    "redis": "redis",
    "prisma": "prisma",
    "supabase": "supabase",
    "firebase": "firebase",
    "graphql": "graphql",
    "docker": "docker",
    "aws": "aws",
    "vercel": "vercel",
    "vitest": "vitest",
    "jest": "jest",
}

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": USERNAME,
}


def github_get(url):
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        return json.load(response)


def display_name(repo_name):
    # "file_organizer" -> "File Organizer", but keep "PicPick" and "RCP" as they are
    words = repo_name.replace("-", " ").replace("_", " ").split()
    return " ".join(word[0].upper() + word[1:] for word in words)


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


# ---------- Featured Projects ----------

def project_card(repo):
    name = display_name(repo["name"])
    description = repo.get("description") or ""

    icons = []
    for topic in repo.get("topics", []):
        icon = ICONS.get(topic)
        if icon and icon not in icons:
            icons.append(icon)

    # Fall back to the repo's main language when no topics match an icon
    if not icons and repo.get("language"):
        icon = ICONS.get(repo["language"].lower())
        if icon:
            icons.append(icon)

    lines = [
        '    <td width="50%" valign="top">',
        f'      <h3><a href="{repo["html_url"]}">{name}</a></h3>',
        f"      {description}",
    ]

    if icons:
        icon_ids = ",".join(icons[:MAX_ICONS])
        lines += [
            "      <br><br>",
            f'      <img src="https://skillicons.dev/icons?i={icon_ids}&theme=dark" height="28" alt="{name} tech stack" />',
        ]

    links = []
    if repo.get("homepage"):
        links.append(f'<a href="{repo["homepage"]}">Live demo</a>')
    links.append(f'<a href="{repo["html_url"]}">Code</a>')

    lines += [
        "      <br><br>",
        "      " + " · ".join(links),
        "    </td>",
    ]

    return "\n".join(lines)


def featured_block(repos):
    rows = []

    # Two cards per row
    for i in range(0, len(repos), 2):
        cards = [project_card(repo) for repo in repos[i:i + 2]]
        rows.append("  <tr>\n" + "\n".join(cards) + "\n  </tr>")

    return "<table>\n" + "\n".join(rows) + "\n</table>"


all_repos = github_get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=pushed"
)

featured_repos = [
    repo for repo in all_repos
    if FEATURED_TOPIC in repo.get("topics", []) and not repo.get("fork")
]


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

repos_by_name = {repo["name"]: repo for repo in all_repos}
project_lines = []

for repo_name in recent_repositories:
    repo_url = f"https://github.com/{USERNAME}/{repo_name}"
    language = repos_by_name.get(repo_name, {}).get("language")

    if language:
        project_lines.append(f"**[{display_name(repo_name)}]({repo_url})** — {language}")
    else:
        project_lines.append(f"**[{display_name(repo_name)}]({repo_url})**")

# If there are no recent public pushes
if not project_lines:
    project_lines.append("No recent public project activity.")

recent_block = "\n".join(line + "  " for line in project_lines).rstrip()


# ---------- Write README ----------

with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.read()

# Leave the current cards alone if nothing is tagged yet
if featured_repos:
    content = replace_section(content, "FEATURED_PROJECTS", featured_block(featured_repos))
else:
    print(f"No repos tagged '{FEATURED_TOPIC}', keeping current Featured Projects.")

content = replace_section(content, "RECENT_PROJECTS", recent_block)

with open(README_PATH, "w", encoding="utf-8") as file:
    file.write(content)

print("README updated successfully.")
print("Featured repositories:")
for repo in featured_repos:
    print(f"- {repo['name']}")
print("Recent repositories:")
for repo in recent_repositories:
    print(f"- {repo}")
