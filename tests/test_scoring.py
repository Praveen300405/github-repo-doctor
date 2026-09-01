from scoring import calculate_score, get_status


def test_calculate_score():
    analysis = {
        "readme": True,
        "gitignore": True,
        "requirements": True,
        "tests": True,
        "commits": True
    }

    score = calculate_score(analysis)

    assert score == 100


def test_get_status():
    assert get_status(100) == "🟢 Excellent"
    assert get_status(70) == "🟡 Good"
    assert get_status(50) == "🟠 Needs Improvement"
    assert get_status(30) == "🔴 Poor"