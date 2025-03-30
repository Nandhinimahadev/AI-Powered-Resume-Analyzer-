import streamlit as st
import os
from utils.extract import extract_text_from_pdf
from utils.analyse import extract_entities

st.title("AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text_from_pdf(file_path)
    if text:
        entities = extract_entities(text)
        st.subheader("Extracted Information")
        st.json(entities)
    else:
        st.error("Could not extract text from the uploaded file.")
