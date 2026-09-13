import streamlit as st

from languages import languages
from quiz import quiz_questions
from progress import (
    progress,
    initialize_progress,
    mark_topic_completed,
    save_quiz_score
)

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)

st.title("🇮🇳 Bharat Bhasha")
st.subheader("Learn Indian Languages Easily")

st.sidebar.title("📚 Menu")

page = st.sidebar.radio(
    "Choose an option:",
    ["Home", "Learn", "Quiz", "Progress"]
)

# ---------------- HOME ----------------

if page == "Home":

    st.header("Welcome to Bharat Bhasha! 🇮🇳")

    st.write(
        "Bharat Bhasha is a simple language-learning platform "
        "to help you learn different Indian languages."
    )

    st.success("Choose a section from the sidebar to start learning.")

    st.info(
        "Available languages: English, Hindi, Odia, Bengali, Punjabi, "
        "Telugu, Tamil, Marathi, Gujarati, Assamese, Bhojpuri and Haryanvi."
    )


# ---------------- LEARN ----------------

elif page == "Learn":

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

    st.subheader(topic.replace("_", " ").title())

    topic_data = topics[topic]

    if isinstance(topic_data, dict):

        for word, meaning in topic_data.items():

            st.write(f"### {word}")

            st.write(f"Meaning: **{meaning}**")

    elif isinstance(topic_data, list):

        for item in topic_data:
            st.write(f"• {item}")

    else:

        st.write(topic_data)

    if st.button("✅ Mark Topic as Completed"):

        mark_topic_completed(language, topic)

        st.success(
            f"{topic.replace('_', ' ').title()} completed!"
        )


# ---------------- QUIZ ----------------

elif page == "Quiz":

    st.header("🧠 Practice Quiz")

    language = st.selectbox(
        "Select a language:",
        list(quiz_questions.keys())
    )

    questions = quiz_questions[language]

    st.write(f"### {language} Quiz")

    with st.form("quiz_form"):

        answers = []

        for i, question in enumerate(questions):

            st.write(
                f"**Question {i + 1}: {question['question']}**"
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
            "Submit Quiz"
        )

    if submitted:

        score = 0

        for i, question in enumerate(questions):

            if answers[i] == question["answer"]:
                score += 1

        save_quiz_score(language, score)

        percentage = (score / len(questions)) * 100

        st.success(
            f"Your Score: {score}/{len(questions)}"
        )

        st.progress(percentage / 100)

        st.write(
            f"Percentage: **{percentage:.0f}%**"
        )

        if percentage == 100:
            st.balloons()
            st.success(
                "Excellent! You have mastered this quiz! 🎉"
            )

        elif percentage >= 60:
            st.info(
                "Good job! Keep practicing. 👍"
            )

        else:
            st.warning(
                "Keep learning and try again. 💪"
            )


# ---------------- PROGRESS ----------------

elif page == "Progress":

    st.header("📊 Learning Progress")

    language = st.selectbox(
        "Select a language:",
        list(languages.keys())
    )

    initialize_progress(language)

    data = progress[language]

    completed = 0

    topics = [
        "greetings",
        "common_words",
        "daily_phrases",
        "numbers"
    ]

    for topic in topics:

        if data[topic]:
            completed += 1
            st.success(
                f"✅ {topic.replace('_', ' ').title()} - Completed"
            )

        else:
            st.warning(
                f"⬜ {topic.replace('_', ' ').title()} - Not Completed"
            )

    percentage = (completed / len(topics)) * 100

    st.divider()

    st.subheader("Overall Progress")

    st.progress(percentage / 100)

    st.write(
        f"### {percentage:.0f}% Completed"
    )

    st.write(
        f"🏆 Best Quiz Score: **{data['quiz_score']}**"
    )
