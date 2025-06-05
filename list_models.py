import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}"

response = requests.get(API_URL)
print(response.status_code)
print(response.json())
