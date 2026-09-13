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

    old_score = st.session_state.progress[language]["quiz_score"]

    if score > old_score:

        st.session_state.progress[language]["quiz_score"] = score

        return True

    return False


initialize_progress()


# ============================================================
# SIMPLE CSS
# ============================================================

st.markdown("""
<style>

/* Main background */

.stApp {
    background-color: #f5f7fb;
}


/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #222222 !important;
}


/* Main headings */

h1, h2, h3, h4 {
    color: #222222 !important;
}


/* Normal text */

p {
    color: #222222 !important;
}


/* Selectbox text */

div[data-baseweb="select"] {
    background-color: #ffffff !important;
}

div[data-baseweb="select"] * {
    color: #222222 !important;
}


/* Buttons */

.stButton button {
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🇮🇳 Bharat Bhasha")

st.sidebar.write("Learn Indian Languages")

st.sidebar.divider()

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

st.sidebar.divider()

selected_language = st.sidebar.selectbox(
    "🌐 Choose Language",
    list(languages.keys())
)


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.title("🇮🇳 Bharat Bhasha")

    st.subheader(
        "Discover and learn Indian languages"
    )

    st.write(
        "Bharat Bhasha is an interactive platform "
        "for learning useful Indian language words "
        "and phrases."
    )

    st.divider()

    st.header("🌏 Learn a New Indian Language")

    st.write(
        "Choose a language and start learning "
        "greetings, common words, daily phrases "
        "and numbers."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("📚 Learn")

        st.write(
            "Learn greetings, common words, "
            "daily phrases and numbers."
        )

    with col2:

        st.subheader("🧠 Practice")

        st.write(
            "Test your knowledge with "
            "language-based quizzes."
        )

    with col3:

        st.subheader("📊 Track Progress")

        st.write(
            "Complete topics and track "
            "your best quiz score."
        )

    st.divider()

    st.header("🌐 Available Languages")

    language_list = list(languages.keys())

    columns = st.columns(4)

    for i, language in enumerate(language_list):

        with columns[i % 4]:

            st.info(
                f"🇮🇳 {language}"
            )


# ============================================================
# LEARN PAGE
# ============================================================

elif page == "📚 Learn":

    st.title(
        f"📚 Learn {selected_language}"
    )

    st.write(
        "Choose a topic and start learning."
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

    st.divider()

    st.header(
        topic_names[topic]
    )

    data = languages[
        selected_language
    ][topic]

for native_word, english_meaning in data.items():

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**English:** {english_meaning}"
        )

    with col2:

        st.write(
            f"**{selected_language}:** {native_word}"
        )

    st.divider()

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
        f"🧠 {selected_language} Practice Quiz"
    )

    questions = quiz_questions[
        selected_language
    ]

    st.write(
        f"Test your knowledge with "
        f"{len(questions)} questions."
    )

    st.divider()

    answers = []

    # --------------------------------------------------------
    # SHOW QUESTIONS
    # --------------------------------------------------------

    for i, question in enumerate(questions):

        st.subheader(
            f"Question {i + 1}"
        )

        # Question text
        st.write(
            question["question"]
        )

        # Create visible answer labels
        option_keys = list(
            question["options"].keys()
        )

        option_labels = []

        for key in option_keys:

            option_labels.append(
                f"{key}. {question['options'][key]}"
            )

        # Dropdown instead of radio
        selected_answer = st.selectbox(
            "Choose your answer:",
            option_labels,
            key=f"answer_{selected_language}_{i}"
        )

        answers.append(
            selected_answer
        )

        st.divider()


    # --------------------------------------------------------
    # SUBMIT QUIZ
    # --------------------------------------------------------

    if st.button(
        "🚀 Submit Quiz",
        type="primary"
    ):

        score = 0

        # Check every answer
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


        # Percentage
        percentage = (
            score /
            len(questions)
        ) * 100


        # Save best score
        new_best = save_quiz_score(
            selected_language,
            score
        )


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.divider()

        st.header("🎉 Quiz Result")

        st.metric(
            "Your Score",
            f"{score}/{len(questions)}"
        )

        st.metric(
            "Percentage",
            f"{percentage:.0f}%"
        )


        if percentage == 100:

            st.balloons()

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

            best_score = st.session_state.progress[
                selected_language
            ]["quiz_score"]

            st.info(
                f"⭐ Best score: "
                f"{best_score}/{len(questions)}"
            )


# ============================================================
# PROGRESS PAGE
# ============================================================

elif page == "📊 Progress":

    st.title(
        "📊 Your Learning Progress"
    )

    st.subheader(
        f"🌐 {selected_language}"
    )

    data = st.session_state.progress[
        selected_language
    ]


    # --------------------------------------------------------
    # TOPICS
    # --------------------------------------------------------

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


    st.divider()


    # --------------------------------------------------------
    # LEARNING PROGRESS
    # --------------------------------------------------------

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
        f"{completed}/{len(topics)} topics completed "
        f"({progress_percentage:.0f}%)"
    )


    st.divider()


    # --------------------------------------------------------
    # QUIZ PROGRESS
    # --------------------------------------------------------

    st.subheader(
        "🧠 Quiz Performance"
    )


    questions = quiz_questions[
        selected_language
    ]


    best_score = data[
        "quiz_score"
    ]


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
            f"{quiz_percentage:.0f}%"
        )

    else:

        st.info(
            "Take the quiz to record "
            "your best score."
        )


    st.divider()


    st.caption(
        "💡 Progress is stored for the current "
        "Streamlit session."
    )
