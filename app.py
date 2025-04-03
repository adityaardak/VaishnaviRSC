from scripts.save_pdf import save_minutes_pdf
import streamlit as st
from scripts.transcribe import SpeechToText
from scripts.summarize import TextSummarizer
from scripts.translate_summary import SummaryTranslator
from scripts.gemini_minutes import generate_minutes
from fpdf import FPDF
import os
import datetime

# Ensure directories exist
for folder in ["audio_files", "transcripts", "minutes"]:
    os.makedirs(folder, exist_ok=True)

# Initialize objects
stt = SpeechToText(model_size="base")
summarizer = TextSummarizer()
translator = SummaryTranslator()

# Streamlit Tabs
tab_home, tab_transcript, tab_history, tab_info = st.tabs(["🏠 Home", "🎤 Transcript", "📜 History", "ℹ️ Info"])

# Home Tab
with tab_home:
    st.title("🎙️ SmartMeetingAI with Gemini")
    st.markdown("Efficient meetings with Gemini-powered minutes generation, transcription, and translations.")
    st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095", caption="Power meetings with Gemini AI")

# Transcript Tab
with tab_transcript:
    st.header("🎤 Upload & Generate Minutes")
    uploaded_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

    if uploaded_file:
        audio_path = os.path.join("audio_files", uploaded_file.name)
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.audio(audio_path)

        if st.button("Generate Transcript, Summary & Minutes"):
            with st.spinner("Processing..."):
                transcript = stt.transcribe(audio_path)

                summary = summarizer.summarize_text(transcript) if len(transcript.split()) >= 30 else "Transcript too short."

                translations = {
                    'hi': translator.translate_summary(summary, 'hi'),
                    'ta': translator.translate_summary(summary, 'ta'),
                    'te': translator.translate_summary(summary, 'te')
                }

                # Gemini Minutes Generation
                minutes_content = generate_minutes(transcript, summary, translations)

                # Save PDF clearly
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                minutes_filename = f"Minutes_{timestamp}.pdf"
                minutes_path = os.path.join("minutes", minutes_filename)

                from fpdf import FPDF

                # Use clearly defined Unicode-compatible PDF function
                save_minutes_pdf(minutes_content, minutes_path)



            st.subheader("📝 Transcript")
            st.text_area("Transcript", transcript, height=200)

            st.subheader("🔖 Summary")
            st.write(summary)

            st.subheader("🌐 Translations")
            st.markdown(f"**Hindi:** {translations['hi']}")
            st.markdown(f"**Tamil:** {translations['ta']}")
            st.markdown(f"**Telugu:** {translations['te']}")

            with open(minutes_path, "rb") as pdf_file:
                st.download_button("Download Minutes PDF", pdf_file, file_name=minutes_filename)

# History Tab
with tab_history:
    st.header("📜 Minutes History")
    minutes_files = sorted(os.listdir("minutes"), reverse=True)

    if minutes_files:
        for file in minutes_files:
            date = file.replace("Minutes_", "").replace(".pdf", "").replace("_", " ")
            file_path = os.path.join("minutes", file)
            col1, col2 = st.columns([3, 1])
            col1.write(f"📅 {date}")
            with open(file_path, "rb") as f:
                col2.download_button("Download", data=f, file_name=file)
    else:
        st.info("No previous minutes found.")

# Info Tab
with tab_info:
    st.header("👩‍💻 Developers")
    st.markdown("""
    - **Developer 1:** [LinkedIn](https://linkedin.com/in/developer1)
    - **Developer 2:** [LinkedIn](https://linkedin.com/in/developer2)

    [🔗 Share this App](https://your-app-link.com)
    """)

