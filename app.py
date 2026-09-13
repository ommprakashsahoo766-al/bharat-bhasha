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


# =========================
# HOME
# =========================

if page == "Home":

    st.header("Welcome to Bharat Bhasha! 🇮🇳")

    st.write(
        "Bharat Bhasha is an Indian language learning platform "
        "designed to help you learn different Indian languages "
        "in a simple and interactive way."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🇮🇳 Languages", len(languages))

    with col2:
        st.metric("📚 Learning Topics", "4")

    with col3:
        st.metric("🧠 Quiz Questions", "10")

    st.divider()

    st.header("🌐 Available Languages")

    for language in languages.keys():
        st.write(f"• **{language}**")

    st.divider()

    st.info("💡 Choose **Learn** from the sidebar to start learning!")


# =========================
# LEARN
# =========================

elif page == "Learn":

    st.header("📖 Learn a Language")

    language = st.selectbox(
        "🌐 Select a language:",
        list(languages.keys()),
        key="learn_language"
    )

    topics = languages[language]
    topic_names = list(topics.keys())

    st.divider()

    st.subheader("📚 Choose a Topic")

    topic = st.selectbox(
        "Select a topic to learn:",
        topic_names,
        format_func=lambda x: f"📘 {x.replace('_', ' ').title()}",
        key="learn_topic"
    )

    initialize_progress(language)

    completed = progress[language][topic]

    st.divider()

    st.header(
        f"📘 {topic.replace('_', ' ').title()}"
    )

    if completed:

        st.success(
            "✅ You have already completed this topic!"
        )

    else:

        st.info(
            "📖 Study the words below and then mark this topic as completed."
        )

    st.divider()

    data = topics[topic]

    for word, meaning in data.items():

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"### 🗣️ {word}")

        with col2:
            st.markdown(f"### ➡️ {meaning}")

        st.divider()

    if not completed:

        if st.button(
            "✅ Mark Topic as Completed",
            key=f"complete_{language}_{topic}"
        ):

            mark_topic_completed(
                language,
                topic
            )

            st.success(
                f"🎉 {topic.replace('_', ' ').title()} "
                f"completed for {language}!"
            )

            st.rerun()

    else:

        st.success("🏆 Topic Completed!")

    st.divider()

    st.subheader("📊 Your Learning Progress")

    completed_topics = 0

    for topic_name in topic_names:

        if progress[language][topic_name]:
            completed_topics += 1

    total_topics = len(topic_names)

    topic_progress = (
        completed_topics / total_topics
    ) * 100

    st.progress(topic_progress / 100)

    st.write(
        f"**{completed_topics}/{total_topics} topics completed**"
    )

    st.write(
        f"Progress: **{topic_progress:.0f}%**"
    )


# =========================
# QUIZ
# =========================

elif page == "Quiz":

    st.header("🧠 Language Quiz")

    language = st.selectbox(
        "Select a language:",
        list(quiz_questions.keys()),
        key="quiz_language"
    )

    questions = quiz_questions[language]

    if len(questions) == 0:

        st.error(
            "❌ No quiz questions available for this language."
        )

    else:

        st.write(f"### 🇮🇳 {language} Quiz")

        st.info(
            f"Test your knowledge with **{len(questions)} questions!**"
        )

        result_key = f"quiz_result_{language}"

        with st.form(f"quiz_form_{language}"):

            answers = []

            for i, question in enumerate(questions):

                st.write(
                    f"### Question {i + 1}/{len(questions)}"
                )

                st.write(question["question"])

                options = question["options"]

                selected = st.radio(
                    "Choose your answer:",
                    list(options.keys()),
                    format_func=lambda x: f"{x}. {options[x]}",
                    key=f"quiz_{language}_{i}"
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

            save_quiz_score(language, score)

            percentage = (
                score / len(questions)
            ) * 100

            st.session_state[result_key] = {
                "score": score,
                "percentage": percentage,
                "answers": answers,
                "questions": questions
            }

        if result_key in st.session_state:

            result = st.session_state[result_key]

            score = result["score"]
            percentage = result["percentage"]

            st.divider()

            st.header("🏆 Quiz Result")

            st.success(
                f"Your Score: {score}/{len(questions)}"
            )

            st.progress(percentage / 100)

            st.write(
                f"### 📊 Percentage: {percentage:.0f}%"
            )

            if percentage == 100:

                st.balloons()

                st.success(
                    "🎉 Perfect Score! You have mastered this quiz!"
                )

            elif percentage >= 80:

                st.success(
                    "🔥 Excellent! Your language knowledge is very strong!"
                )

            elif percentage >= 60:

                st.info(
                    "👍 Good job! Keep practicing to improve."
                )

            else:

                st.warning(
                    "💪 Keep learning! Try the quiz again."
                )

            st.divider()

            st.header("📝 Answer Review")

            for i, question in enumerate(
                result["questions"]
            ):

                user_answer = result["answers"][i]
                correct_answer = question["answer"]

                user_text = question["options"][user_answer]
                correct_text = question["options"][correct_answer]

                if user_answer == correct_answer:

                    st.success(
                        f"✅ Question {i + 1}: Correct!"
                    )

                    st.write(
                        f"Your answer: **{user_answer}. {user_text}**"
                    )

                else:

                    st.error(
                        f"❌ Question {i + 1}: Incorrect"
                    )

                    st.write(
                        f"Your answer: **{user_answer}. {user_text}**"
                    )

                    st.write(
                        f"Correct answer: **{correct_answer}. {correct_text}**"
                    )

                st.divider()

            initialize_progress(language)

            best_score = progress[language]["quiz_score"]

            st.write(
                f"🏅 **Best Score:** "
                f"{best_score}/{len(questions)}"
            )

            if st.button(
                "🔄 Try Again",
                key=f"retry_{language}"
            ):

                del st.session_state[result_key]

                st.rerun()


# =========================
# PROGRESS
# =========================

elif page == "Progress":

    st.header("📊 Your Progress")

    language = st.selectbox(
        "Select a language:",
        list(languages.keys()),
        key="progress_language"
    )

    initialize_progress(language)

    data = progress[language]

    st.divider()

    st.subheader(
        f"📚 {language} Progress"
    )

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
                f"✅ {topic.replace('_', ' ').title()} — Completed"
            )

            completed += 1

        else:

            st.warning(
                f"⬜ {topic.replace('_', ' ').title()} — Not Completed"
            )

    topic_percentage = (
        completed / len(topics)
    ) * 100

    st.divider()

    st.subheader("📈 Learning Progress")

    st.progress(
        topic_percentage / 100
    )

    st.write(
        f"**{completed}/{len(topics)} topics completed**"
    )

    st.write(
        f"Progress: **{topic_percentage:.0f}%**"
    )

    st.divider()

    st.subheader("🧠 Quiz Performance")

    best_score = data["quiz_score"]

    st.metric(
        "🏅 Best Quiz Score",
        f"{best_score}/10"
    )

    if best_score == 10:

        st.success(
            "🎉 Amazing! You achieved a perfect quiz score!"
        )

    elif best_score >= 8:

        st.info(
            "🔥 Excellent quiz performance!"
        )

    elif best_score >= 5:

        st.info(
            "👍 Good progress. Keep practicing!"
        )

    else:

        st.warning(
            "💪 Complete some quizzes to improve your score!"
        )
