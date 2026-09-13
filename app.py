import streamlit as st


# ============================================================
# IMPORTS
# ============================================================

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

/* ==========================================================
   MAIN PAGE
   ========================================================== */

.stApp {
    background-color: #f5f7fb;
}


/* ==========================================================
   SIDEBAR
   ========================================================== */

section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}

section[data-testid="stSidebar"] * {
    color: #222222 !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #222222 !important;
}


/* Sidebar radio */

section[data-testid="stSidebar"] div[data-testid="stRadio"] label {
    color: #222222 !important;
}

section[data-testid="stSidebar"] div[data-testid="stRadio"] label p {
    color: #222222 !important;
}


/* Sidebar selectbox */

section[data-testid="stSidebar"] div[data-testid="stSelectbox"] label {
    color: #222222 !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] {
    background-color: #ffffff !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #222222 !important;
}


/* ==========================================================
   GENERAL TEXT
   ========================================================== */

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #222222 !important;
}

.stMarkdown p {
    color: #222222 !important;
}


/* ==========================================================
   HERO
   ========================================================== */

.hero {
    background: linear-gradient(
        135deg,
        #ff9933,
        #ffffff,
        #138808
    );

    padding: 45px;

    border-radius: 25px;

    text-align: center;

    margin-bottom: 35px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: #111111 !important;
    margin-bottom: 15px;
}

.hero-subtitle {
    font-size: 20px;
    color: #222222 !important;
}


/* ==========================================================
   HOME CARDS
   ========================================================== */

.card {
    background-color: #ffffff;

    padding: 25px;

    border-radius: 18px;

    margin-bottom: 20px;

    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
}

.card-title {
    font-size: 25px;
    font-weight: 700;
    color: #222222 !important;

    margin-bottom: 10px;
}

.card-text {
    font-size: 16px;
    color: #333333 !important;
}


/* ==========================================================
   TOPIC CARDS
   ========================================================== */

.topic-card {
    background-color: #ffffff;

    padding: 20px;

    border-radius: 15px;

    margin-top: 12px;
    margin-bottom: 12px;

    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
}

.topic-title {
    font-size: 21px;
    font-weight: 700;
    color: #222222 !important;
}

.topic-translation {
    font-size: 19px;
    color: #333333 !important;
}


/* ==========================================================
   QUIZ
   ========================================================== */

.quiz-card {
    background-color: #ffffff;

    padding: 20px;

    border-radius: 16px;

    margin-bottom: 15px;

    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.07);
}


/* Quiz question text */

div[data-testid="stRadio"] label {
    color: #222222 !important;
}

div[data-testid="stRadio"] label p {
    color: #222222 !important;
}

div[data-testid="stRadio"] span {
    color: #222222 !important;
}


/* ==========================================================
   RESULT
   ========================================================== */

.result-card {
    background-color: #ffffff;

    padding: 30px;

    border-radius: 20px;

    text-align: center;

    margin-top: 25px;

    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
}

.result-score {
    font-size: 50px;
    font-weight: 800;
    color: #111111 !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🇮🇳 Bharat Bhasha")

st.sidebar.write("Learn Indian Languages")

st.sidebar.markdown("---")

st.sidebar.subheader("Navigate")

page = st.sidebar.radio(
    "Choose a page",
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

    <div class="hero-title">
        🇮🇳 Bharat Bhasha
    </div>

    <div class="hero-subtitle">
        Discover and learn Indian languages
        in a simple and interactive way.
    </div>

</div>
""", unsafe_allow_html=True)


    st.header("🌏 Learn a New Indian Language")

    st.write(
        "Bharat Bhasha helps you learn useful words, "
        "greetings, daily phrases and numbers from "
        "different Indian languages."
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown("""
<div class="card">

    <div class="card-title">
        📚 Learn
    </div>

    <div class="card-text">
        Learn greetings, common words,
        daily phrases and numbers.
    </div>

</div>
""", unsafe_allow_html=True)


    with col2:

        st.markdown("""
<div class="card">

    <div class="card-title">
        🧠 Practice
    </div>

    <div class="card-text">
        Test your knowledge using
        language-based quizzes.
    </div>

</div>
""", unsafe_allow_html=True)


    with col3:

        st.markdown("""
<div class="card">

    <div class="card-title">
        📊 Track Progress
    </div>

    <div class="card-text">
        Complete topics and track
        your best quiz score.
    </div>

</div>
""", unsafe_allow_html=True)


    st.markdown("---")

    st.header("🌐 Available Languages")

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
        "Choose a topic and start learning useful "
        "words and phrases."
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

    <div class="topic-title">
        {english}
    </div>

    <div class="topic-translation">
        ➜ {translation}
    </div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("---")


    completed = st.session_state.progress[
        selected_language
    ][topic]


    if completed:

        st.success(
            "✅ You have completed this topic!"
        )

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

    st.title(
        "🧠 " +
        selected_language +
        " Practice Quiz"
    )


    questions = quiz_questions[
        selected_language
    ]


    st.write(
        f"Test your knowledge with "
        f"**{len(questions)} questions**."
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

    <b>Question {i + 1}</b>

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


            answers.append(
                selected_answer
            )


        submitted = st.form_submit_button(
            "🚀 Submit Quiz"
        )


    if submitted:

        score = 0


        for i, question in enumerate(questions):

            correct_key = question["answer"]


            correct_text = question[
                "options"
            ][correct_key]


            correct_answer = (
                f"{correct_key}. "
                f"{correct_text}"
            )


            if answers[i] == correct_answer:

                score += 1


        percentage = (
            score /
            len(questions)
        ) * 100


        new_best = save_quiz_score(
            selected_language,
            score
        )


        st.markdown(
            f"""
<div class="result-card">

    <div class="result-score">
        {score}/{len(questions)}
    </div>

    <h3>
        {percentage:.0f}%
    </h3>

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
        "🌐 " + selected_language
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
        completed /
        len(topics)
    ) * 100


    st.subheader(
        "📈 Learning Progress"
    )


    st.progress(
        progress_percentage / 100
    )


    st.write(
        f"**{completed}/{len(topics)} topics completed "
        f"({progress_percentage:.0f}%)**"
    )


    st.markdown("---")


    st.subheader(
        "🧠 Quiz Performance"
    )


    questions = quiz_questions[
        selected_language
    ]


    best_score = data["quiz_score"]


    st.metric(
        "⭐ Best Quiz Score",
        f"{best_score}/{len(questions)}"
    )


    if best_score > 0:

        quiz_percentage = (
            best_score /
            len(questions)
        ) * 100


        st.write(
            f"Best percentage: "
            f"**{quiz_percentage:.0f}%**"
        )

    else:

        st.info(
            "Take the quiz to record your best score."
        )


    st.markdown("---")


    st.caption(
        "💡 Progress is stored for the current "
        "Streamlit session."
    )
