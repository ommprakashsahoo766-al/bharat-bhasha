import streamlit as st
from languages import languages
from quiz import quiz_questions


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .stApp {
        background: linear-gradient(
            135deg,
            #fffaf3 0%,
            #ffffff 50%,
            #f4f8ff 100%
        );
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero */
    .hero-box {
        background: linear-gradient(135deg, #ff9933, #ff6b00);
        padding: 45px 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(255, 120, 0, 0.20);
        margin-bottom: 25px;
    }

    .hero-icon {
        font-size: 60px;
    }

    /* Cards */
    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #eeeeee;
        box-shadow: 0 5px 18px rgba(0, 0, 0, 0.06);
        text-align: center;
        min-height: 170px;
        margin-bottom: 15px;
    }

    .card-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .card-text {
        color: #666666;
        font-size: 14px;
    }

    /* Language cards */
    .language-card {
        background: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #eeeeee;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-bottom: 15px;
        font-weight: 600;
    }

    /* Statistics */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #eeeeee;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }

    .stat-number {
        font-size: 32px;
        font-weight: 800;
        color: #ff7a00;
    }

    .stat-label {
        color: #666666;
        font-size: 14px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777777;
        padding: 35px 10px 10px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_language" not in st.session_state:
    st.session_state.selected_language = None

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = {}


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🇮🇳 Bharat Bhasha")

    st.caption("Learn. Connect. Communicate.")

    st.divider()

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

    if st.button("📚 Start Learning", use_container_width=True):
        st.session_state.page = "Learning"
        st.rerun()

    if st.button("📝 Practice Quiz", use_container_width=True):
        st.session_state.page = "Quiz"
        st.rerun()

    if st.button("📊 My Progress", use_container_width=True):
        st.session_state.page = "Progress"
        st.rerun()

    st.divider()

    st.markdown("### 🌏 Explore India")

    st.caption("12 Indian Languages")

    st.caption("Learn through words, phrases and quizzes.")

    st.divider()

    st.caption("Built with Python + Streamlit")


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "Home":

    # Hero background
    st.markdown("""
    <div class="hero-box">
        <div class="hero-icon">🇮🇳</div>
    </div>
    """, unsafe_allow_html=True)

    # Main hero text
    st.markdown(
        "<h1 style='text-align:center; font-size:52px; "
        "font-weight:800; margin-top:-10px;'>Bharat Bhasha</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center; color:#555555;'>"
        "Learn Indian Languages. Connect with India."
        "</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; font-size:18px; color:#666666;'>"
        "Discover words, phrases and expressions from across India."
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    # Start button
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "🚀 Start Learning",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.page = "Learning"
            st.rerun()

    st.write("")

    # --------------------------------------------------------
    # STATS
    # --------------------------------------------------------

    st.markdown("## 🌏 Explore Bharat Through Languages")

    st.write(
        "One platform to discover the linguistic diversity of India."
    )

    stat1, stat2, stat3, stat4 = st.columns(4)

    with stat1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">12</div>
            <div class="stat-label">Indian Languages</div>
        </div>
        """, unsafe_allow_html=True)

    with stat2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">4</div>
            <div class="stat-label">Learning Topics</div>
        </div>
        """, unsafe_allow_html=True)

    with stat3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">📝</div>
            <div class="stat-label">Practice Quizzes</div>
        </div>
        """, unsafe_allow_html=True)

    with stat4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">📊</div>
            <div class="stat-label">Progress Tracking</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # --------------------------------------------------------
    # FEATURES
    # --------------------------------------------------------

    st.markdown("## ✨ Why Bharat Bhasha?")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">📖</div>
            <div class="card-title">Learn Naturally</div>
            <div class="card-text">
                Learn greetings, common words, daily phrases
                and numbers in different Indian languages.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🧠</div>
            <div class="card-title">Practice & Test</div>
            <div class="card-text">
                Test your knowledge with interactive quizzes
                and improve your understanding.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">📊</div>
            <div class="card-title">Track Progress</div>
            <div class="card-text">
                Keep track of completed topics and
                your best quiz performance.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # --------------------------------------------------------
    # LANGUAGES
    # --------------------------------------------------------

    st.markdown("## 🗣️ Languages You Can Explore")

    language_list = list(languages.keys())

    columns = st.columns(4)

    for i, language in enumerate(language_list):

        with columns[i % 4]:

            st.markdown(
                f"""
                <div class="language-card">
                    🌐 {language}
                </div>
                """,
                unsafe_allow_html=True
            )

    # Footer
    st.markdown("""
    <div class="footer">
        <b>Bharat Bhasha</b><br>
        Celebrating India's linguistic diversity 🇮🇳
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# LEARNING PAGE
# ============================================================

elif st.session_state.page == "Learning":

    st.title("📚 Start Learning")

    st.write(
        "Choose a language and explore useful words and phrases."
    )

    st.divider()

    language_list = list(languages.keys())

    selected = st.selectbox(
        "🌐 Choose a language",
        language_list
    )

    st.session_state.selected_language = selected

    st.success(f"You are currently learning **{selected}**.")

    st.divider()

    topic = st.selectbox(
        "📖 Choose a topic",
        [
            "greetings",
            "common_words",
            "daily_phrases",
            "numbers"
        ],
        format_func=lambda x: x.replace("_", " ").title()
    )

    data = languages[selected][topic]

    st.markdown(
        f"## {topic.replace('_', ' ').title()}"
    )

    st.write("")

    # Display learning content
    for english, translation in data.items():

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**🇬🇧 English**")
            st.write(english)

        with col2:
            st.markdown(f"**🌐 {selected}**")
            st.write(translation)

        st.divider()

    # Save completed topic
    if selected not in st.session_state.completed_topics:
        st.session_state.completed_topics[selected] = set()

    st.session_state.completed_topics[selected].add(topic)

    st.success(
        f"✅ {topic.replace('_', ' ').title()} marked as completed!"
    )

    st.write("")

    if st.button(
        "📝 Take Practice Quiz",
        type="primary",
        use_container_width=True
    ):

        st.session_state.selected_language = selected
        st.session_state.page = "Quiz"
        st.rerun()


# ============================================================
# QUIZ PAGE
# ============================================================

elif st.session_state.page == "Quiz":

    st.title("📝 Practice Quiz")

    st.write(
        "Test your knowledge and see how much you have learned."
    )

    st.divider()

    language_list = list(quiz_questions.keys())

    # Remember selected language
    if st.session_state.selected_language in language_list:

        default_index = language_list.index(
            st.session_state.selected_language
        )

    else:

        default_index = 0

    selected = st.selectbox(
        "🌐 Choose a language",
        language_list,
        index=default_index
    )

    st.session_state.selected_language = selected

    questions = quiz_questions[selected]

    st.info(
        f"📋 This quiz contains **{len(questions)} questions**."
    )

    st.write("")

    # --------------------------------------------------------
    # QUIZ FORM
    # --------------------------------------------------------

    with st.form("quiz_form"):

        answers = []

        for i, question in enumerate(questions):

            st.markdown(
                f"### Question {i + 1}"
            )

            answer = st.radio(
                question["question"],
                list(question["options"].keys()),
                format_func=lambda option,
                q=question: f"{option}. {q['options'][option]}",
                key=f"{selected}_question_{i}"
            )

            answers.append(answer)

            st.divider()

        submitted = st.form_submit_button(
            "🚀 Submit Quiz",
            use_container_width=True,
            type="primary"
        )

    # --------------------------------------------------------
    # QUIZ RESULT
    # --------------------------------------------------------

    if submitted:

        score = 0

        for i, question in enumerate(questions):

            if answers[i] == question["answer"]:
                score += 1

        # Save best score
        if score > st.session_state.quiz_score:
            st.session_state.quiz_score = score

        percentage = (score / len(questions)) * 100

        st.write("")

        st.markdown("## 🎯 Quiz Result")

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            st.metric(
                "Your Score",
                f"{score}/{len(questions)}"
            )

        with result_col2:

            st.metric(
                "Percentage",
                f"{percentage:.0f}%"
            )

        st.progress(percentage / 100)

        st.write("")

        if percentage == 100:

            st.success(
                "🏆 Outstanding! You have mastered this quiz!"
            )

        elif percentage >= 60:

            st.success(
                "👏 Good job! Keep practicing and improving!"
            )

        else:

            st.warning(
                "📚 Keep learning and try the quiz again!"
            )


# ============================================================
# PROGRESS PAGE
# ============================================================

elif st.session_state.page == "Progress":

    st.title("📊 My Progress")

    st.write(
        "Track your Bharat Bhasha learning journey."
    )

    st.divider()

    language_list = list(languages.keys())

    selected = st.selectbox(
        "🌐 Choose a language",
        language_list
    )

    # --------------------------------------------------------
    # TOPIC PROGRESS
    # --------------------------------------------------------

    st.markdown("## 📚 Learning Topics")

    topics = [
        "greetings",
        "common_words",
        "daily_phrases",
        "numbers"
    ]

    completed_count = 0

    if selected in st.session_state.completed_topics:

        completed_topics = st.session_state.completed_topics[selected]

    else:

        completed_topics = set()

    for topic in topics:

        col1, col2 = st.columns([5, 1])

        with col1:

            st.write(
                topic.replace("_", " ").title()
            )

        with col2:

            if topic in completed_topics:

                st.write("✅")
                completed_count += 1

            else:

                st.write("⬜")

    # Progress percentage
    progress_percentage = completed_count / len(topics)

    st.divider()

    st.markdown("### 📈 Learning Progress")

    st.progress(progress_percentage)

    st.write(
        f"**{completed_count} of {len(topics)} topics completed "
        f"({progress_percentage * 100:.0f}%)**"
    )

    # --------------------------------------------------------
    # QUIZ SCORE
    # --------------------------------------------------------

    st.markdown("## 📝 Quiz Performance")

    if st.session_state.quiz_score > 0:

        quiz_total = len(
            quiz_questions[st.session_state.selected_language]
        ) if st.session_state.selected_language in quiz_questions else 1

        st.metric(
            "Best Quiz Score",
            f"{st.session_state.quiz_score}/{quiz_total}"
        )

    else:

        st.info(
            "Take a practice quiz to see your score here."
        )


# ============================================================
# FINAL FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    Bharat Bhasha • Learn Indian Languages • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
