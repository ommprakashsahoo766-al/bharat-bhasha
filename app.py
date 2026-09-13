import streamlit as st

from languages import languages
from quiz import quiz_questions
from progress import (
    progress,
    initialize_progress,
    mark_topic_completed,
    save_quiz_score
)

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: 800;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    margin-top: 5px;
    margin-bottom: 35px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.3);
    text-align: center;
    margin-bottom: 20px;
}

.language-card {
    padding: 15px;
    border-radius: 12px;
    border: 1px solid rgba(128,128,128,0.3);
    text-align: center;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

st.sidebar.title("🇮🇳 Bharat Bhasha")

page = st.sidebar.radio(
    "Menu",
    ["🏠 Home", "📖 Learn", "🧠 Quiz", "📊 Progress"]
)


# ==================================================
# HOME
# ==================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🇮🇳 Bharat Bhasha</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Learn • Practice • Discover Indian Languages</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.header("Welcome to Bharat Bhasha! 👋")

    st.write(
        "Bharat Bhasha is an interactive language-learning platform "
        "designed to help you learn Indian languages through vocabulary, "
        "phrases, numbers and quizzes."
    )

    st.info(
        "🌱 Start with a language, learn some words, and test your knowledge!"
    )

    st.divider()

    # ---------------- FEATURES ----------------

    st.subheader("✨ What can you do?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
            <h2>📖 Learn</h2>
            <p>Learn greetings, common words, daily phrases and numbers.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h2>🧠 Quiz</h2>
            <p>Test your knowledge and improve your language skills.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
            <h2>📊 Progress</h2>
            <p>Track your learning progress and best quiz scores.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ---------------- STATISTICS ----------------

    st.subheader("📈 Bharat Bhasha at a Glance")

    total_languages = len(languages)
    total_topics = 4

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌐 Languages", total_languages)

    with col2:
        st.metric("📚 Topics", total_topics)

    with col3:
        st.metric("🧠 Quiz Languages", len(quiz_questions))

    st.divider()

    # ---------------- LANGUAGES ----------------

    st.subheader("🌐 Available Languages")

    language_list = list(languages.keys())

    # Display languages in 4 columns
    for i in range(0, len(language_list), 4):

        cols = st.columns(4)

        for j, col in enumerate(cols):

            if i + j < len(language_list):

                language = language_list[i + j]

                with col:
                    st.markdown(
                        f"""
                        <div class="language-card">
                        <h4>🌐 {language}</h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    st.divider()

    st.success(
        "💡 Tip: Use the sidebar to start learning or take a quiz!"
    )


# ==================================================
# LEARN
# ==================================================

elif page == "📖 Learn":

    st.header("📖 Learn a Language")

    language = st.selectbox(
        "Select a language:",
        list(languages.keys())
    )

    topics = languages[language]

    topic_names = list(topics.keys())

    topic = st.selectbox(
        "Select a topic:",
        topic_names
    )

    st.divider()

    st.subheader(
        topic.replace("_", " ").title()
    )

    topic_data = topics[topic]

    if isinstance(topic_data, dict):

        for word, meaning in topic_data.items():

            st.markdown(
                f"### 🔹 {word}"
            )

            st.write(
                f"Meaning: **{meaning}**"
            )

            st.divider()

    elif isinstance(topic_data, list):

        for item in topic_data:

            st.write(f"🔹 {item}")

    else:

        st.write(topic_data)

    if st.button("✅ Mark Topic as Completed"):

        mark_topic_completed(
            language,
            topic
        )

        st.success(
            f"{topic.replace('_', ' ').title()} completed! 🎉"
        )


# ==================================================
# QUIZ
# ==================================================

elif page == "🧠 Quiz":

    st.header("🧠 Practice Quiz")

    language = st.selectbox(
        "Select a language:",
        list(quiz_questions.keys())
    )

    questions = quiz_questions[language]

    st.subheader(
        f"{language} Quiz"
    )

    st.write(
        f"Test your knowledge with {len(questions)} questions."
    )

    st.divider()

    with st.form("quiz_form"):

        answers = []

        for i, question in enumerate(questions):

            st.write(
                f"### Question {i + 1}"
            )

            st.write(
                f"**{question['question']}**"
            )

            options = question["options"]

            selected = st.radio(
                "Choose your answer:",
                list(options.keys()),
                format_func=lambda x: f"{x}. {options[x]}",
                key=f"question_{i}"
            )

            answers.append(selected)

            st.divider()

        submitted = st.form_submit_button(
            "🚀 Submit Quiz"
        )

    if submitted:

        score = 0

        for i, question in enumerate(questions):

            if answers[i] == question["answer"]:

                score += 1

        save_quiz_score(
            language,
            score
        )

        percentage = (
            score / len(questions)
        ) * 100

        st.success(
            f"🎯 Your Score: {score}/{len(questions)}"
        )

        st.progress(
            percentage / 100
        )

        st.write(
            f"### {percentage:.0f}%"
        )

        if percentage == 100:

            st.balloons()

            st.success(
                "🏆 Excellent! You have mastered this quiz!"
            )

        elif percentage >= 60:

            st.info(
                "👍 Good job! Keep practicing!"
            )

        else:

            st.warning(
                "💪 Keep learning and try the quiz again!"
            )


# ==================================================
# PROGRESS
# ==================================================

elif page == "📊 Progress":

    st.header("📊 Learning Progress")

    language = st.selectbox(
        "Select a language:",
        list(languages.keys())
    )

    initialize_progress(language)

    data = progress[language]

    topics = [
        "greetings",
        "common_words",
        "daily_phrases",
        "numbers"
    ]

    completed = 0

    for topic in topics:

        if data[topic]:

            completed += 1

            st.success(
                f"✅ {topic.replace('_', ' ').title()} — Completed"
            )

        else:

            st.warning(
                f"⬜ {topic.replace('_', ' ').title()} — Not Completed"
            )

    percentage = (
        completed / len(topics)
    ) * 100

    st.divider()

    st.subheader("Overall Progress")

    st.progress(
        percentage / 100
    )

    st.write(
        f"### {percentage:.0f}% Completed"
    )

    st.metric(
        "🏆 Best Quiz Score",
        data["quiz_score"]
    )
