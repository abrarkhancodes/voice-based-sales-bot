import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

duration = 5  # seconds
samplerate = 16000

print("🎙️ Recording for 5 seconds...")
recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
sd.wait()
wav.write("input.wav", samplerate, recording)

model = whisper.load_model("base")
result = model.transcribe("input.wav")
print("📝 You said:", result["text"])
