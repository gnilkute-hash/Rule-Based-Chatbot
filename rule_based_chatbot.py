from datetime import datetime


def normalize_input(user_input):
    """Clean user input so matching is case-insensitive and simple."""
    return user_input.strip().lower()


def get_help_message():
    """Return a list of commands the chatbot understands."""
    return (
        "I can understand these commands:\n"
        "- hello / hi\n"
        "- how are you\n"
        "- what is your name\n"
        "- help\n"
        "- time\n"
        "- date\n"
        "- thank you / thanks\n"
        "- bye / exit"
    )


def get_current_time():
    """Return the current system time in hours, minutes, and seconds."""
    return datetime.now().strftime("%H:%M:%S")


def get_current_date():
    """Return today's system date in day-month-year format."""
    return datetime.now().strftime("%d-%m-%Y")


def get_bot_response(user_input):
    """Choose the correct chatbot response using if-elif-else rules."""
    message = normalize_input(user_input)

    if message == "hello" or message == "hi":
        return "Hello! How can I help you today?"

    elif message == "how are you":
        return "I'm doing well, thank you!"

    elif message == "what is your name":
        return "I'm RuleBot, your virtual assistant."

    elif message == "help":
        return get_help_message()

    elif message == "time":
        return f"The current time is {get_current_time()}."

    elif message == "date":
        return f"Today's date is {get_current_date()}."

    elif message == "thank you" or message == "thanks":
        return "You're welcome!"

    elif message == "bye" or message == "exit":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Please try another question."


def chat():
    """Run the main chatbot loop until the user chooses to exit."""
    print("Welcome to RuleBot!")
    print("Type 'help' to see available commands.")
    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ")

            # Input validation: do not process empty messages.
            if not user_input.strip():
                print("Bot: Please enter a message.")
                continue

            response = get_bot_response(user_input)
            print("Bot:", response)

            if normalize_input(user_input) == "bye" or normalize_input(user_input) == "exit":
                break

        except KeyboardInterrupt:
            print("\nBot: Chat interrupted. Goodbye!")
            break

        except Exception as error:
            print(f"Bot: An unexpected error occurred: {error}")
            print("Bot: Please try again.")


if __name__ == "__main__":
    chat()
