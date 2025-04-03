import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(duration=10, filename="output.wav", fs=16000):
    print("Recording audio...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    audio_path = os.path.join("audio_files", filename)
    write(audio_path, fs, audio)
    print(f"Audio recording saved as {audio_path}")
    return audio_path
