import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time

from bot_response import get_ai_reply
from user_response import speak

# Load Whisper model once (outside the loop for efficiency)
model = whisper.load_model("base")

# Function to record and save audio
def record_audio(filename="input.wav", duration=5, samplerate=16000):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, samplerate, recording)

# Function to transcribe audio
def transcribe_audio(filename="input.wav"):
    result = model.transcribe(filename)
    return result["text"].strip()

# Main conversation loop
def main():
    print("🤖 Initializing AI Sales Bot...")
    print("Say 'exit', 'bye', or 'quit' to stop.\n")

    # Sales bot personality and context introduction
    sales_context = """
    You are an enthusiastic, persuasive, and highly knowledgeable AI sales representative for TechSolutions Inc.
    Your primary goal is to actively sell our services while building trust and understanding the customer's needs.

    We sell:
    1. AI-powered analytics tools ($2,000 to $10,000/month) – helps businesses make data-driven decisions faster.
    2. Cloud infrastructure services ($500 to $5,000/month) – secure, scalable, and cost-efficient cloud hosting.
    3. Custom software development ($50,000 to $200,000/project) – tailored solutions for unique business needs.
    4. IT consulting services ($200 per hour) – expert advice to optimize tech strategy.

    Your goals:
    - Actively pitch relevant services based on customer needs
    - Highlight benefits and unique selling points
    - Share pricing and explain value clearly
    - Handle objections with confidence
    - Ask questions that lead toward a purchase
    - Encourage decision-making in a friendly, helpful way

    Keep responses under 3 sentences but persuasive and engaging.
    Always end your response with a follow-up sales question unless the user is ending the conversation.
    If they ask about a service, provide details and benefits without overwhelming them.
    """

    # Initial welcome message (speak once)
    welcome_message = (
        "Hello! Welcome to TechSolutions Inc. "
        "I’m your AI sales assistant. "
        "We offer powerful AI analytics, secure cloud services, custom software, and expert IT consulting. "
        "What challenges is your business currently facing so I can recommend the perfect solution?"
    )
    print("🤖 AI: " + welcome_message)
    speak(welcome_message)

    while True:
        try:
            # Step 1: Record
            record_audio()

            # Step 2: Transcribe
            user_input = transcribe_audio()
            print("📝 You said:", user_input)

            # Exit condition (checks anywhere in sentence)
            if any(word in user_input.lower() for word in ["exit", "quit", "bye"]):
                print("👋 Ending conversation. Goodbye!")
                speak("Thank you for your time! I hope we can work together soon. Goodbye!")
                break

            # Step 3: Get AI reply with sales context
            reply = get_ai_reply(f"{sales_context}\nCustomer: {user_input}")
            print("🤖 AI Reply:", reply)

            # Step 4: Speak AI reply
            speak(reply)

        except KeyboardInterrupt:
            print("\n⛔ Interrupted by user. Exiting.")
            speak("Goodbye!")
            break
        except Exception as e:
            print("[ERROR]", e)
            speak("Sorry, something went wrong. Please try again.")

if __name__ == "__main__":
    main()
