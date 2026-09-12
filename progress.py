# Bharat Bhasha
# Progress Tracking System


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
    total_topics = 4

    print("\n" + "=" * 50)
    print(f"        {language.upper()} PROGRESS")
    print("=" * 50)

    print(
        f"Greetings       : "
        f"{'Completed' if data['greetings'] else 'Not completed'}"
    )

    print(
        f"Common Words    : "
        f"{'Completed' if data['common_words'] else 'Not completed'}"
    )

    print(
        f"Daily Phrases   : "
        f"{'Completed' if data['daily_phrases'] else 'Not completed'}"
    )

    print(
        f"Numbers         : "
        f"{'Completed' if data['numbers'] else 'Not completed'}"
    )

    for topic in ["greetings", "common_words", "daily_phrases", "numbers"]:
        if data[topic]:
            completed += 1

    percentage = (completed / total_topics) * 100

    print("-" * 50)
    print(f"Learning Progress: {percentage:.0f}%")
    print(f"Best Quiz Score : {data['quiz_score']}")

    print("=" * 50)
