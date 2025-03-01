# chatbot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer



# Create a ChatBot instance with a storage adapter (using a local SQLite database)
chatbot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',  # Finds the closest matching response
        'chatterbot.logic.TimeLogicAdapter'  # Can respond with the current time
    ]
)

# Optional: Train with a custom conversation
custom_conversation = [
    "Hi there!",
    "Hello!",
    "How can I help you?",
    "I need assistance with my order.",
    "Sure, please provide your order number.",
    "Thanks, my order number is 12345.",
    "You're welcome! Your order is on its way."
]

trainer = ListTrainer(chatbot)
trainer.train(custom_conversation)

# Alternatively, you can train using the pre-built English corpus:
# corpus_trainer = ChatterBotCorpusTrainer(chatbot)
# corpus_trainer.train("chatterbot.corpus.english")

# Chat loop
print("Welcome to Buddy! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Buddy: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Buddy:", response)
