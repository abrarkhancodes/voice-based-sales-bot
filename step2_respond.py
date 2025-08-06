import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global conversation history
conversation_history = [
    {"role": "system", "content": "You are a persuasive sales assistant."}
]

# Load API key securely
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Missing OpenRouter API key. Make sure .env file contains OPENROUTER_API_KEY.")

def get_ai_reply(prompt):
    global conversation_history

    conversation_history.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": conversation_history,
        "max_tokens": 150
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        if "choices" not in result:
            print("[ERROR] Unexpected response format:")
            print(result)
            return "Sorry, I couldn't understand your request."

        reply = result["choices"][0]["message"]["content"]
        conversation_history.append({"role": "assistant", "content": reply})
        return reply

    except requests.exceptions.RequestException as e:
        print("[ERROR] Network or HTTP error:", e)
        return "Sorry, there was a problem connecting to the AI service."

    except Exception as e:
        print("[ERROR] General failure:", e)
        print("[DEBUG] Raw response:", response.text)
        return "Sorry, something went wrong while generating a reply."
