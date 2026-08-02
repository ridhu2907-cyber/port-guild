# chatbot.py
print("Welcome to Riddhi's Chatbot!")
while True:
    user = input("You: ")
    if user.lower() in ["hi", "hello"]:
        print("Bot: Hello! How are you?")
    elif user.lower() in ["bye", "exit"]:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I'm still learning, but nice to chat!")
