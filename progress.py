progress = {}


def initialize_progress(language):

    if language not in progress:

        progress[language] = {
            "greetings": False,
            "common_words": False,
            "daily_phrases": False,
            "numbers": False,
            "quiz_score": 0
        }


def mark_topic_completed(language, topic):

    initialize_progress(language)

    progress[language][topic] = True


def save_quiz_score(language, score):

    initialize_progress(language)

    if score > progress[language]["quiz_score"]:

        progress[language]["quiz_score"] = score


def show_progress(language):

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

    percentage = (
        completed / len(topics)
    ) * 100

    print("\n" + "=" * 50)

    print(f"{language.upper()} PROGRESS")

    print("=" * 50)

    for topic in topics:

        status = (
            "Completed"
            if data[topic]
            else "Not completed"
        )

        print(
            f"{topic.replace('_', ' ').title()}: {status}"
        )

    print("-" * 50)

    print(
        f"Learning Progress: {percentage:.0f}%"
    )

    print(
        f"Best Quiz Score: {data['quiz_score']}"
    )

    print("=" * 50)
