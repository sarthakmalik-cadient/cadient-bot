from flask import Flask, request, jsonify, render_template
from services.chatbot_service import ask_question

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = ask_question(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
