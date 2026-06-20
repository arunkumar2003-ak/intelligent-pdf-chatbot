import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📄 PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    st.success("PDF Loaded Successfully")

    question = st.text_input(
        "Ask Question About PDF"
    )

    if question:

        prompt = f"""
        PDF Content:
        {text}

        Question:
        {question}

        Answer based only on PDF.
        """

        response = model.generate_content(prompt)

        st.write(response.text)