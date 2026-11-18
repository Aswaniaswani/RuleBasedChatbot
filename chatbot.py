import re
import random

# Chatbot responses

responses = {
    "greeting": [
        "Hello! Welcome. What can I do for you today?",
        "Hey! It's nice to see you here.",
        "Hi! How is your day going?",
        "Good to see you! Let's have a conversation."
    ],

    "introduction": [
        "I'm PyBot, your virtual assistant. Nice to meet you!",
        "I'm a Python-based chatbot designed to answer simple questions.",
        "You can call me PyBot. I'm here to make your day easier!",
        "I'm a friendly chatbot who enjoys helping people."
    ],

    "python": [
        "Python is a versatile language used by developers around the world.",
        "You can use Python to build websites, automate tasks and create AI applications.",
        "Python has simple syntax, which makes it a great language for beginners.",
        "Python is one of the most popular languages in the technology industry."
    ],

    "thanks": [
        "It's my pleasure to help you!",
        "You're very welcome! Feel free to ask me anything.",
        "Glad I could help!",
        "Anytime! I'm always happy to assist."
    ],

    "goodbye": [
        "It was lovely chatting with you. See you soon!",
        "Take care and have a wonderful day!",
        "Thanks for chatting with me. Goodbye!",
        "Until next time! Have a great day."
    ]
}


# Keyword mapping
keywords = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "introduction": ["who are you", "your name", "introduce yourself"],
    "python": ["python", "programming", "coding"],
    "thanks": ["thank you", "thanks"],
    "goodbye": ["bye", "goodbye", "see you", "exit"]
}


# Intent recognition
def recognize_intent(user_input):

    user_input = user_input.lower()

    for intent, words in keywords.items():

        for word in words:

            pattern = r"\b" + re.escape(word) + r"\b"

            if re.search(pattern, user_input):
                return intent

    return "unknown"


# Generate chatbot response
def chatbot_response(user_input):

    intent = recognize_intent(user_input)

    if intent == "unknown":
        return "Sorry, I don't understand. Can you ask something else?"

    return random.choice(responses[intent])


# Main chatbot
def start_chatbot():

    print("================================")
    print("       WELCOME TO PYBOT")
    print("================================")
    print("Type 'bye' to exit the chatbot.")

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("PyBot: Please enter a message.")
            continue

        response = chatbot_response(user_input)

        print("PyBot:", response)

        if recognize_intent(user_input) == "goodbye":
            break


# Run chatbot
if __name__ == "__main__":
    start_chatbot()
