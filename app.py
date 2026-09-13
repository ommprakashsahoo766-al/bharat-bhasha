elif page == "Quiz":

    st.header("🧠 Language Quiz")

    language = st.selectbox(
        "Select a language:",
        list(quiz_questions.keys()),
        key="quiz_language"
    )

    questions = quiz_questions[language]

    if len(questions) == 0:
        st.error("No quiz questions available for this language.")

    else:
        st.write(f"### 🇮🇳 {language} Quiz")
        st.info(f"Test your knowledge with {len(questions)} questions!")

        # Create a unique result key for each language
        result_key = f"quiz_result_{language}"

        # Quiz form
        with st.form(f"quiz_form_{language}"):

            answers = []

            for i, question in enumerate(questions):

                st.write(
                    f"**Question {i + 1}/{len(questions)}**"
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

        # When user submits
        if submitted:

            score = 0

            for i, question in enumerate(questions):

                if answers[i] == question["answer"]:
                    score += 1

            # Save best score
            save_quiz_score(language, score)

            percentage = (score / len(questions)) * 100

            # Save result
            st.session_state[result_key] = {
                "score": score,
                "percentage": percentage,
                "answers": answers,
                "questions": questions
            }

        # Show result if quiz has been submitted
        if result_key in st.session_state:

            result = st.session_state[result_key]

            score = result["score"]
            percentage = result["percentage"]

            st.divider()

            st.header("🏆 Quiz Result")

            # Score
            st.success(
                f"Your Score: {score}/{len(questions)}"
            )

            st.progress(percentage / 100)

            st.write(
                f"### 📊 Percentage: {percentage:.0f}%"
            )

            # Performance message
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

            # Answer review
            st.divider()

            st.header("📝 Answer Review")

            for i, question in enumerate(result["questions"]):

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

            # Best score
            initialize_progress(language)

            best_score = progress[language]["quiz_score"]

            st.write(
                f"🏅 **Best Score:** {best_score}/{len(questions)}"
            )

            # Try again
            if st.button(
                "🔄 Try Again",
                key=f"retry_{language}"
            ):

                del st.session_state[result_key]

                st.rerun()
