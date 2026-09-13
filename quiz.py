# Bharat Bhasha
# Automatic Quiz System

from languages import languages
import random


def create_questions(language_data, language_name):
    """
    Create quiz questions automatically from languages.py
    """

    vocabulary = []

    # Collect words and meanings from all topics
    for topic, data in language_data.items():

        if isinstance(data, dict):

            for word, meaning in data.items():
                vocabulary.append((str(word), str(meaning)))

    questions = []

    # Need at least some vocabulary
    if len(vocabulary) < 4:
        return questions

    # Create up to 10 questions
    selected = vocabulary[:10]

    for word, correct_answer in selected:

        # Get possible wrong answers
        wrong_answers = []

        for other_word, other_meaning in vocabulary:
            if other_meaning != correct_answer:
                wrong_answers.append(other_meaning)

        # Remove duplicate answers
        wrong_answers = list(set(wrong_answers))

        # Need 3 wrong answers
        if len(wrong_answers) >= 3:

            wrong_options = random.sample(wrong_answers, 3)

            options = wrong_options + [correct_answer]

            random.shuffle(options)

            # Find correct option letter
            letters = ["A", "B", "C", "D"]

            answer_letter = letters[options.index(correct_answer)]

            questions.append({
                "question": f"What does '{word}' mean in {language_name}?",
                "options": {
                    "A": options[0],
                    "B": options[1],
                    "C": options[2],
                    "D": options[3]
                },
                "answer": answer_letter
            })

    return questions


# Create quiz questions for every language
quiz_questions = {}

for language_name, language_data in languages.items():

    questions = create_questions(
        language_data,
        language_name
    )

    quiz_questions[language_name] = questions[:10]


# Console quiz
def start_quiz(language, questions):

    print("\n" + "=" * 50)
    print(f"          {language} PRACTICE QUIZ")
    print("=" * 50)

    score = 0

    for number, question in enumerate(questions, 1):

        print(f"\nQuestion {number}")
        print(question["question"])

        for key, option in question["options"].items():
            print(f"{key}. {option}")

        answer = input(
            "Enter your answer (A/B/C/D): "
        ).upper()

        if answer == question["answer"]:

            print("Correct! ✅")
            score += 1

        else:

            correct = question["options"][
                question["answer"]
            ]

            print(
                f"Wrong! ❌ Correct answer: {correct}"
            )

    print("\n" + "=" * 50)
    print("              QUIZ RESULT")
    print("=" * 50)

    print(f"Language: {language}")
    print(f"Score: {score}/{len(questions)}")

    if len(questions) > 0:

        percentage = (
            score / len(questions)
        ) * 100

        print(
            f"Percentage: {percentage:.0f}%"
        )

        if percentage == 100:

            print(
                "Excellent! You have mastered this quiz! 🏆"
            )

        elif percentage >= 60:

            print(
                "Good job! Keep practicing! 👍"
            )

        else:

            print(
                "Keep learning and try again! 💪"
            )

    print("=" * 50)

    return score
