def calculate_score(filler_count, grammar_errors, sentiment):
    score = 100

    # Filler Words Penalty
    score -= filler_count * 5

    # Grammar errors Penalty
    score -= grammar_errors *10

    # Sentiment Penalty
    if "Negative" in sentiment:
        score -= 15
    elif "Nertral" in sentiment:
        score -= 5

    # Score 0-100 range maintain
    score = max(0, min(100, score))

    return score


def generate_feedback(filler_count, grammar_errors, sentiment, score):
    feedback =[]
    
    if filler_count > 2:
        feedback.append(" Too many fillers words -- avoid 'um', 'like', 'you know'")
    elif filler_count > 0:
        feedback.append("Reduce filler words for better fluency")
    else:
        feedback.append("Great! No filler words detected")

    if grammar_errors > 2:
        feedback.append("Multiple grammar errors -- Practice more")
    elif grammar_errors > 0:
        feedback.append("Minor grammar errors -- Review your sentiment")
    else:
        feedback.append("Perfect grammars!")

    if "Positive" in sentiment:
        feedback.append("Great Confident Tone!")
    elif "Neutral" in sentiment:
        feedback.append("Try to sound more confident")
    else:
        feedback.append("Work on your tone -- sound more positive")

    if score >= 80:
        feedback.append("🏆 Excellent! You are interview ready!")
    elif score >= 60:
        feedback.append("💪 Good! Keep practicing")
    else:
        feedback.append("📚 Need more practice -- don't give up!")

    return feedback


def get_readiness_score(filler_count, grammar_errors, sentiment):
    score = calculate_score(filler_count, grammar_errors, sentiment)
    feedback = generate_feedback(filler_count, grammar_errors, sentiment, score)

    print("\n" + "="*40)
    print(f"INTERVIEW READINESS SCORE: {score}/100")
    print("="*40)
    print("\n FEEDBACK:")
    for f in feedback:
        print(f"   {f}")
    print("="*40)

    return score, feedback



if __name__ == "__main__":
    get_readiness_score(
        filler_count=3,
        grammar_errors=1,
        sentiment="Positive"
    )