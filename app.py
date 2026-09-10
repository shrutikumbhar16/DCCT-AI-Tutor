from flask import Flask, request, render_template
from agent import ask_tutor, clear_history, generate_quiz

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question")

    if not question:
        return {
            "error": "Please provide a question."
        }, 400

    answer = ask_tutor(question)

    return {
        "answer": answer
    }
@app.route("/quiz", methods=["POST"])
def quiz():
    question = generate_quiz()
    return {"question": question}

@app.route("/clear", methods=["POST"])
def clear():

    clear_history()

    return {
        "message": "Conversation cleared."
    }


if __name__ == "__main__":
    app.run(debug=True)