def calculate_score(analysis):
    score = 0

    if analysis["readme"]:
        score += 20

    if analysis["gitignore"]:
        score += 15

    if analysis["requirements"]:
        score += 15

    if analysis["tests"]:
        score += 20

    if analysis["commits"]:
        score += 30

    return score


def get_status(score):
    if score >= 80:
        return "🟢 Excellent"
    elif score >= 60:
        return "🟡 Good"
    elif score >= 40:
        return "🟠 Needs Improvement"
    else:
        return "🔴 Poor"