from sentence_transformers import SentenceTransformer, util
import numpy as np

class TextClassifierRanker:
    def __init__(self):
        print("Loading SentenceTransformer model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Model loaded successfully.")

        # Define keywords representing urgency/action items
        self.action_keywords = ['complete', 'finish', 'submit', 'do', 'start', 'call', 'email', 'arrange', 'schedule', 'plan', 'organize', 'review', 'fix', 'resolve', 'urgent', 'asap', 'immediately']

    def classify_and_rank(self, transcript):
        sentences = [sent.strip() for sent in transcript.split('.') if sent.strip()]
        sentence_embeddings = self.model.encode(sentences)

        action_scores = []
        for sentence in sentences:
            score = sum([keyword in sentence.lower() for keyword in self.action_keywords])
            action_scores.append(score)

        # Classify sentences
        classified = {
            'Action Items': [],
            'Discussion Topics': []
        }

        for idx, sentence in enumerate(sentences):
            if action_scores[idx] > 0:
                classified['Action Items'].append((sentence, action_scores[idx]))
            else:
                classified['Discussion Topics'].append(sentence)

        # Rank Action Items by urgency (score)
        classified['Action Items'].sort(key=lambda x: x[1], reverse=True)

        return classified
