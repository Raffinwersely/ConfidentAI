import streamlit as st
import sounddevice as sd
import soundfile as sf
import plotly.graph_objects as go
from speech.transcribe import transcribe_audio
from nlp.analyzer import analyze_speech
from scoring.score import get_readiness_score
from database.db import init_db, save_session, get_history

st.set_page_config(page_title="ConfidentAI", page_icon="🎤", layout="wide")
init_db()

# Header
st.title("🎤 ConfidentAI")
st.markdown("**Speak. Score. Improve.**")
st.markdown("---")

# Interview questions
QUESTIONS = [
    "Tell me about yourself",
    "What are your strengths?",
    "Why should we hire you?",
    "Where do you see yourself in 5 years?",
    "What is your greatest weakness?"
]

# Record function
def record_audio(duration=10, samplerate=16000):
    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    sf.write("input.wav", audio, samplerate)

# Feedback display function
def show_feedback(text, duration):
    with st.spinner("🔄 Analyzing..."):
        results = analyze_speech(text)
        filler_count = results["filler_count"]
        grammar_errors = results["grammar_errors"]
        sentiment = results["sentiment"]
        score, feedback = get_readiness_score(filler_count, grammar_errors, sentiment)
        save_session(text, filler_count, grammar_errors, sentiment, score)

    # Score gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Interview Readiness Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkblue"},
            "steps": [
                {"range": [0, 40],  "color": "#FF4444"},
                {"range": [40, 70], "color": "#FFA500"},
                {"range": [70, 100],"color": "#00CC44"},
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("🔴 Filler Words", filler_count)
    m2.metric("📝 Grammar Errors", grammar_errors)
    m3.metric("💬 Tone", sentiment.split()[0])

    # Feedback
    st.markdown("### 💡 Feedback:")
    for f in feedback:
        st.write(f)

    return score

# ── MODE SELECTION ───────────────────────────────────────
mode = st.radio(
    "### 🎯 Mode Select பண்ணு:",
    ["🗣️ Free Talk Mode", "📋 Interview Mode"],
    horizontal=True
)
st.markdown("---")

# ── FREE TALK MODE ───────────────────────────────────────
if mode == "🗣️ Free Talk Mode":
    st.markdown("### 🗣️ Free Talk Mode")
    st.info("Topic இல்லாம freely பேசு — AI analyze பண்ணும்!")

    duration = st.slider("Recording Duration (seconds)", 5, 30, 10)

    if st.button("🔴 Start Recording", use_container_width=True):
        with st.spinner("🎤 Recording... பேசு!"):
            record_audio(duration=duration)
        st.success("✅ Recording complete!")

        with st.spinner("Converting to text..."):
            text = transcribe_audio()

        st.markdown("**📝 நீ சொன்னது:**")
        st.write(text)
        st.markdown("---")

        show_feedback(text, duration)

# ── INTERVIEW MODE ───────────────────────────────────────
elif mode == "📋 Interview Mode":
    st.markdown("### 📋 Interview Mode")
    st.info("5 questions one by one கேக்கும் — ஒவ்வொன்னுக்கும் தனி feedback கிடைக்கும்!")

    # Session state initialize
    if "q_index" not in st.session_state:
        st.session_state["q_index"] = 0
        st.session_state["all_scores"] = []
        st.session_state["interview_done"] = False
        st.session_state["answered"] = False

    # Interview complete
    if st.session_state["interview_done"]:
        st.balloons()
        st.success("🎉 Interview Complete!")

        all_scores = st.session_state["all_scores"]
        avg = int(sum(all_scores) / len(all_scores))

        st.markdown(f"## 🏆 Overall Score: **{avg}/100**")

        # Score per question chart
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=[f"Q{i+1}" for i in range(len(all_scores))],
            y=all_scores,
            marker_color=["#FF4444" if s < 40 else "#FFA500" if s < 70 else "#00CC44" for s in all_scores]
        ))
        fig.update_layout(
            title="Score per Question",
            yaxis=dict(range=[0, 100])
        )
        st.plotly_chart(fig, use_container_width=True)

        if avg >= 80:
            st.success("🏆 Excellent! You are Interview Ready!")
        elif avg >= 60:
            st.warning("💪 Good! Keep Practicing!")
        else:
            st.error("📚 Need more practice — Don't give up!")

        if st.button("🔄 Restart Interview", use_container_width=True):
            st.session_state["q_index"] = 0
            st.session_state["all_scores"] = []
            st.session_state["interview_done"] = False
            st.session_state["answered"] = False
            st.rerun()

    else:
        q_index = st.session_state["q_index"]
        question = QUESTIONS[q_index]

        # Progress bar
        progress = q_index / len(QUESTIONS)
        st.progress(progress)
        st.markdown(f"**Question {q_index + 1} of {len(QUESTIONS)}**")

        # Show question
        st.markdown(f"### ❓ {question}")

        duration = st.slider("Recording Duration (seconds)", 5, 30, 10, key=f"dur_{q_index}")

        col1, col2 = st.columns(2)

        with col1:
            if not st.session_state["answered"]:
                if st.button("🔴 Record Answer", use_container_width=True):
                    with st.spinner("🎤 Recording... பேசு!"):
                        record_audio(duration=duration)
                    st.success("✅ Recording complete!")

                    with st.spinner("Converting to text..."):
                        text = transcribe_audio()

                    st.markdown("**📝 உன் Answer:**")
                    st.write(text)

                    score = show_feedback(text, duration)
                    st.session_state["all_scores"].append(score)
                    st.session_state["answered"] = True
                    st.rerun()

        with col2:
            if st.session_state["answered"]:
                # Next question button
                if q_index < len(QUESTIONS) - 1:
                    if st.button("➡️ Next Question", use_container_width=True):
                        st.session_state["q_index"] += 1
                        st.session_state["answered"] = False
                        st.rerun()
                else:
                    if st.button("✅ Finish Interview", use_container_width=True):
                        st.session_state["interview_done"] = True
                        st.rerun()

# ── PROGRESS HISTORY ────────────────────────────────────
st.markdown("---")
st.markdown("### 📈 Progress History")

history = get_history()
if history:
    dates  = [row[0] for row in history]
    scores = [row[1] for row in history]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=dates, y=scores,
        mode="lines+markers",
        line=dict(color="#4FC3F7", width=3),
        marker=dict(size=10)
    ))
    fig2.update_layout(
        title="Score Over Time",
        yaxis=dict(range=[0, 100])
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("No history yet — Start your first session!")