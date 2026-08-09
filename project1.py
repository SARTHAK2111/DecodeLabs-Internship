
"""
Rule-Based AI Chatbot
DecodeLabs - Project 1
A simple chatbot that uses if-else logic to respond to predefined inputs.
"""

def get_bot_response(user_input):
    """
    Takes user input, normalizes it, and returns a response
    based on predefined rules (if-else logic).
    """
    # Normalize input: lowercase + remove extra spaces
    text = user_input.lower().strip()

    # --- Greetings ---
    if text in ["hi", "hello", "hey", "hii", "helo"]:
        return "Hello there! How can I help you today?"

    elif text in ["good morning"]:
        return "Good morning! Hope you have a great day ahead."

    elif text in ["good night"]:
        return "Good night! Sleep well."

    # --- Bot identity ---
    elif "your name" in text:
        return "I'm DecodeBot, your friendly rule-based AI assistant."

    elif "how are you" in text:
        return "I'm just a program, but I'm running perfectly! How about you?"

    # --- Help ---
    elif text in ["help", "what can you do"]:
        return ("I can respond to greetings, tell you my name, "
                "answer 'how are you', and chat a bit. Type 'bye' to exit.")

    # --- Gratitude ---
    elif text in ["thanks", "thank you"]:
        return "You're welcome! Happy to help."

    # --- Exit commands ---
    elif text in ["bye", "exit", "quit", "goodbye"]:
        return "EXIT"  # special signal handled in main loop

    # --- Default fallback ---
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    """
    Runs the chatbot in a continuous loop until the user exits.
    """
    print("=" * 50)
    print("   Welcome to DecodeBot - Rule-Based AI Chatbot")
    print("   Type 'help' to see options, or 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("You: ")

        response = get_bot_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day. 👋")
            break
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    run_chatbot()
