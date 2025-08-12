import datetime

print("🤖 Hello! I am your enhanced chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if "bye" in user_input:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    # Greetings
    elif any(greet in user_input for greet in ["hi", "hello", "hey"]):
        print("Bot: Hello! How can I help you today?")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking. How about you?")

    # Name
    elif "your name" in user_input:
        print("Bot: I am a Python rule-based chatbot created during the BroskiesHub Internship.")

    # Date and time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: The current time is {current_time} ⏰")

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Bot: Today's date is {current_date} 📅")

    # FAQs
    elif "internship" in user_input:
        print("Bot: The internship is a great opportunity to learn and build Python projects.")

    elif "python" in user_input:
        print("Bot: Python is a versatile programming language great for web, AI, and automation.")

    elif "flask" in user_input:
        print("Bot: Flask is a lightweight Python web framework, perfect for small to medium projects.")

    # Help menu
    elif "help" in user_input:
        print("Bot: You can ask me about the date, time, my name, Python, Flask, or the internship.")

    # Unknown input
    else:
        print("Bot: I'm not sure how to respond to that. Try asking about date, time, Python, Flask, or internship.")
