from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_model = None
def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    return _model

def check_relevance(user_answer, expected_keywords):
    """
    Compare user answer with expected answer keywords
    Returns similarity score 0-100
    """
    model = get_model()
    embeddings = model.encode([user_answer, expected_keywords])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    relevance_score = round(similarity * 100, 1)
    return max(0, min(100, relevance_score))


def calculate_score(filler_count, grammar_errors, sentiment, relevance_score=None):
    """
    If relevance_score is given:
      Final Score = 60% Communication + 40% Relevance
    Else:
      Final Score = 100% Communication (Free Talk mode)
    """
    comm_score = 100

    # Filler words penalty
    if filler_count == 0:
        comm_score -= 0
    elif filler_count <= 2:
        comm_score -= 10
    elif filler_count <= 4:
        comm_score -= 20
    elif filler_count <= 6:
        comm_score -= 30
    else:
        comm_score -= 45

    # Grammar errors penalty
    if grammar_errors == 0:
        comm_score -= 0
    elif grammar_errors <= 2:
        comm_score -= 10
    elif grammar_errors <= 4:
        comm_score -= 20
    elif grammar_errors <= 6:
        comm_score -= 30
    else:
        comm_score -= 40

    # Sentiment penalty
    if "Negative" in sentiment:
        comm_score -= 20
    elif "Neutral" in sentiment:
        comm_score -= 10

    comm_score = max(0, min(100, comm_score))

    if relevance_score is None:
        return comm_score

    final_score = (comm_score * 0.6) + (relevance_score * 0.4)
    return round(final_score)


def generate_feedback(filler_count, grammar_errors, sentiment, score, relevance_score=None):
    feedback = []

    # Filler words
    if filler_count == 0:
        feedback.append("Excellent! No filler words detected")
    elif filler_count <= 2:
        feedback.append("Minor filler words — try to reduce 'um', 'like', 'you know'")
    elif filler_count <= 4:
        feedback.append("Too many filler words — practice speaking without fillers")
    else:
        feedback.append("Way too many filler words — slow down and think before speaking")

    # Grammar
    if grammar_errors == 0:
        feedback.append("Perfect grammar!")
    elif grammar_errors <= 2:
        feedback.append("Minor grammar errors — review your sentences")
    elif grammar_errors <= 4:
        feedback.append("Multiple grammar errors — practice more")
    else:
        feedback.append("Many grammar errors — focus on sentence structure")

    # Tone
    if "Positive" in sentiment:
        feedback.append("Great confident tone!")
    elif "Neutral" in sentiment:
        feedback.append("Try to sound more enthusiastic and confident")
    else:
        feedback.append("Your tone sounds negative — work on sounding more positive")

    # Relevance feedback (only in Interview Mode)
    if relevance_score is not None:
        if relevance_score >= 70:
            feedback.append(f"Great! Your answer covers {relevance_score}% of expected key points")
        elif relevance_score >= 40:
            feedback.append(f"Your answer covers {relevance_score}% of expected key points — add more relevant details")
        else:
            feedback.append(f"Your answer covers only {relevance_score}% of expected key points — review this topic")

    # Overall
    if score >= 85:
        feedback.append("Outstanding! You are fully interview ready!")
    elif score >= 70:
        feedback.append("Good! You are almost interview ready!")
    elif score >= 50:
        feedback.append("Average — keep practicing daily!")
    else:
        feedback.append("Needs improvement — don't give up, practice more!")

    return feedback


def get_readiness_score(filler_count, grammar_errors, sentiment, relevance_score=None):
    score = calculate_score(filler_count, grammar_errors, sentiment, relevance_score)
    feedback = generate_feedback(filler_count, grammar_errors, sentiment, score, relevance_score)
    return score, feedback