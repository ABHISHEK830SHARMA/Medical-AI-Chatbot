from flask import Flask, render_template, request, jsonify
from connect_memory_with_llm import get_answer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        question = data.get("message")

        if not question:
            return jsonify({"error": "Question is required"}), 400

        answer = get_answer(question)

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
