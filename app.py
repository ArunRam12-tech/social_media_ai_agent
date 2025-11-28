import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    st.error("❌ API key not found in .env.\nAdd:\nGROQ_API_KEY=your_key_here")
    st.stop()

client = Groq(api_key=API_KEY)

st.set_page_config(page_title="Social Media AI Agent", page_icon="📱", layout="wide")
st.title("📱 AI Social Media Content Generator (FREE)")
st.write("Powered by Groq Llama 3 — No billing required 🚀")

platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter", "YouTube Short", "Facebook"])
tone = st.selectbox("Tone", ["Funny 😂", "Professional 👔", "Motivational 💪", "Casual 😎", "Educational 📚"])
content_type = st.selectbox("Content Type", ["Caption", "Hashtags", "Full Post", "Content Ideas", "Weekly Plan"])
topic = st.text_input("Enter Topic:", placeholder="ex: Fitness, Clothing, AI, Motivation...")

if st.button("🚀 Generate"):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating content..."):

            prompt = f"""
            You are an expert social media content creator.

            Platform: {platform}
            Tone: {tone}
            Task: Generate {content_type}
            Topic: {topic}

            Make it interesting, engaging, and readable.
            """

            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant"
            )

            result = chat_completion.choices[0].message.content

        st.success("✨ Content Generated!")
        st.text_area("Your Result:", result, height=250)
        st.download_button("📥 Download", data=result, file_name="content.txt")

st.caption("Made with ❤️ | Arun's AI Agent | Free Version")
