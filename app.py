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
# PROGRESS SYSTEM
# ============================================================

def initialize_progress():

    if "progress" not in st.session_state:

        st.session_state.progress = {}

        for language in languages:

            st.session_state.progress[language] = {
                "greetings": False,
                "common_words": False,
                "daily_phrases": False,
                "numbers": False,
                "quiz_score": 0
            }


def mark_topic_completed(language, topic):

    st.session_state.progress[language][topic] = True


def save_quiz_score(language, score):

    current_best = st.session_state.progress[language]["quiz_score"]

    if score > current_best:
        st.session_state.progress[language]["quiz_score"] = score
        return True

    return False


initialize_progress()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f7f9fc, #eef3f8);
}

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

div[data-testid="stRadio"] label {
    color: #222222 !important;
}

div[data-testid="stRadio"] label p {
    color: #222222 !important;
}

div[data-testid="stRadio"] span {
    color: #222222 !important;
}

div[data-testid="stSelectbox"] label {
    color: #222222 !important;
}

div[data-testid="stSelectbox"] div {
    color: #222222 !important;
}

.hero {
    padding: 45px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(135deg, #ff9933, #ffffff, #138808);
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 52px;
    font-weight: 800;
    color: #111111 !important;
}

.hero p {
    font-size: 21px;
    color: #222222 !important;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

.card h3 {
    color: #222222 !important;
}

.topic-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    margin-top: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.07);
}

.quiz-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

.result-card {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #e8f5e9, #ffffff);
    text-align: center;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🇮🇳 Bharat Bhasha")

st.sidebar.markdown(
    "### Learn Indian Languages"
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📚 Learn",
        "🧠 Quiz",
        "📊 Progress"
    ]
)

st.sidebar.markdown("---")

selected_language = st.sidebar.selectbox(
    "🌐 Choose Language",
    list(languages.keys())
)


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">

        <h1>🇮🇳 Bharat Bhasha</h1>

        <p>
        Discover and learn Indian languages in a simple and interactive way.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("🌏 Learn a New Indian Language")

    st.write(
        "Bharat Bhasha helps you learn useful words, greetings, "
        "daily phrases and numbers from different Indian languages."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">

        <h3>📚 Learn</h3>

        <p>
        Learn greetings, common words, daily phrases and numbers.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">

        <h3>🧠 Practice</h3>

        <p>
        Test your knowledge using language-based quizzes.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">

        <h3>📊 Track Progress</h3>

        <p>
        Complete topics and keep track of your best quiz score.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🌐 Available Languages")

    language_list = list(languages.keys())

    columns = st.columns(4)

    for i, language in enumerate(language_list):

        with columns[i % 4]:

            st.info(f"🇮🇳 {language}")


# ============================================================
# LEARN PAGE
# ============================================================

elif page == "📚 Learn":

    st.title("📚 Learn " + selected_language)

    st.write(
        "Choose a topic and start learning useful words and phrases."
    )

    topic_names = {
        "greetings": "👋 Greetings",
        "common_words": "📝 Common Words",
        "daily_phrases": "💬 Daily Phrases",
        "numbers": "🔢 Numbers"
    }

    topic = st.selectbox(
        "Choose a topic",
        list(topic_names.keys()),
        format_func=lambda x: topic_names[x]
    )

    st.markdown("---")

    st.subheader(topic_names[topic])

    data = languages[selected_language][topic]

    for english, translation in data.items():

        st.markdown(
            f"""
            <div class="topic-card">

            <h3>{english}</h3>

            <p style="font-size:20px;">
            ➜ <b>{translation}</b>
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    completed = st.session_state.progress[selected_language][topic]

    if completed:

        st.success("✅ You have completed this topic!")

    else:

        if st.button(
            "✅ Mark this topic as completed",
            key=f"complete_{selected_language}_{topic}"
        ):

            mark_topic_completed(
                selected_language,
                topic
            )

            st.success(
                f"🎉 {topic_names[topic]} completed!"
            )

            st.rerun()


# ============================================================
# QUIZ PAGE
# ============================================================

elif page == "🧠 Quiz":

    st.title("🧠 " + selected_language + " Practice Quiz")

    questions = quiz_questions[selected_language]

    st.write(
        f"Test your knowledge with **{len(questions)} questions**."
    )

    st.markdown("---")

    with st.form(
        key=f"quiz_form_{selected_language}"
    ):

        answers = []

        for i, question in enumerate(questions):

            st.markdown(
                f"""
                <div class="quiz-card">

                <h3>Question {i + 1}</h3>

                </div>
                """,
                unsafe_allow_html=True
            )

            option_keys = list(
                question["options"].keys()
            )

            option_labels = []

            for key in option_keys:

                label = (
                    f"{key}. "
                    f"{question['options'][key]}"
                )

                option_labels.append(label)

            selected_answer = st.radio(
                question["question"],
                option_labels,
                key=f"quiz_{selected_language}_{i}"
            )

            answers.append(selected_answer)

        submitted = st.form_submit_button(
            "🚀 Submit Quiz"
        )

    if submitted:

        score = 0

        for i, question in enumerate(questions):

            correct_key = question["answer"]

            correct_text = question["options"][
                correct_key
            ]

            correct_answer = (
                f"{correct_key}. {correct_text}"
            )

            if answers[i] == correct_answer:

                score += 1

        percentage = (
            score / len(questions)
        ) * 100

        new_best = save_quiz_score(
            selected_language,
            score
        )

        st.markdown(
            f"""
            <div class="result-card">

            <h2>🎉 Quiz Completed!</h2>

            <h1>{score}/{len(questions)}</h1>

            <h3>{percentage:.0f}%</h3>

            </div>
            """,
            unsafe_allow_html=True
        )

        if percentage == 100:

            st.success(
                "🏆 Excellent! Perfect score!"
            )

        elif percentage >= 60:

            st.success(
                "👏 Good job! Keep practicing."
            )

        else:

            st.warning(
                "📚 Keep learning and try again!"
            )

        if new_best:

            st.info(
                "⭐ New best score saved!"
            )

        else:

            st.info(
                f"⭐ Best score: "
                f"{st.session_state.progress[selected_language]['quiz_score']}"
                f"/{len(questions)}"
            )


# ============================================================
# PROGRESS PAGE
# ============================================================

elif page == "📊 Progress":

    st.title("📊 Your Learning Progress")

    st.subheader(
        f"🌐 {selected_language}"
    )

    data = st.session_state.progress[
        selected_language
    ]

    topics = [
        ("greetings", "👋 Greetings"),
        ("common_words", "📝 Common Words"),
        ("daily_phrases", "💬 Daily Phrases"),
        ("numbers", "🔢 Numbers")
    ]

    completed = 0

    for topic_key, topic_name in topics:

        if data[topic_key]:

            completed += 1

            st.success(
                f"✅ {topic_name} — Completed"
            )

        else:

            st.warning(
                f"⭕ {topic_name} — Not completed"
            )

    st.markdown("---")

    progress_percentage = (
        completed / len(topics)
    ) * 100

    st.subheader("📈 Learning Progress")

    st.progress(
        progress_percentage / 100
    )

    st.write(
        f"**{completed}/{len(topics)} topics completed "
        f"({progress_percentage:.0f}%)**"
    )

    st.markdown("---")

    st.subheader("🧠 Quiz Performance")

    questions = quiz_questions[selected_language]

    best_score = data["quiz_score"]

    st.metric(
        "⭐ Best Quiz Score",
        f"{best_score}/{len(questions)}"
    )

    if best_score > 0:

        quiz_percentage = (
            best_score / len(questions)
        ) * 100

        st.write(
            f"Best percentage: **{quiz_percentage:.0f}%**"
        )

    else:

        st.info(
            "Take the quiz to record your best score."
        )

    st.markdown("---")

    st.caption(
        "💡 Progress is stored for the current Streamlit session."
    )
