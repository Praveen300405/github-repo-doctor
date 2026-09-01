import requests


def get_repository(repo_url):
    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 2:
        return None

    owner = parts[-2]
    repo = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(api_url, timeout=10)

    if response.status_code != 200:
        return None

    return response.json()


def get_files(owner, repo):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = requests.get(api_url, timeout=10)

    if response.status_code != 200:
        return []

    return response.json()


def get_commits(owner, repo):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(api_url, timeout=10)

    if response.status_code != 200:
        return []

    return response.json()