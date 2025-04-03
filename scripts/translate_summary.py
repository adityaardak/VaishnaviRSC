from deep_translator import GoogleTranslator

class SummaryTranslator:
    def __init__(self):
        print("Translator initialized using deep-translator.")

    def translate_summary(self, text, dest_lang):
        print(f"Translating summary to {dest_lang}...")
        translation = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        print("Translation completed.")
        return translation
