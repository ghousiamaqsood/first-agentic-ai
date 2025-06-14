# # # import os
# # # from dotenv import load_dotenv
# # # import streamlit as st
# # # import requests

# # # # Load API key from .env
# # # load_dotenv()
# # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # MODEL = "gemini-1.5-flash"
# # # API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# # # # Gemini se response lene ka function
# # # def get_gemini_response(prompt, language):
# # #     lang_prefix = {
# # #         "English": "Answer in English:",
# # #         "Urdu": "براہ کرم اردو میں جواب دیں:",
# # #         "Sindhi": "مهرباني ڪري سنڌي ۾ جواب ڏيو:",
# # #         "Arabic": "يرجى الرد باللغة العربية:",
# # #         "Pashto": "مهرباني وکړئ په پښتو کې ځواب ورکړئ:",
# # #         "Hindi": "कृपया हिंदी में उत्तर दें:",
# # #         "Chinese": "请用中文回答：",
# # #         "Bengali": "অনুগ্রহ করে বাংলায় উত্তর দিন:",
# # #         "Punjabi": "ਕਿਰਪਾ ਕਰਕੇ ਪੰਜਾਬੀ ਵਿੱਚ ਜਵਾਬ ਦਿਓ:"
# # #     }
# # #     full_prompt = f"{lang_prefix.get(language, '')}\n{prompt}"

# # #     headers = {"Content-Type": "application/json"}
# # #     data = {
# # #         "contents": [
# # #             {"parts": [{"text": full_prompt}]}
# # #         ]
# # #     }
# # #     response = requests.post(API_URL, headers=headers, json=data)
# # #     if response.status_code == 200:
# # #         return response.json()["candidates"][0]["content"]["parts"][0]["text"]
# # #     else:
# # #         return f"❌ Error: {response.status_code} - {response.text}"

# # # # Streamlit UI
# # # def main():
# # #     st.set_page_config(page_title="🌐 Agentic AI - Multilingual Chat", page_icon="🧠")
# # #     st.title("🤖 Agentic AI: Multilingual Gemini Chat")

# # #     st.markdown("🗣️ **Choose your language:**")
# # #     language = st.radio(
# # #         "Language",
# # #         ["English", "Urdu", "Sindhi", "Arabic", "Pashto", "Hindi", "Chinese", "Bengali", "Punjabi"],
# # #         horizontal=True
# # #     )

# # #     prompt = st.text_area("✍️ Enter your message here:", height=150)

# # #     if st.button("🚀 Get Response"):
# # #         if not prompt.strip():
# # #             st.warning("⚠️ Please enter a message first.")
# # #         else:
# # #             response = get_gemini_response(prompt, language)
# # #             st.markdown("### 📥 Gemini Response:")
# # #             st.markdown(
# # #                 f"<div style='background-color:#e0f7fa;padding:10px;border-radius:10px;font-size:16px;'>{response}</div>",
# # #                 unsafe_allow_html=True
# # #             )

# # # if __name__ == "__main__":
# # #     main()
# # import os
# # from dotenv import load_dotenv
# # import streamlit as st
# # import requests

# # # Load API key
# # load_dotenv()
# # API_KEY = os.getenv("GEMINI_API_KEY")

# # # Gemini model & endpoint
# # MODEL = "gemini-1.5-flash"
# # API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# # # Gemini response function
# # def get_gemini_response(prompt):
# #     headers = {
# #         "Content-Type": "application/json"
# #     }
# #     data = {
# #         "contents": [
# #             {"parts": [{"text": prompt}]}
# #         ]
# #     }
# #     response = requests.post(API_URL, headers=headers, json=data)
# #     if response.status_code == 200:
# #         return response.json()["candidates"][0]["content"]["parts"][0]["text"]
# #     else:
# #         return f"❌ Error: {response.status_code} - {response.text}"

# # # Streamlit UI
# # def main():
# #     st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
# #     st.title("🤖 Multilingual Chat with Gemini AI")

# #     st.markdown("💬 **Just type your message in any language (Urdu, English, Hindi, Pashto, Punjabi, Bengali, Chinese, etc.) and get a smart response.**")

# #     prompt = st.text_area("✍️ Write your message here:", height=150)

# #     if st.button("🚀 Get Response"):
# #         if not prompt.strip():
# #             st.warning("⚠️ Please enter a message first.")
# #         else:
# #             response = get_gemini_response(prompt)
# #             st.markdown("### 📥 Gemini Response:")
# #             st.markdown(
# #                 f"<div style='background-color:#e0f7fa;padding:10px;border-radius:10px;'>{response}</div>",
# #                 unsafe_allow_html=True
# #             )

# # if __name__ == "__main__":
# #     main()
# import streamlit as st
# import requests

# #  ✅ Use API key from Streamlit secrets
# API_KEY = st.secrets["GEMINI_API_KEY"]

# # Gemini model & endpoint
# MODEL = "gemini-1.5-flash"
# API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# # Gemini response function
# def get_gemini_response(prompt):
#     headers = {
#         "Content-Type": "application/json"
#     }
#     data = {
#         "contents": [
#             {"parts": [{"text": prompt}]}
#         ]
#     }
#     response = requests.post(API_URL, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()["candidates"][0]["content"]["parts"][0]["text"]
#     else:
#         return f"❌ Error: {response.status_code} - {response.text}"

# # Streamlit UI
# def main():
#     st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
#     st.title("🤖 Multilingual Chat with Gemini AI")

#     prompt = st.text_area("✍️ Write your message here:", height=150)

#     if st.button("🚀 Get Response"):
#         if not prompt.strip():
#             st.warning("⚠️ Please enter a message first.")
#         else:
#             response = get_gemini_response(prompt)
#             st.markdown("### 📥 Gemini Response:")
#             st.markdown(
#                 f"<div style='background-color:#e0f7fa;padding:10px;border-radius:10px;'>{response}</div>",
#                 unsafe_allow_html=True
#             )

# if __name__ == "__main__":
#     main()
import streamlit as st
import requests

# API Key and Model
API_KEY = st.secrets["GEMINI_API_KEY"]
MODEL = "gemini-1.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# Function to get Gemini Response
def get_response(prompt):
    system_prompt = f"""
User may write in any language. Detect the language and reply in the same language.

{prompt}
"""
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": system_prompt}]}]}
    res = requests.post(API_URL, headers=headers, json=data)
    if res.status_code == 200:
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Error: {res.status_code}"

# Main App
def main():
    st.set_page_config(page_title="Multilingual Chat with Gemini AI", layout="centered")

    # Heading
    st.markdown("""
        <h1 style='text-align: center;'>🤖 Multilingual Chat with Gemini AI</h1>
        <p style='text-align: left; font-size:16px; margin-top:30px;'>✍️ Write your message here:</p>
    """, unsafe_allow_html=True)

    # Styled input box using HTML/CSS
    user_input = st.text_input("", placeholder="Type your message here...", key="input")
    
    # Custom CSS for button and input field
    st.markdown("""
        <style>
        .stTextInput>div>div>input {
            background-color: #f9f9f9;
            height: 50px;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
        }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            margin-top: 10px;
        }
        div.stButton > button:hover {
            background-color: #45a049;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Button
    if st.button("Send"):
        if user_input.strip() == "":
            st.warning("⚠️ Please write something first.")
        else:
            response = get_response(user_input)
            st.markdown(
                f"<div style='background-color:#f1f1f1;padding:15px;border-radius:10px;margin-top:10px;'>{response}</div>",
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
