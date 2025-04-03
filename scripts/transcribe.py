import whisper
import torch

class SpeechToText:
    def __init__(self, model_size="base"):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading Whisper '{model_size}' model on {device}...")
        self.model = whisper.load_model(model_size, device=device)
        print("Whisper model loaded successfully.")

    def transcribe(self, audio_path):
        print("Starting transcription with Whisper...")
        result = self.model.transcribe(audio_path)
        transcript = result["text"]
        print("Transcription completed.")
        return transcript
