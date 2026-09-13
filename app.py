import streamlit as st

from languages import languages
from quiz import quiz_questions

from progress import (
    progress,
    initialize_progress,
    mark_topic_completed,
    save_quiz_score
)


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Bharat Bhasha",
    page_icon="🇮🇳",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🇮🇳 Bharat Bhasha")
st.subheader("Learn Indian Languages Easily")


# --------------------------------------------------
# SIDEBAR MENU
# --------------------------------------------------

st.sidebar.title("📚 Menu")

page = st.sidebar.radio(
    "Choose an option:",
    [
        "Home",
        "Learn",
        "Quiz",
        "Progress"
    ]
)


# ==================================================
# HOME PAGE
# ==================================================

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
        st.metric(
            "🇮🇳 Languages",
            len(languages)
        )

    with col2:
        st.metric(
            "📚 Learning Topics",
            "4"
        )

    with col3:
        st.metric(
            "🧠 Quiz Questions",
            "10"
        )

    st.divider()

    st.header("🌐 Available Languages")

    language_names = list(languages.keys())

    for language in language_names:

        st.write(f"• **{language}**")

    st.divider()

    st.info(
        "💡 Choose **Learn** from the sidebar to start learning!"
    )


# ==================================================
# LEARN PAGE
# ==================================================

elif page == "Learn":

    st.header("📖 Learn a Language")

    # Select language
    language = st.selectbox(
        "Select a language:",
        list(languages.keys()),
        key="learn_language"
    )

    # Get topics
    topics = languages[language]

    topic_names = list(topics.keys())

    # Select topic
    topic = st.selectbox(
        "Select a topic:",
        topic_names,
        key="learn_topic"
    )

    st.divider()

    st.header(
        f"📚 {topic.replace('_', ' ').title()}"
    )

    data = topics[topic]

    # Display vocabulary
    for word, meaning in data.items():

        st.write(
            f"**{word}** → {meaning}"
        )

    st.divider()

    # Mark topic completed
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


# ==================================================
# QUIZ PAGE
# ==================================================

elif page == "Quiz":

    st.header("🧠 Language Quiz")

    # Select language
    language = st.selectbox(
        "Select a language:",
        list(quiz_questions.keys()),
        key="quiz_language"
    )

    questions = quiz_questions[language]

    # Check whether questions exist
    if len(questions) == 0:

        st.error(
            "❌ No quiz questions available for this language."
        )

    else:

        st.write(
            f"### 🇮🇳 {language} Quiz"
        )

        st.info(
            f"Test your knowledge with "
            f"**{len(questions)} questions!**"
        )

        # Unique result key
        result_key = f"quiz_result_{language}"

        # --------------------------------------------------
        # QUIZ FORM
        # --------------------------------------------------

        with st.form(
            f"quiz_form_{language}"
        ):

            answers = []

            for i, question in enumerate(questions):

                st.write(
                    f"### Question {i + 1}/{len(questions)}"
                )

                st.write(
                    question["question"]
                )

                options = question["options"]

                selected = st.radio(
                    "Choose your answer:",
                    list(options.keys()),

                    format_func=lambda x:
                    f"{x}. {options[x]}",

                    key=f"quiz_{language}_{i}"
                )

                answers.append(selected)

                st.divider()

            # Submit button
            submitted = st.form_submit_button(
                "🚀 Submit Quiz"
            )


        # --------------------------------------------------
        # CALCULATE RESULT
        # --------------------------------------------------

        if submitted:

            score = 0

            for i, question in enumerate(questions):

                if answers[i] == question["answer"]:

                    score += 1

            # Save best score
            save_quiz_score(
                language,
                score
            )

            # Calculate percentage
            percentage = (
                score / len(questions)
            ) * 100

            # Store result in session
            st.session_state[result_key] = {

                "score": score,

                "percentage": percentage,

                "answers": answers,

                "questions": questions
            }


        # --------------------------------------------------
        # SHOW RESULT
        # --------------------------------------------------

        if result_key in st.session_state:

            result = st.session_state[result_key]

            score = result["score"]

            percentage = result["percentage"]

            st.divider()

            st.header("🏆 Quiz Result")

            # Score
            st.success(
                f"Your Score: "
                f"{score}/{len(questions)}"
            )

            # Progress bar
            st.progress(
                percentage / 100
            )

            st.write(
                f"### 📊 Percentage: "
                f"{percentage:.0f}%"
            )


            # --------------------------------------------------
            # PERFORMANCE MESSAGE
            # --------------------------------------------------

            if percentage == 100:

                st.balloons()

                st.success(
                    "🎉 Perfect Score! "
                    "You have mastered this quiz!"
                )

            elif percentage >= 80:

                st.success(
                    "🔥 Excellent! "
                    "Your language knowledge is very strong!"
                )

            elif percentage >= 60:

                st.info(
                    "👍 Good job! "
                    "Keep practicing to improve."
                )

            else:

                st.warning(
                    "💪 Keep learning! "
                    "Try the quiz again."
                )


            # --------------------------------------------------
            # ANSWER REVIEW
            # --------------------------------------------------

            st.divider()

            st.header("📝 Answer Review")

            for i, question in enumerate(
                result["questions"]
            ):

                user_answer = result["answers"][i]

                correct_answer = question["answer"]

                user_text = question["options"][
                    user_answer
                ]

                correct_text = question["options"][
                    correct_answer
                ]


                # Correct answer
                if user_answer == correct_answer:

                    st.success(
                        f"✅ Question {i + 1}: Correct!"
                    )

                    st.write(
                        f"Your answer: "
                        f"**{user_answer}. {user_text}**"
                    )


                # Wrong answer
                else:

                    st.error(
                        f"❌ Question {i + 1}: Incorrect"
                    )

                    st.write(
                        f"Your answer: "
                        f"**{user_answer}. {user_text}**"
                    )

                    st.write(
                        f"Correct answer: "
                        f"**{correct_answer}. "
                        f"{correct_text}**"
                    )

                st.divider()


            # --------------------------------------------------
            # BEST SCORE
            # --------------------------------------------------

            initialize_progress(
                language
            )

            best_score = progress[language][
                "quiz_score"
            ]

            st.write(
                f"🏅 **Best Score:** "
                f"{best_score}/{len(questions)}"
            )


            # --------------------------------------------------
            # TRY AGAIN
            # --------------------------------------------------

            if st.button(
                "🔄 Try Again",
                key=f"retry_{language}"
            ):

                del st.session_state[result_key]

                st.rerun()


# ==================================================
# PROGRESS PAGE
# ==================================================

elif page == "Progress":

    st.header("📊 Your Progress")

    # Select language
    language = st.selectbox(
        "Select a language:",
        list(languages.keys()),
        key="progress_language"
    )

    # Initialize progress
    initialize_progress(language)

    data = progress[language]

    st.divider()

    st.subheader(
        f"📚 {language} Progress"
    )


    # --------------------------------------------------
    # TOPIC PROGRESS
    # --------------------------------------------------

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


    # --------------------------------------------------
    # PROGRESS BAR
    # --------------------------------------------------

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


    # --------------------------------------------------
    # QUIZ SCORE
    # --------------------------------------------------

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
