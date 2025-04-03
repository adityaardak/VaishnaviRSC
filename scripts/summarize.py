from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        print("Loading summarization model...")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        print("Summarization model loaded successfully.")

    def summarize_text(self, text, max_length=150, min_length=40):
        # Check if the input text is too short for summarization
        if len(text.split()) < 30:
            print("Input text too short to summarize. Skipping summarization.")
            return "Transcript too short to summarize."

        print("Summarizing text...")
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        summarized_text = summary[0]['summary_text']
        print("Text summarized successfully.")
        return summarized_text
