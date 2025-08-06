import requests

# Global variable to store conversation history
conversation_history = [
    {"role": "system", "content": "You are a persuasive sales assistant."}
]

def get_ai_reply(prompt):
    global conversation_history

    # Add user's input to conversation history
    conversation_history.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": "Bearer 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",  # Replace with your key
        "Content-Type": "application/json",
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": conversation_history,
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    # Extract and save assistant's reply
    reply = response.json()["choices"][0]["message"]["content"]
    conversation_history.append({"role": "assistant", "content": reply})

    return reply
