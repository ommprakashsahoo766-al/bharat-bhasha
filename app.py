import streamlit as st

from languages import languages
from quiz import quiz_questions


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f8fafc;
    }

    /* General text */
    .stMarkdown,
    .stMarkdown p,
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    label,
    p,
    span {
        color: #222222 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    section[data-testid="stSidebar"] * {
        color: #222222 !important;
    }

    /* Main title */
    .main-title {
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #555555 !important;
        margin-bottom: 30px;
    }

    /* Hero box */
    .hero {
        background: linear-gradient(135deg, #fff7ed, #eff6ff);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid #e5e7eb;
    }

    .hero h1 {
        font-size: 46px;
        font-weight: 800;
        color: #222222 !important;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 20px;
        color: #444444 !important;
    }

    /* Cards */
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    .card h3 {
        color: #222222 !important;
    }

    .card p {
        color: #555555 !important;
    }

    /* Quiz information box */
    .quiz-info {
        background-color: #dbeafe;
        padding: 18px;
        border-radius: 12px;
        margin: 20px 0;
        font-size: 17px;
        color: #1e40af !important;
    }

    /* Quiz question box */
    .quiz-question {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        margin-bottom: 18px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
    }

    .quiz-question h3 {
        color: #111827 !important;
    }

    /* Radio button text */
    div[data-testid="stRadio"] label {
        color: #222222 !important;
    }

    div[data-testid="stRadio"] label p {
        color: #222222 !important;
    }

    div[data-testid="stRadio"] span {
        color: #222222 !important;
    }

    /* Selectbox text */
    div[data-testid="stSelectbox"] label {
        color: #222222 !important;
    }

    div[data-testid="stSelectbox"] div {
        color: #222222 !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #666666 !important;
        padding: 30px;
        margin-top: 40px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🇮🇳 Bharat Bhasha")

st.sidebar.write("Learn Indian Languages")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📚 Learn",
        "📝 Practice Quiz",
        "📊 Progress"
    ]
)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "🏠 Home":

    st.markdown(
        '<div class="hero">'
        '<div style="font-size:60px;">🇮🇳</div>'
        '<h1>Bharat Bhasha</h1>'
        '<p>Learn Indian Languages. Connect with India.</p>'
        '<p>Discover words, phrases and expressions from across India.</p>'
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader("🌏 Explore Indian Languages")

    st.write(
        "Choose a language and start learning useful words, "
        "greetings, phrases and numbers."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📖 Learn</h3>
            <p>
            Learn greetings, common words, daily phrases and numbers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📝 Practice</h3>
            <p>
            Test your knowledge with language-based quizzes.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📊 Track Progress</h3>
            <p>
            Track completed topics and your best quiz score.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🗣️ Available Languages")

    language_list = list(languages.keys())

    cols = st.columns(4)

    for i, language in enumerate(language_list):

        with cols[i % 4]:

            st.markdown(
                f"""
                <div class="card" style="text-align:center;">
                    <h3>🌐 {language}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="footer">'
        '🇮🇳 Bharat Bhasha • Learn Languages • Connect with India'
        '</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# LEARN PAGE
# --------------------------------------------------

elif page == "📚 Learn":

    st.title("📚 Learn a Language")

    st.write(
        "Select a language and explore different learning topics."
    )

    selected_language = st.selectbox(
        "🌐 Choose a language",
        list(languages.keys())
    )

    topic = st.selectbox(
        "📖 Choose a topic",
        [
            "greetings",
            "common_words",
            "daily_phrases",
            "numbers"
        ]
    )

    st.markdown("---")

    topic_names = {
        "greetings": "👋 Greetings",
        "common_words": "💬 Common Words",
        "daily_phrases": "🗣️ Daily Phrases",
        "numbers": "🔢 Numbers"
    }

    st.subheader(
        f"{topic_names[topic]} — {selected_language}"
    )

    data = languages[selected_language][topic]

    for english, translation in data.items():

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"**English:** {english}"
            )

        with col2:
            st.markdown(
                f"**{selected_language}:** {translation}"
            )

        st.divider()


# --------------------------------------------------
# QUIZ PAGE
# --------------------------------------------------

elif page == "📝 Practice Quiz":

    st.title("📝 Practice Quiz")

    st.write(
        "Test your knowledge and see how much you have learned."
    )

    selected_language = st.selectbox(
        "🌐 Choose a language",
        list(quiz_questions.keys()),
        key="quiz_language"
    )

    questions = quiz_questions[selected_language]

    st.markdown(
        f"""
        <div class="quiz-info">
            📋 This quiz contains <b>{len(questions)} questions</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Quiz form
    with st.form("quiz_form"):

        answers = []

        for i, question in enumerate(questions):

            st.markdown(
                f"""
                <div class="quiz-question">
                    <h3>Question {i + 1}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Create complete option text
            option_keys = list(question["options"].keys())

            option_labels = []

            for key in option_keys:
                label = f"{key}. {question['options'][key]}"
                option_labels.append(label)

            # Display question
            selected_answer = st.radio(
                question["question"],
                option_labels,
                key=f"quiz_{selected_language}_{i}"
            )

            answers.append(selected_answer)

            st.divider()

        submitted = st.form_submit_button(
            "✅ Submit Quiz",
            use_container_width=True
        )

    # --------------------------------------------------
    # QUIZ RESULT
    # --------------------------------------------------

    if submitted:

        score = 0

        for i, question in enumerate(questions):

            selected_answer = answers[i]

            correct_key = question["answer"]

            correct_text = question["options"][correct_key]

            correct_answer = f"{correct_key}. {correct_text}"

            if selected_answer == correct_answer:
                score += 1

        percentage = (score / len(questions)) * 100

        st.markdown("---")

        st.subheader("🏆 Quiz Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Score",
                f"{score}/{len(questions)}"
            )

        with col2:
            st.metric(
                "Percentage",
                f"{percentage:.0f}%"
            )

        with col3:

            if percentage == 100:
                result = "Excellent! 🎉"

            elif percentage >= 60:
                result = "Good Job! 👍"

            else:
                result = "Keep Practicing! 💪"

            st.metric(
                "Result",
                result
            )

        if percentage == 100:

            st.success(
                "🎉 Excellent! You have mastered this quiz."
            )

        elif percentage >= 60:

            st.info(
                "👍 Good job! Keep practicing to improve."
            )

        else:

            st.warning(
                "💪 Keep learning and try the quiz again."
            )


# --------------------------------------------------
# PROGRESS PAGE
# --------------------------------------------------

elif page == "📊 Progress":

    st.title("📊 Your Learning Progress")

    st.write(
        "Track the topics you have completed."
    )

    selected_language = st.selectbox(
        "🌐 Choose a language",
        list(languages.keys()),
        key="progress_language"
    )

    # Create session progress
    if "progress" not in st.session_state:
        st.session_state.progress = {}

    if selected_language not in st.session_state.progress:

        st.session_state.progress[selected_language] = {
            "greetings": False,
            "common_words": False,
            "daily_phrases": False,
            "numbers": False,
            "quiz_score": 0
        }

    data = st.session_state.progress[selected_language]

    completed = 0

    topics = [
        ("greetings", "👋 Greetings"),
        ("common_words", "💬 Common Words"),
        ("daily_phrases", "🗣️ Daily Phrases"),
        ("numbers", "🔢 Numbers")
    ]

    for topic_key, topic_name in topics:

        if data[topic_key]:
            status = "✅ Completed"
            completed += 1
        else:
            status = "⬜ Not completed"

        st.write(
            f"**{topic_name}** — {status}"
        )

    progress_percentage = (completed / 4) * 100

    st.markdown("---")

    st.subheader("📈 Learning Progress")

    st.progress(
        progress_percentage / 100
    )

    st.write(
        f"You have completed **{progress_percentage:.0f}%** "
        "of the learning topics."
    )

    st.metric(
        "Best Quiz Score",
        data["quiz_score"]
    )

    st.info(
        "💡 Complete more learning topics and practice quizzes "
        "to improve your progress."
    )


# --------------------------------------------------
# END
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    '🇮🇳 Bharat Bhasha | Learn Indian Languages | Built with Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
