def analyze_repository(files, commits):

    file_names = []

    for file in files:
        if "name" in file:
            file_names.append(file["name"].lower())

    analysis = {
        "readme": "readme.md" in file_names,
        "gitignore": ".gitignore" in file_names,
        "requirements": "requirements.txt" in file_names,
        "tests": any("test" in name for name in file_names),
        "commits": len(commits) > 0
    }

    return analysis