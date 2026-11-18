# Rule-Based Chatbot – PyBot

## Project Description

This project is a simple conversational chatbot developed using Python. It accepts a user's message, checks the message for predefined keywords, identifies the corresponding intent, and returns a suitable response.

The project uses regular expressions for keyword matching and the random module to select from multiple predefined responses. A Graphical User Interface (GUI) is also provided using Tkinter, allowing users to chat through a window instead of only using the command line.

The project demonstrates basic chatbot development, intent recognition, keyword mapping, response generation, and GUI development.

## Features

- Greeting recognition
- Self-introduction
- Python-related conversations
- Thank-you responses
- Goodbye responses
- Fallback responses for unknown questions
- Simple graphical user interface using Tkinter

## System Workflow

The chatbot follows the workflow given below:

**User Input → Keyword Mapping → Intent Recognition → Response Generation → Display Output**

**Step 1 – User Input:** The user enters a message through the terminal or the Tkinter input field.

**Step 2 – Keyword Mapping:** The program stores predefined keywords and phrases under different intent categories, such as greeting, introduction, Python, thanks, and goodbye.

**Step 3 – Intent Recognition:** The `recognize_intent()` function converts the user's message into lowercase and checks for predefined keywords using regular expressions. It identifies the matching intent. If no keyword matches, it returns "unknown".

**Step 4 – Response Generation:** The `chatbot_response()` function generates a suitable response based on the identified intent. For a recognized intent, `random.choice()` selects one response from the available response list. If the intent is unknown, the chatbot returns a default message.

**Step 5 – Display Output:** Finally, the chatbot displays the generated response to the user through the terminal or the Tkinter graphical interface.

## Technologies Used

- Python
- Regular Expressions (Regex)
- Tkinter
- Random Module
- Basic NLP Concepts

## Project Structure

```text
RuleBasedChatbot/
│
├── README.md
├── chatbot.py
└── gui.py
```

## How to Run

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command to start the chatbot:

   `python chatbot.py`

5. To launch the graphical interface, run:

   `python gui.py`

6. Start chatting with PyBot!

## Conclusion

This project demonstrates basic chatbot development, intent recognition, keyword mapping, and response generation using Python. It also provides practical experience in developing a simple graphical user interface using Tkinter.
