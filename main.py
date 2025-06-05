import os
from dotenv import load_dotenv
import streamlit as st
import requests

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Gemini API ka latest URL (model name se 'models/' hata diya)
MODEL = "gemini-1.5-flash"  # 'models/' hata diya hai
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# Gemini se response lene ka function
def get_gemini_response(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# Streamlit UI
def main():
    st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
    st.title("🤖 Chat with Gemini (Google AI)")

    prompt = st.text_area("✍️ Enter your message here:", height=150)

    if st.button("🚀 Get Response"):
        if not prompt.strip():
            st.warning("⚠️ Please enter a message first.")
        else:
            response = get_gemini_response(prompt)
            st.markdown("### 📥 Gemini Response:")
            st.markdown(f"<div style='background-color:#e0f7fa;padding:10px;border-radius:10px;'>{response}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
