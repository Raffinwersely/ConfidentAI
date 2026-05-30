import spacy
import language_tool_python
from transformers import pipeline

# Filler Words list
FILLER_WORDS = [
    "um", "uh", "like", "basically", "you know",
    "kind of", "sort of", "actually", "literally", "right"
]

# Step 1 --> Filler words dectect
def detect_fillers(text):
    text_lower = text.lower()
    found = []
    for word in FILLER_WORDS:
        count = text_lower.count(word)
        if count > 0:
            found.append({"word": word, "count": count})
    total = sum(f["count"] for f in found)
    print(f"Filler Words: {total}")
    for f in found:
        print(f"   '{f["word"]}' -> {f["count"]} times")
    return found, total

# Step 2 --> Grammer Check
def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    print(f"Grammar errors: {len(matches)}")
    for m in matches:
        print(f"   ❌ {m.message}")
    return len(matches)

# Step 3 --> Sentiment Analysis
def analyze_sentiment(text):
    model = pipeline(
        "sentiment-analysis",
        model = "cardiffnlp/twitter-roberta-base-sentiment"
    )
    result = model(text[:512])[0]
    sentiment_map = {
        "LABEL_0": "Negative",
        "LABEL_1": "Neutral",
        "LABEL_2": "Positive"
    }
    sentiment = sentiment_map.get(result["label"], "Neutral")
    print(f"Tone: {sentiment}")
    return sentiment

# Main analysis function
def analyze_speech(text):
    print("\n" + "="*40)
    print("📊 ANALYSIS REPORT")
    print("="*40)
    print(f"🎤 Text: {text}\n")
    
    fillers, filler_count = detect_fillers(text)
    grammar_errors = check_grammar(text)
    sentiment = analyze_sentiment(text)
    
    print("="*40)
    
    return {
        "filler_count": filler_count,
        "fillers": fillers,
        "grammar_errors": grammar_errors,
        "sentiment": sentiment
    }

if __name__ == "__main__":
    test = "Um I am basiclly a good developer you know like I work hard"
    analyze_speech(test)