# Bharat Bhasha
# Indian Language Learning Project - Streamlit App

import streamlit as st

from languages import languages
from quiz import quiz_questions
from progress import (
    initialize_progress,
    mark_topic_completed,
    save_quiz_score,
)


# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🇮🇳 Bharat Bhasha")
st.subheader("Indian Language Learning Platform")

st.write(
    "Learn Indian languages through vocabulary, phrases, "
    "numbers and interactive quizzes."
)

st.divider()


# -------------------------------------------------
# LANGUAGE SELECTION
# -------------------------------------------------

language_list = list(languages.keys())

language = st.selectbox(
    "🌐 Choose a Language",
    language_list
)

# Initialize progress
initialize_progress(language)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("📚 Bharat Bhasha")

page = st.sidebar.radio(
    "Choose Section",
    [
        "🏠 Home",
        "📖 Learn",
        "📝 Quiz",
        "📊 Progress"
    ]
)


# =================================================
# HOME
# =================================================

if page == "🏠 Home":

    st.header("Welcome to Bharat Bhasha 🇮🇳")

    st.write(
        "Bharat Bhasha is a simple language-learning project "
        "designed to help you practice different Indian languages."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Languages", len(languages))

    with col2:
        st.metric("Topics", 4)

    with col3:
        st.metric("Quiz Questions", "2 / Language")

    st.info(
        f"You have selected **{language}**. "
        "Go to the Learn section to start learning!"
    )


# =================================================
# LEARN
# =================================================

elif page == "📖 Learn":

    st.header(f"📖 Learn {language}")

    topics = list(languages[language].keys())

    topic = st.selectbox(
        "Choose a Topic",
        topics
    )

    st.subheader(topic.replace("_", " ").title())

    data = languages[language][topic]

    for english, translation in data.items():

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**English:** {english}")

        with col2:
            st.write(f"**{language}:** {translation}")

        st.divider()

    if st.button("✅ Mark Topic as Completed"):

        mark_topic_completed(language, topic)

        st.success(
            f"{topic.replace('_', ' ').title()} completed!"
        )


# =================================================
# QUIZ
# =================================================

elif page == "📝 Quiz":

    st.header(f"📝 {language} Practice Quiz")

    questions = quiz_questions.get(language, [])

    if not questions:

        st.warning("No quiz questions available for this language.")

    else:

        st.write(
            f"Test your knowledge of **{language}**."
        )

        # Create form so answers are submitted together
        with st.form("quiz_form"):

            answers = []

            for number, question in enumerate(questions, 1):

                st.subheader(f"Question {number}")

                st.write(question["question"])

                options = list(question["options"].keys())

                answer = st.radio(
                    "Choose your answer:",
                    options,
                    format_func=lambda x:
                        f"{x}. {question['options'][x]}",
                    key=f"question_{number}"
                )

                answers.append(answer)

                st.divider()

            submitted = st.form_submit_button(
                "🚀 Submit Quiz"
            )

        if submitted:

            score = 0

            for i, question in enumerate(questions):

                if answers[i] == question["answer"]:
                    score += 1

            percentage = (score / len(questions)) * 100

            # Save best score
            save_quiz_score(language, score)

            st.success(
                f"Quiz completed! Your score is "
                f"**{score}/{len(questions)}**"
            )

            st.progress(
                percentage / 100
            )

            st.write(
                f"### Score: {percentage:.0f}%"
            )

            if percentage == 100:

                st.balloons()

                st.success(
                    "🎉 Excellent! You have mastered this quiz."
                )

            elif percentage >= 60:

                st.info(
                    "👍 Good job! Keep practicing."
                )

            else:

                st.warning(
                    "📚 Keep learning and try the quiz again."
                )


# =================================================
# PROGRESS
# =================================================

elif page == "📊 Progress":

    st.header(f"📊 {language} Progress")

    data = initialize_progress(language)

    # Get the progress dictionary
    from progress import progress

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

            st.success(
                f"✅ {topic.replace('_', ' ').title()} - Completed"
            )

            completed += 1

        else:

            st.warning(
                f"⭕ {topic.replace('_', ' ').title()} - Not completed"
            )

    percentage = (completed / len(topics)) * 100

    st.divider()

    st.subheader("Learning Progress")

    st.progress(
        percentage / 100
    )

    st.write(
        f"**{percentage:.0f}% completed**"
    )

    st.divider()

    st.subheader("🏆 Best Quiz Score")

    st.write(
        f"**{data['quiz_score']} / 2**"
    )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "🇮🇳 Bharat Bhasha | Indian Language Learning Project"
)
