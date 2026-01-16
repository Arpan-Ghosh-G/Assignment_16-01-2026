import requests

api_key = input("Enter your OpenRouter API key: ")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "CLI Chatbot"
}

print("\nChat started. Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        bot_reply = data["choices"][0]["message"]["content"]

        print("Bot:", bot_reply)

    except Exception as e:
        print("Error:", e)