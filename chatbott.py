print("====================================")
print("       Welcome to DecodeBot 🤖")
print("====================================")
print("Type 'bye', 'exit', or 'quit' to stop.\n")

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! Welcome to DecodeBot.",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "My name is DecodeBot.",
    "who are you": "I am a simple Rule-Based AI Chatbot.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what can you do": "I can answer simple predefined questions.",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!"
}

while True:
    user_input = input("You: ").lower().strip()

    
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    
    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")