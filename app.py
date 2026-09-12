# Bharat Bhasha
# Indian Language Learning Project

print("=" * 50)
print("              BHARAT BHASHA")
print("       Learn Indian Languages")
print("=" * 50)

languages = {
    1: "English",
    2: "Hindi",
    3: "Odia",
    4: "Bengali",
    5: "Punjabi",
    6: "Telugu",
    7: "Tamil",
    8: "Marathi",
    9: "Gujarati",
    10: "Assamese",
    11: "Bhojpuri",
    12: "Haryanvi"
}

print("\nChoose a language to learn:\n")

for number, language in languages.items():
    print(f"{number}. {language}")

try:
    choice = int(input("\nEnter your choice: "))

    if choice in languages:

        selected_language = languages[choice]

        print("\n" + "=" * 50)
        print(f"You selected: {selected_language}")
        print("=" * 50)

        print("\nWhat would you like to learn?")
        print("1. Greetings")
        print("2. Common Words")
        print("3. Daily Phrases")
        print("4. Numbers")
        print("5. Practice Quiz")
        print("6. Exit")

        topic = int(input("\nEnter your choice: "))

        if topic == 1:
            print("\n--- Greetings ---")
            print("Hello")
            print("Good Morning")
            print("How are you?")
            print("Thank you")

        elif topic == 2:
            print("\n--- Common Words ---")
            print("Yes")
            print("No")
            print("Water")
            print("Food")
            print("Friend")

        elif topic == 3:
            print("\n--- Daily Phrases ---")
            print("What is your name?")
            print("Where are you going?")
            print("I am fine")
            print("See you tomorrow")

        elif topic == 4:
            print("\n--- Numbers ---")
            print("1 - One")
            print("2 - Two")
            print("3 - Three")
            print("4 - Four")
            print("5 - Five")

        elif topic == 5:
            print("\n--- Practice Quiz ---")
            print("Quiz feature will be added soon!")

        elif topic == 6:
            print("\nThank you for using Bharat Bhasha!")

        else:
            print("\nInvalid topic choice.")

    else:
        print("\nInvalid language choice.")

except ValueError:
    print("\nPlease enter a valid number.")

print("\n" + "=" * 50)
print("Thank you for using Bharat Bhasha!")
print("=" * 50)
