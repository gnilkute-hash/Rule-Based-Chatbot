# Rule-Based Chatbot

A simple beginner-friendly chatbot built with Python. It responds to user messages using predefined `if-elif-else` rules and runs continuously until the user types `bye` or `exit`.

## Features

- Responds to common greetings and questions
- Converts user input to lowercase for case-insensitive matching
- Shows the current system time
- Shows today's date
- Displays a help menu
- Handles empty input and unexpected errors gracefully
- Uses Python's built-in `datetime` module

## Requirements

- Python 3.x

No external Python packages are required.

## How to Run

Open a terminal in this project folder and run:

```powershell
python rule_based_chatbot.py
```

If the `python` command does not work on Windows, run it with the full Python path:

```powershell
& "$env:LocalAppData\Programs\Python\Python313\python.exe" .\rule_based_chatbot.py
```

You can also run the default VS Code task with:

```text
Ctrl + Shift + B
```

## Supported Commands

| User Input | Bot Response |
| --- | --- |
| `hello` / `hi` | `Hello! How can I help you today?` |
| `how are you` | `I'm doing well, thank you!` |
| `what is your name` | `I'm RuleBot, your virtual assistant.` |
| `help` | Displays the list of supported commands |
| `time` | Displays the current system time |
| `date` | Displays today's date |
| `thank you` / `thanks` | `You're welcome!` |
| `bye` / `exit` | Ends the conversation |

## Sample Output

```text
Welcome to RuleBot!
Type 'help' to see available commands.
Type 'bye' or 'exit' to end the conversation.

You: hello
Bot: Hello! How can I help you today?

You: time
Bot: The current time is 20:44:48.

You: help
Bot: I can understand these commands:
- hello / hi
- how are you
- what is your name
- help
- time
- date
- thank you / thanks
- bye / exit

You: bye
Bot: Goodbye! Have a great day!
```

## Project Structure

```text
.
+-- rule_based_chatbot.py
+-- README.md
+-- LICENSE
+-- .vscode/
    +-- tasks.json
```

## Future Improvements

- Add more chatbot commands
- Use pattern matching or regular expressions
- Add fuzzy matching for spelling mistakes
- Add speech recognition
- Add text-to-speech responses
- Connect the chatbot to an AI or NLP model

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
