from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Home route (VERY IMPORTANT)
@app.route("/")
def home():
    return render_template("index.html")

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_message,
            "stream": False
        }
    )

    reply = response.json()["response"]
    return jsonify({"reply": reply})

# Run app
if __name__ == "__main__":
    app.run(debug=True)