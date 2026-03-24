from flask import Flask, request, jsonify, render_template
from services.chatbot_service import ask_question, clear_session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    session_id = request.json.get("session_id", "default")
    data = ask_question(user_input, session_id)
    return jsonify({
        "message": data.get("message", ""),
        "product_list": data.get("product_list", [])
    })

@app.route("/clear", methods=["POST"])
def clear():
    session_id = request.json.get("session_id", "default")
    clear_session(session_id)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
