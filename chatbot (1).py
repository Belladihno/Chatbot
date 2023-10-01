import random

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "Hey",
    "How is your day",
    "Hello, Talk to you later",
    "wassup",
    "Be right back"
]


print("Welcome to my first python chatbot😁")
human_input = input()
response = random.choice(conversation)
print(response)