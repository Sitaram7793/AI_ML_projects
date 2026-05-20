import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_pdf(text):

    prompt = f"""
    Summarize the following PDF content in simple language:

    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text