import re

import language_tool_python
from transformers import pipeline

FILLER_WORDS = [
    "um", "uh", "like", "basically", "you know",
    "kind of", "sort of", "actually", "literally", "right"
]

def detect_fillers(text):
    text_lower = text.lower()
    found = []
    for word in FILLER_WORDS:
        count = text_lower.count(word)
        if count > 0:
            found.append({"word": word, "count": count})
    total = sum(f["count"] for f in found)
    return found, total

def _fallback_grammar_errors(text):
    issues = 0
    words = re.findall(r"[A-Za-z']+", text)

    for current, nxt in zip(words, words[1:]):
        if current.lower() == nxt.lower() and len(current) > 2:
            issues += 1

    issues += len(re.findall(r"\b(?:im|dont|cant|wont|shouldnt|isnt|arent|didnt|wasnt|werent|havent|hasnt|hadnt|wouldnt|couldnt|mustnt)\b", text, flags=re.IGNORECASE))

    if text and text[-1] not in ".!?":
        issues += 1

    issues += len(re.findall(r"([.!?])\1+", text))
    return issues


def check_grammar(text):
    try:
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(text)
        return len(matches)
    except Exception:
        return _fallback_grammar_errors(text)

def analyze_sentiment(text):
    model = pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment"
    )
    result = model(text[:512])[0]
    sentiment_map = {
        "LABEL_0": "Negative",
        "LABEL_1": "Neutral",
        "LABEL_2": "Positive"
    }
    return sentiment_map.get(result["label"], "Neutral")

def analyze_speech(text):
    fillers, filler_count = detect_fillers(text)
    grammar_errors = check_grammar(text)
    sentiment = analyze_sentiment(text)
    return {
        "filler_count": filler_count,
        "fillers": fillers,
        "grammar_errors": grammar_errors,
        "sentiment": sentiment
    }