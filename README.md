# 🧠 Voice-Based AI Sales Bot

A voice-interactive AI Sales Bot that listens to the user, transcribes their speech, generates a context-aware sales response using an LLM via OpenRouter, and speaks it back using Google Text-to-Speech (gTTS).

## 🎯 Features

- 🎤 Voice input via microphone
- ✍️ Speech-to-text using OpenAI Whisper
- 🤖 Smart response generation via OpenRouter (LLM API)
- 🔊 Natural voice output using gTTS
- 🔁 Continuous conversation loop
- ⚡ Lightweight and terminal-based — No GUI needed

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/abrarkhancodes/voice-based-sales-bot.git
cd voice-based-sales-bot

2. Set Up the Environment
Make sure you have Python 3.10+ installed. Then install dependencies:
pip install -r requirements.txt

3. Add Your Environment Variables
Create a .env file in the root directory with the following content:
OPENROUTER_API_KEY=your_openrouter_api_key_here
Get your API key from: https://openrouter.ai/

▶️ Running the Bot
bash
Copy
Edit
python sales_bot.py

Powered By:

Whisper for Speech Recognition
OpenRouter for LLM Integration
gTTS for Text-to-Speech
Python for orchestration
