from gtts import gTTS
import os
import platform

def speak(text):
    # 📢 Generate speech (fast by setting slow=False)
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("reply.mp3")

    # 🔊 Play audio based on the OS
    system = platform.system()

    if system == "Darwin":  # macOS
        os.system("afplay reply.mp3")
    elif system == "Windows":
        os.system("start reply.mp3")
    elif system == "Linux":
        os.system("mpg123 reply.mp3")
    else:
        print("Unsupported OS for audio playback")
