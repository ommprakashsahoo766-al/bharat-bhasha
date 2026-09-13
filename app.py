import streamlit as st
from languages import languages
from quiz import quiz_questions


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #fffaf0 0%, #ffffff 45%, #f3f8ff 100%);
    }

    /* Remove top spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hero section */
    .hero {
        padding: 55px 30px;
        border-radius: 25px;
        background: linear-gradient(135deg, #ff9933, #ff7a18);
        color: white;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 12px 35px rgba(255, 120, 20, 0.20);
    }

    .hero h1 {
        font-size: 55px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 21px;
        margin-bottom: 25px;
    }

    .tagline {
        font-size: 17px;
        opacity: 0.95;
    }

    /* Section heading */
    .section-title {
        font-size: 30px;
        font-weight: 750;
        margin-top: 25px;
        margin-bottom: 10px;
        color: #202124;
    }

    .section-subtitle {
        font-size: 16px;
        color: #666;
        margin-bottom: 25px;
    }

    /* Feature cards */
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        min-height: 180px;
        border: 1px solid #eeeeee;
        box-shadow: 0 5px 20px rgba(0,0,0,0.06);
        text-align: center;
    }

    .feature-icon {
        font-size: 38px;
        margin-bottom: 10px;
    }

    .feature-title {
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .feature-text {
        color: #666;
        font-size: 14px;
    }

    /* Language cards */
    .language-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #eeeeee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 15px;
    }

    .language-name {
        font-size: 18px;
        font-weight: 700;
        color: #222;
    }

    /* Stats */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #eeeeee;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    .stat-number {
        font-size: 32px;
        font-weight: 800;
        color: #ff7a18;
    }

    .stat-label {
        color: #666;
        font-size: 14px;
    }

    /* Learning content */
    .content-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #eeeeee;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 35px 10px 10px;
        color: #777;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_language" not in st.session_state:
    st.session_state.selected_language = None

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 🇮🇳 Bharat Bhasha")

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

    st.caption("12 Indian Languages")
    st.caption("Made with Python + Streamlit")


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "Home":

    # Hero
    st.markdown("""
    <div class="hero">

        <div style="font-size:55px;">🇮🇳</div>

        <h1>Bharat Bhasha</h1>

        <p>Learn Indian Languages. Connect with India.</p>

        <div class="tagline">
            Discover words, phrases and expressions from across India.
        </div>

    </div>
    """, unsafe_allow_html=True)


    # CTA
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "🚀 Start Learning",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.page = "Learning"
            st.rerun()


    # Stats
    st.markdown(
        '<div class="section-title">Explore Bharat Through Languages</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">One platform to discover the linguistic diversity of India.</div>',
        unsafe_allow_html=True
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
            <div class="stat-number">4+</div>
            <div class="stat-label">Learning Topics</div>
        </div>
        """, unsafe_allow_html=True)

    with stat3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">40+</div>
            <div class="stat-label">Learning Examples</div>
        </div>
        """, unsafe_allow_html=True)

    with stat4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">∞</div>
            <div class="stat-label">Ways to Learn</div>
        </div>
        """, unsafe_allow_html=True)


    # Features
    st.markdown(
        '<div class="section-title">Why Bharat Bhasha?</div>',
        unsafe_allow_html=True
    )

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📖</div>
            <div class="feature-title">Learn Naturally</div>
            <div class="feature-text">
                Learn greetings, common words, daily phrases and numbers.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Practice With Quizzes</div>
            <div class="feature-text">
                Test your knowledge and improve your language skills.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Track Your Progress</div>
            <div class="feature-text">
                Keep track of your learning journey and quiz performance.
            </div>
        </div>
        """, unsafe_allow_html=True)


    # Languages
    st.markdown(
        '<div class="section-title">Languages You Can Explore</div>',
        unsafe_allow_html=True
    )

    language_list = list(languages.keys())

    cols = st.columns(4)

    for i, language in enumerate(language_list):

        with cols[i % 4]:

            st.markdown(
                f"""
                <div class="language-card">
                    <div class="language-name">{language}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


    # Footer
    st.markdown("""
    <div class="footer">
        <b>Bharat Bhasha</b><br>
        Built to celebrate India's linguistic diversity 🇮🇳
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# LEARNING PAGE
# ============================================================

elif st.session_state.page == "Learning":

    st.markdown(
        '<div class="section-title">📚 Start Learning</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Choose an Indian language and begin your journey.</div>',
        unsafe_allow_html=True
    )

    selected = st.selectbox(
        "Choose a language",
        list(languages.keys())
    )

    st.session_state.selected_language = selected

    st.success(f"You are learning **{selected}**")


    topic = st.selectbox(
        "Choose a topic",
        [
            "greetings",
            "common_words",
            "daily_phrases",
            "numbers"
        ]
    )


    data = languages[selected][topic]

    st.markdown(
        f"""
        <div class="content-box">
            <h2>{topic.replace("_", " ").title()}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


    for english, translation in data.items():

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**English:** {english}")

        with col2:
            st.write(f"**{selected}:** {translation}")

        st.divider()


    if st.button("📝 Take Practice Quiz", type="primary"):

        st.session_state.page = "Quiz"
        st.rerun()


# ============================================================
# QUIZ PAGE
# ============================================================

elif st.session_state.page == "Quiz":

    st.markdown(
        '<div class="section-title">📝 Practice Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Test what you have learned.</div>',
        unsafe_allow_html=True
    )


    selected = st.selectbox(
        "Choose a language",
        list(quiz_questions.keys()),
        index=(
            list(quiz_questions.keys()).index(
                st.session_state.selected_language
            )
            if st.session_state.selected_language in quiz_questions
            else 0
        )
    )


    questions = quiz_questions[selected]

    st.info(f"Quiz contains {len(questions)} questions.")


    with st.form("quiz_form"):

        answers = []

        for i, question in enumerate(questions):

            st.markdown(f"### Question {i + 1}")

            answer = st.radio(
                question["question"],
                list(question["options"].keys()),
                format_func=lambda x, q=question:
                    f"{x}. {q['options'][x]}",
                key=f"question_{i}"
            )

            answers.append(answer)

            st.divider()


        submitted = st.form_submit_button(
            "Submit Quiz",
            type="primary",
            use_container_width=True
        )


    if submitted:

        score = 0

        for i, question in enumerate(questions):

            if answers[i] == question["answer"]:
                score += 1

        st.session_state.quiz_score = score

        percentage = (score / len(questions)) * 100

        st.markdown("## 🎯 Quiz Result")

        st.metric(
            "Your Score",
            f"{score}/{len(questions)}"
        )

        st.progress(percentage / 100)

        st.write(f"**Percentage: {percentage:.0f}%**")

        if percentage == 100:
            st.success("🏆 Excellent! You mastered this quiz!")

        elif percentage >= 60:
            st.success("👏 Good job! Keep practicing!")

        else:
            st.warning("📚 Keep learning and try again!")


# ============================================================
# PROGRESS PAGE
# ============================================================

elif st.session_state.page == "Progress":

    st.markdown(
        '<div class="section-title">📊 My Progress</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Track your Bharat Bhasha learning journey.</div>',
        unsafe_allow_html=True
    )


    selected = st.selectbox(
        "Choose a language",
        list(languages.keys())
    )


    st.markdown("### Learning Topics")

    topics = [
        "greetings",
        "common_words",
        "daily_phrases",
        "numbers"
    ]


    for topic in topics:

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(topic.replace("_", " ").title())

        with col2:
            st.write("✅")


    st.divider()

    st.markdown("### 📝 Best Quiz Score")

    if st.session_state.quiz_score > 0:

        st.metric(
            "Best Score",
            f"{st.session_state.quiz_score}/{len(quiz_questions[selected])}"
        )

    else:

        st.info("Take a quiz to see your score here.")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    Bharat Bhasha • Learn Indian Languages • Python + Streamlit
</div>
""", unsafe_allow_html=True)
