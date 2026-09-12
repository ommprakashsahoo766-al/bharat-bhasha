```python
# Bharat Bhasha
# Indian Language Learning Project

from languages import languages


def show_topic(language, topic):
    data = languages[language][topic]

    print("\n" + "=" * 50)
    print(f"{topic.upper()} - {language}")
    print("=" * 50)

    for english, translation in data.items():
        print(f"{english}  →  {translation}")


print("=" * 50)
print("              BHARAT BHASHA")
print("       Learn Indian Languages")
print("=" * 50)

language_list = list(languages.keys())

while True:

    print("\nChoose a language to learn:\n")

    for i, language in enumerate(language_list, 1):
        print(f"{i}. {language}")

    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 0:
            print("\nThank you for using Bharat Bhasha!")
            break

        if choice < 1 or choice > len(language_list):
            print("\nInvalid language choice.")
            continue

        selected_language = language_list[choice - 1]

        print("\n" + "=" * 50)
        print(f"You selected: {selected_language}")
        print("=" * 50)

        while True:

            print("\nWhat would you like to learn?")
            print("1. Greetings")
            print("2. Common Words")
            print("3. Daily Phrases")
            print("4. Numbers")
            print("5. Back to Language Menu")

            topic_choice = input("\nEnter your choice: ")

            if topic_choice == "1":
                show_topic(selected_language, "greetings")

            elif topic_choice == "2":
                show_topic(selected_language, "common_words")

            elif topic_choice == "3":
                show_topic(selected_language, "daily_phrases")

            elif topic_choice == "4":
                show_topic(selected_language, "numbers")

            elif topic_choice == "5":
                break

            else:
                print("\nInvalid topic choice.")

    except ValueError:
        print("\nPlease enter a valid number.")
```
