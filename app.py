```python
# Bharat Bhasha
# Indian Language Learning Project

print("=" * 45)
print("             BHARAT BHASHA")
print("       Learn Indian Languages")
print("=" * 45)

languages = {
    1: "Hindi",
    2: "Odia",
    3: "Bengali",
    4: "Punjabi",
    5: "Telugu",
    6: "Tamil",
    7: "Marathi",
    8: "Gujarati",
    9: "Assamese",
    10: "Bhojpuri",
    11: "Haryanvi"
}

print("\nChoose a language:\n")

for number, language in languages.items():
    print(f"{number}. {language}")

try:
    choice = int(input("\nEnter your choice: "))

    if choice in languages:
        selected_language = languages[choice]

        print("\n" + "=" * 45)
        print(f"You selected: {selected_language}")
        print("=" * 45)

        print("\nWhat would you like to learn?")
        print("1. Basic Words")
        print("2. Greetings")
        print("3. Daily Phrases")
        print("4. Numbers")

        topic = int(input("\nEnter your choice: "))

        if topic == 1:
            print("\nBasic Words:")
            print("Hello")
            print("Thank You")
            print("Yes")
            print("No")
            print("Water")
            print("Food")

        elif topic == 2:
            print("\nGreetings:")
            print("Hello!")
            print("Good Morning!")
            print("Good Evening!")
            print("How are you?")

        elif topic == 3:
            print("\nDaily Phrases:")
            print("What is your name?")
            print("Where are you going?")
            print("I am fine.")
            print("See you tomorrow.")

        elif topic == 4:
            print("\nNumbers:")
            print("1 - One")
            print("2 - Two")
            print("3 - Three")
            print("4 - Four")
            print("5 - Five")

        else:
            print("\nInvalid topic choice.")

    else:
        print("\nInvalid language choice.")

except ValueError:
    print("\nPlease enter a valid number.")

print("\nThank you for using Bharat Bhasha!")
```

