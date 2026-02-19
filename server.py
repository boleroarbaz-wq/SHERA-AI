from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="PASTE_YOUR_OPENROUTER_KEY",
    base_url="https://openrouter.ai/api/v1"
)

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are SHERA, a Hindi & Urdu speaking friendly AI assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

app.run(host="0.0.0.0", port=10000)
