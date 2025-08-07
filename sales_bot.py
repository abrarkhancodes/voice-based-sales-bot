import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time

from step2_respond import get_ai_reply
from step3_speak import speak

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
    You are an enthusiastic and knowledgeable AI sales representative for TechSolutions Inc.
    We sell cutting-edge software solutions including:
    1. AI-powered analytics tools ($2,000-$10,000/month)
    2. Cloud infrastructure services ($500-$5,000/month)
    3. Custom software development ($50,000-$200,000 per project)
    4. IT consulting services ($200/hour)

    Your goals:
    - Build rapport with potential customers
    - Understand their business needs
    - Recommend appropriate solutions
    - Handle objections professionally
    - Guide them toward making a purchase decision

    Keep responses conversational, engaging, and under 3 sentences.
    Always ask follow-up questions to understand their needs better.
    Be helpful and solution-oriented.
    """

    # Initial welcome message (speak once)
    welcome_message = "Hello! Welcome to TechSolutions Inc. I'm your AI sales assistant. How can I help you find the perfect technology solution for your business today?"
    print("🤖 AI: " + welcome_message)
    speak(welcome_message)

    while True:
        try:
            # Step 1: Record
            record_audio()

            # Step 2: Transcribe
            user_input = transcribe_audio()
            print("📝 You said:", user_input)

            # Exit condition
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("👋 Ending conversation. Goodbye!")
                speak("Thank you for your time! Have a great day!")
                break

            # Step 3: Get AI reply
            reply = get_ai_reply(user_input)
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
