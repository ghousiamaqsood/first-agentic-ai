import os
from dotenv import load_dotenv
import streamlit as st
import requests

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "gemini-1.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# Gemini se response lene ka function
def get_gemini_response(prompt, language):
    lang_prefix = {
        "English": "Answer in English:",
        "Urdu": "براہ کرم اردو میں جواب دیں:",
        "Sindhi": "مهرباني ڪري سنڌي ۾ جواب ڏيو:",
        "Arabic": "يرجى الرد باللغة العربية:",
        "Pashto": "مهرباني وکړئ په پښتو کې ځواب ورکړئ:",
        "Hindi": "कृपया हिंदी में उत्तर दें:",
        "Chinese": "请用中文回答：",
        "Bengali": "অনুগ্রহ করে বাংলায় উত্তর দিন:",
        "Punjabi": "ਕਿਰਪਾ ਕਰਕੇ ਪੰਜਾਬੀ ਵਿੱਚ ਜਵਾਬ ਦਿਓ:"
    }
    full_prompt = f"{lang_prefix.get(language, '')}\n{prompt}"

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": full_prompt}]}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# Streamlit UI
def main():
    st.set_page_config(page_title="🌐 Agentic AI - Multilingual Chat", page_icon="🧠")
    st.title("🤖 Agentic AI: Multilingual Gemini Chat")

    st.markdown("🗣️ **Choose your language:**")
    language = st.radio(
        "Language",
        ["English", "Urdu", "Sindhi", "Arabic", "Pashto", "Hindi", "Chinese", "Bengali", "Punjabi"],
        horizontal=True
    )

    prompt = st.text_area("✍️ Enter your message here:", height=150)

    if st.button("🚀 Get Response"):
        if not prompt.strip():
            st.warning("⚠️ Please enter a message first.")
        else:
            response = get_gemini_response(prompt, language)
            st.markdown("### 📥 Gemini Response:")
            st.markdown(
                f"<div style='background-color:#e0f7fa;padding:10px;border-radius:10px;font-size:16px;'>{response}</div>",
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
