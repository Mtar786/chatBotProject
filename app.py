from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Initialize your ChatBot instance
chatbot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

# Train your chatbot using the English corpus (optional, if not already trained)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot.get_response(user_input)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
