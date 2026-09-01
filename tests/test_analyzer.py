from analyzer import analyze_repository


def test_analyze_repository():
    files = [
        {"name": "README.md"},
        {"name": ".gitignore"},
        {"name": "requirements.txt"},
        {"name": "test_scoring.py"}
    ]

    commits = [
        {"sha": "123456"}
    ]

    result = analyze_repository(files, commits)

    assert result["readme"] is True
    assert result["gitignore"] is True
    assert result["requirements"] is True
    assert result["tests"] is True
    assert result["commits"] is True