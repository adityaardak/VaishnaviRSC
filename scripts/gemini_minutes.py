import google.generativeai as genai
import streamlit as st

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINIAPIKEY"])

def generate_minutes(transcript, summary, translations):
    prompt = f"""
    Generate professional Minutes of Meeting document from the given details:

    Transcript:
    {transcript}

    Summary:
    {summary}

    Translations:
    Hindi: {translations['hi']}
    Tamil: {translations['ta']}
    Telugu: {translations['te']}

    Format it clearly and professionally.
    """

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    return response.text
