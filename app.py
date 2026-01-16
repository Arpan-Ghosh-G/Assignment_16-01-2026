# from flask import Flask, request, jsonify, render_template
# import requests

# # Take OpenRouter API key from user at runtime
# api_key = input("Enter your OpenRouter API key: ")

# OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json",
#     "HTTP-Referer": "http://localhost",
#     "X-Title": "Flask Chatbot"
# }

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message")

#     if not user_message:
#         return jsonify({"reply": "Message is required"}), 400

#     payload = {
#         "model": "meta-llama/llama-3.3-70b-instruct:free",
#         "messages": [
#             {"role": "user", "content": user_message}
#         ]
#     }

#     try:
#         response = requests.post(
#             OPENROUTER_URL,
#             headers=HEADERS,
#             json=payload,
#             timeout=30
#         )

#         response.raise_for_status()
#         result = response.json()

#         bot_reply = result["choices"][0]["message"]["content"]

#         return jsonify({"reply": bot_reply})

#     except requests.exceptions.RequestException as e:
#         return jsonify({
#             "reply": f"Error from OpenRouter API: {str(e)}"
#         }), 500


# if __name__ == "__main__":
#     app.run(debug=True)












# Form Landing Page UI Backend
from flask import Flask, request, jsonify, render_template
import requests
import json

# Take OpenRouter API key at runtime (assignment-safe)
api_key = input("Enter your OpenRouter API key: ")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Dynamic Form Generator"
}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-form", methods=["POST"])
def generate_form():
    user_prompt = request.json.get("prompt")

    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    system_prompt = """
You are a form generator.

From the user request, generate a JSON schema for a web form.

Rules:
- Output ONLY valid JSON
- No explanations
- No markdown
- Each field must have:
  - label
  - name (snake_case)
  - type (text, number, textarea)
  - required (true/false)

Output format:
{
  "title": "Form title",
  "fields": [
    {
      "label": "Field Label",
      "name": "field_name",
      "type": "text",
      "required": true
    }
  ]
}
"""

    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        response.raise_for_status()

        result = response.json()
        raw_output = result["choices"][0]["message"]["content"]

        # Convert LLM output string → JSON safely
        schema = json.loads(raw_output)

        return jsonify(schema)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/submit-form", methods=["POST"])
def submit_form():
    # Meta-tag mapping (key-value pairs)
    submitted_data = request.json
    return jsonify({
        "message": "Form submitted successfully",
        "mapped_data": submitted_data
    })


if __name__ == "__main__":
    app.run(debug=True)
