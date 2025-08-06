import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

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
    print("🤖 Sales bot is listening! Say 'exit', 'bye', or 'quit' to stop.\n")

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
                speak("Goodbye!")
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

if __name__ == "__main__":
    main()
