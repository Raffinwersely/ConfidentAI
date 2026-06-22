import streamlit as st
import sounddevice as sd
import soundfile as sf
import plotly.graph_objects as go
import random
from speech.transcribe import transcribe_audio
from nlp.analyzer import analyze_speech
from scoring.score import get_readiness_score, check_relevance
from database.db import init_db, save_session, get_history
from data.questions import INTERVIEW_QUESTIONS, DURATION_QUESTIONS, JOB_ROLES

st.set_page_config(page_title="ConfidentAI", page_icon="🎤", layout="wide")
init_db()

# HEADER
st.title("🎤 ConfidentAI")
st.markdown("Speak. Score. Improve. — Your AI Interview Coach")
st.markdown("---")

# RECORD FUNCTION
def record_audio(duration=10, samplerate=16000):
    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    sf.write("input.wav", audio, samplerate)

# FEEDBACK FUNCTION
def show_feedback(text, expected=None):
    results = analyze_speech(text)
    filler_count   = results["filler_count"]
    grammar_errors = results["grammar_errors"]
    sentiment      = results["sentiment"]

    relevance_score = None
    if expected:
        relevance_score = check_relevance(text, expected)

    score, feedback = get_readiness_score(filler_count, grammar_errors, sentiment, relevance_score)
    save_session(text, filler_count, grammar_errors, sentiment, score)

    # Score gauge
    color = "#00CC44" if score >= 70 else "#FFA500" if score >= 40 else "#FF4444"
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Interview Readiness Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar":  {"color": color},
            "steps": [
                {"range": [0,  40], "color": "#FFE5E5"},
                {"range": [40, 70], "color": "#FFF3CD"},
                {"range": [70,100], "color": "#E5FFE5"},
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    # Metrics
    if relevance_score is not None:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Filler Words",   filler_count)
        m2.metric("Grammar Errors", grammar_errors)
        m3.metric("Tone",           sentiment.split()[0])
        m4.metric("Relevance",      f"{relevance_score}%")
    else:
        m1, m2, m3 = st.columns(3)
        m1.metric("Filler Words",   filler_count)
        m2.metric("Grammar Errors", grammar_errors)
        m3.metric("Tone",           sentiment.split()[0])

    # Detailed feedback
    st.markdown("💡 Feedback:")
    if results["fillers"]:
        st.warning("Filler Words Detected:")
        for f in results["fillers"]:
            st.write(f"   • '{f['word']}' used {f['count']} time(s) — avoid this!")

    if "Negative" in sentiment:
        st.error("Tone: Your speech sounds negative — try to sound more confident!")
    elif "Neutral" in sentiment:
        st.warning("Tone: Your speech is neutral — add more enthusiasm!")
    else:
        st.success("Tone: Great confident tone! Keep it up!")

    for f in feedback:
        st.write(f)

    return score, filler_count, grammar_errors, sentiment, relevance_score

# MODE SELECTION
mode = st.radio(
    "Select Mode:",
    ["🗣️ Free Talk Mode", "📋 Interview Mode"],
    horizontal=True
)
st.markdown("---")

# FREE TALK MODE
if mode == "🗣️ Free Talk Mode":
    st.markdown("Free Talk Mode")
    st.info("Speak freely on any topic — AI will analyze your communication!")

    duration = st.slider("Recording Duration (seconds)", 5, 30, 10)

    if st.button("🔴 Start Recording", use_container_width=True):
        with st.spinner("Recording... Please speak now!"):
            record_audio(duration=duration)
        st.success("Recording complete!")

        with st.spinner("Converting speech to text..."):
            text = transcribe_audio()

        st.markdown("Your Speech:")
        st.write(text)
        st.markdown("---")

        with st.spinner("Analyzing..."):
            show_feedback(text)

# INTERVIEW MODE
elif mode == "📋 Interview Mode":
    st.markdown("Interview Mode")

    if "interview_started" not in st.session_state:
        st.session_state["interview_started"] = False

    if not st.session_state["interview_started"]:

        st.markdown("Step 1: Select Your Job Role")
        selected_role = st.selectbox("Job Role:", JOB_ROLES)

        st.markdown("Step 2: Select Interview Duration")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("⏱️ 30 mins\n(5 Questions)", use_container_width=True):
                st.session_state["duration_key"] = "30 mins"
        with col2:
            if st.button("⏱️ 45 mins\n(8 Questions)", use_container_width=True):
                st.session_state["duration_key"] = "45 mins"
        with col3:
            if st.button("⏱️ 1 hour\n(12 Questions)", use_container_width=True):
                st.session_state["duration_key"] = "1 hour"

        if "duration_key" in st.session_state:
            duration_key  = st.session_state["duration_key"]
            num_questions = DURATION_QUESTIONS[duration_key]
            st.info(f"Selected: **{selected_role}** | **{duration_key}** | **{num_questions} Questions**")

            if st.button("Start Interview!", use_container_width=True):
                all_questions = INTERVIEW_QUESTIONS[selected_role]
                selected_questions = random.sample(
                    all_questions,
                    min(num_questions, len(all_questions))
                )
                st.session_state["interview_started"] = True
                st.session_state["questions"]         = selected_questions
                st.session_state["q_index"]           = 0
                st.session_state["all_scores"]        = []
                st.session_state["all_feedback"]      = []
                st.session_state["interview_done"]    = False
                st.session_state["answered"]          = False
                st.session_state["selected_role"]     = selected_role
                st.session_state["duration_key"]      = duration_key
                st.rerun()

    elif not st.session_state.get("interview_done", False):
        questions     = st.session_state["questions"]
        q_index       = st.session_state["q_index"]
        question_data = questions[q_index]
        question      = question_data["question"]
        expected      = question_data["expected"]
        total_q       = len(questions)
        role          = st.session_state["selected_role"]
        dur           = st.session_state["duration_key"]

        st.markdown(f"**Role:** {role} | **Duration:** {dur} | **Question {q_index+1} of {total_q}**")
        st.progress((q_index) / total_q)
        st.markdown("---")

        # Question box
        st.markdown(
            f"""
            <div style='background:#1E2761;padding:20px;border-radius:10px;
                        border-left:5px solid #4FC3F7;'>
                <h3 style='color:#4FC3F7;margin:0'>Question {q_index+1}</h3>
                <p style='color:white;font-size:18px;margin:10px 0 0'>{question}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("")

        rec_duration = st.slider("Recording Duration (seconds)", 5, 60, 15, key=f"dur_{q_index}")

        col1, col2 = st.columns(2)

        with col1:
            if not st.session_state["answered"]:
                if st.button("Record Answer", use_container_width=True, key=f"rec_{q_index}"):
                    with st.spinner("Recording... Please speak now!"):
                        record_audio(duration=rec_duration)
                    st.success("Recording complete!")

                    with st.spinner("Converting to text..."):
                        text = transcribe_audio()

                    st.markdown("Your Answer:")
                    st.write(text)
                    st.markdown("---")

                    with st.spinner("Analyzing..."):
                        score, fc, ge, sent, rel = show_feedback(text, expected=expected)

                    st.session_state["all_scores"].append(score)
                    st.session_state["all_feedback"].append({
                        "question":  question,
                        "text":      text,
                        "score":     score,
                        "fillers":   fc,
                        "grammar":   ge,
                        "sentiment": sent,
                        "relevance": rel
                    })
                    st.session_state["answered"] = True
                    st.rerun()

        with col2:
            if st.session_state["answered"]:
                current_score = st.session_state["all_scores"][-1]
                if current_score >= 70:
                    st.success(f"Score: {current_score}/100 — Great answer!")
                elif current_score >= 40:
                    st.warning(f"Score: {current_score}/100 — Good, keep improving!")
                else:
                    st.error(f"Score: {current_score}/100 — Practice more!")

                st.markdown("")
                if q_index < total_q - 1:
                    if st.button("Next Question →", use_container_width=True):
                        st.session_state["q_index"] += 1
                        st.session_state["answered"] = False
                        st.rerun()
                else:
                    if st.button("Finish Interview", use_container_width=True):
                        st.session_state["interview_done"] = True
                        st.rerun()

    else:
        st.balloons()
        all_scores   = st.session_state["all_scores"]
        all_feedback = st.session_state["all_feedback"]
        role         = st.session_state["selected_role"]
        avg_score    = int(sum(all_scores) / len(all_scores))

        st.markdown(f"Interview Complete! — {role}")
        st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=avg_score,
                title={"text": "Overall Interview Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar":  {"color": "#1E2761"},
                    "steps": [
                        {"range": [0,  40], "color": "#FFE5E5"},
                        {"range": [40, 70], "color": "#FFF3CD"},
                        {"range": [70,100], "color": "#E5FFE5"},
                    ]
                }
            ))
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("Overall Stats")
            avg_fillers   = round(sum(f["fillers"]   for f in all_feedback) / len(all_feedback), 1)
            avg_grammar   = round(sum(f["grammar"]   for f in all_feedback) / len(all_feedback), 1)
            avg_relevance = round(sum(f["relevance"] for f in all_feedback) / len(all_feedback), 1)
            pos_count     = sum(1 for f in all_feedback if "Positive" in f["sentiment"])

            st.metric("Overall Score",      f"{avg_score}/100")
            st.metric("Avg Filler Words",   avg_fillers)
            st.metric("Avg Grammar Errors", avg_grammar)
            st.metric("Avg Relevance",      f"{avg_relevance}%")
            st.metric("Positive Answers",   f"{pos_count}/{len(all_feedback)}")

            if avg_score >= 70:
                st.success("Excellent! You are Interview Ready!")
            elif avg_score >= 40:
                st.warning("Good! Keep Practicing!")
            else:
                st.error("Need more practice — Don't give up!")

        # Score per question
        st.markdown("Score per Question")
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=[f"Q{i+1}" for i in range(len(all_scores))],
            y=all_scores,
            marker_color=[
                "#00CC44" if s >= 70 else
                "#FFA500" if s >= 40 else
                "#FF4444"
                for s in all_scores
            ],
            text=all_scores,
            textposition="auto"
        ))
        fig2.update_layout(yaxis=dict(range=[0, 100]), title="Score per Question")
        st.plotly_chart(fig2, use_container_width=True)

        # Question breakdown
        st.markdown("Question-by-Question Breakdown")
        for i, fb in enumerate(all_feedback):
            with st.expander(f"Q{i+1}: {fb['question']} — Score: {fb['score']}/100"):
                st.markdown(f"**Your Answer:** {fb['text']}")
                st.markdown(f"**Filler Words:** {fb['fillers']}")
                st.markdown(f"**Grammar Errors:** {fb['grammar']}")
                st.markdown(f"**Tone:** {fb['sentiment']}")
                st.markdown(f"**Content Relevance:** {fb['relevance']}%")
                if fb['score'] >= 70:
                    st.success("Strong answer!")
                elif fb['score'] >= 40:
                    st.warning("Average answer — improve this")
                else:
                    st.error("Weak answer — practice more")

        if st.button("Start New Interview", use_container_width=True):
            for key in ["interview_started","questions","q_index",
                        "all_scores","all_feedback","interview_done",
                        "answered","selected_role","duration_key"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# PROGRESS HISTORY
st.markdown("---")
st.markdown("Progress History")

history = get_history()
if history:
    dates  = [row[0] for row in history]
    scores = [row[1] for row in history]

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=dates, y=scores,
        mode="lines+markers",
        line=dict(color="#4FC3F7", width=3),
        marker=dict(size=10)
    ))
    fig3.update_layout(
        title="Score Over Time",
        yaxis=dict(range=[0, 100])
    )
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("No history yet — Start your first session!")