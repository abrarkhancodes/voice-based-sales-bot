# step2_respond.py
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Conversation history
conversation_history = [
    {
        "role": "system",
        "content": """
You are an enthusiastic and knowledgeable AI sales representative for TechSolutions Inc.

We offer:
1. AI-powered analytics tools ($2,000-$10,000/month)
2. Cloud infrastructure services ($500-$5,000/month)
3. Custom software development ($50,000-$200,000 per project)
4. IT consulting services ($200/hour)

Goals:
- Build rapport with potential customers
- Understand their business needs
- Recommend appropriate solutions
- Handle objections professionally
- Keep responses under 3 sentences and always ask helpful follow-up questions
"""
    }
]

# API key
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Missing OpenRouter API key.")

def get_ai_reply(user_input):
    global conversation_history

    conversation_history.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": conversation_history[-10:],  # Keep recent history
        "max_tokens": 150
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        reply = result["choices"][0]["message"]["content"]
        conversation_history.append({"role": "assistant", "content": reply})
        return reply

    except requests.exceptions.RequestException as e:
        print("[ERROR] HTTP error:", e)
        return "Sorry, I'm having trouble reaching the server."

    except Exception as e:
        print("[ERROR] General error:", e)
        return "Something went wrong. Can you please try again?"
