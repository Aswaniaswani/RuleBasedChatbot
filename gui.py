import tkinter as tk
from chatbot import chatbot_response

# Main window
root = tk.Tk()
root.title("PyBot - AI Chatbot")
root.geometry("550x550")
root.configure(bg="#F4F7FC")
root.resizable(False, False)

# Header
header = tk.Frame(root, bg="#B8D4F5", height=70)
header.pack(fill="x")
header.pack_propagate(False)

title = tk.Label(
    header,
    text="🤖 PyBot Chatbot",
    font=("Arial", 20, "bold"),
    bg="#B8D4F5",
    fg="#23395D"
)
title.pack(pady=17)


# Bottom input section
input_frame = tk.Frame(root, bg="#F4F7FC")
input_frame.pack(side="bottom", fill="x", padx=15, pady=10)

message_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    bd=1,
    relief="solid"
)
message_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)


# Chat display area
chat_frame = tk.Frame(root, bg="#F4F7FC")
chat_frame.pack(
    side="top",
    fill="both",
    expand=True,
    padx=15,
    pady=15
)

chat_area = tk.Text(
    chat_frame,
    font=("Arial", 11),
    bg="white",
    fg="#333333",
    wrap="word",
    state="disabled",
    bd=0,
    padx=12,
    pady=12
)
chat_area.pack(fill="both", expand=True)


# Display messages
def display_message(sender, message):

    chat_area.config(state="normal")

    if sender == "You":
        chat_area.insert(
            "end",
            f"\nYou: {message}\n",
            "user"
        )
    else:
        chat_area.insert(
            "end",
            f"\nPyBot: {message}\n",
            "bot"
        )

    chat_area.config(state="disabled")
    chat_area.see("end")


# Message styles
chat_area.tag_config(
    "user",
    foreground="#246B45",
    font=("Arial", 11, "bold"),
    justify="right"
)

chat_area.tag_config(
    "bot",
    foreground="#294C7A",
    font=("Arial", 11)
)


# Send message
def send_message(event=None):

    user_message = message_entry.get().strip()

    if not user_message:
        return

    display_message("You", user_message)

    message_entry.delete(0, "end")

    response = chatbot_response(user_message)

    root.after(
        300,
        lambda: display_message("PyBot", response)
    )


# Clear chat
def clear_chat():

    chat_area.config(state="normal")
    chat_area.delete("1.0", "end")
    chat_area.config(state="disabled")

    display_message(
        "PyBot",
        "Hello! Welcome to PyBot. How can I help you?"
    )


# Send button
send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 10, "bold"),
    bg="#426FA9",
    fg="white",
    relief="flat",
    padx=18,
    pady=8,
    command=send_message
)
send_button.pack(side="left", padx=8)


# Enter key binding
message_entry.bind("<Return>", send_message)


# Clear button
clear_button = tk.Button(
    root,
    text="Clear Chat",
    font=("Arial", 10),
    bg="#DCE7F5",
    fg="#23395D",
    relief="flat",
    command=clear_chat
)
clear_button.pack(side="bottom", pady=(0, 10))


# Welcome message
display_message(
    "PyBot",
    "Hello! Welcome to PyBot. How can I help you?"
)

message_entry.focus()

# Run application
root.mainloop()
