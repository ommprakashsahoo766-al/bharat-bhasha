```python
# Bharat Bhasha
# Language Practice Quiz


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

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {question['answer']}")

    print("\n" + "=" * 50)
    print("              QUIZ RESULT")
    print("=" * 50)

    print(f"Language: {language}")
    print(f"Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100

    print(f"Percentage: {percentage:.0f}%")

    if percentage == 100:
        print("Excellent! You have mastered this quiz.")
    elif percentage >= 60:
        print("Good job! Keep practicing.")
    else:
        print("Keep learning and try the quiz again.")

    print("=" * 50)
```
