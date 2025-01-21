import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from PyPDF2 import PdfReader

# Set your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyCtwToVA60UQpJpa1BrHHGxxoxcoSNBBbM"))

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    """Extracts text from the uploaded PDF file."""
    try:
        pdf_reader = PdfReader(uploaded_file)
        text = "\n".join(page.extract_text() for page in pdf_reader.pages)
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

# Function to divide text into chunks
def divide_text_into_chunks(text, chunk_size=2000):
    """Divides the extracted text into manageable chunks for processing."""
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

# Function to review the CTD document using Generative AI
def review_ctd_document(document_text):
    """Analyzes the CTD document using Generative AI and returns a structured review."""
    try:
        prompt_template = """
        You are an expert in reviewing Common Technical Dossiers (CTDs) for regulatory compliance and quality.
        Analyze the following CTD content and provide a structured review with detailed comments for improvement.

        Content:
        {content}

        Provide your feedback in the format below:
        - Section of CTD: [Section Name]
        - Subsection of CTD: [Subsection Name]
        - Name of Content: [Specific Content]
        - Review Comments: [Detailed Feedback]

        Be precise and focus on identifying flaws, inconsistencies, or areas for improvement.
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        chunks = divide_text_into_chunks(document_text)
        reviews = []

        for chunk in chunks:
            prompt = prompt_template.format(content=chunk)
            response = model.generate_content(prompt)
            reviews.append(response.text)

        return "\n\n".join(reviews)
    except Exception as e:
        st.error(f"Error generating review: {e}")
        return None

# Streamlit App Layout
st.set_page_config(page_title="CTD PDF Review Analyzer", page_icon="📄", layout="wide")
st.title("📄 Common Technical Dossier (CTD) Review Analyzer")
st.markdown(
    """
    Upload your CTD document in PDF format, and let our AI-powered system provide an extensive review with detailed comments and suggestions for improvement.
    """
)

# File uploader
uploaded_file = st.file_uploader("Upload CTD Document (PDF format only)", type=["pdf"])

# Analyze the uploaded document
if uploaded_file:
    with st.spinner("Extracting text from the PDF..."):
        document_text = extract_text_from_pdf(uploaded_file)

    if document_text:
        st.subheader("📑 Extracted Document Text")
        st.text_area("Preview of Extracted Text", document_text[:1000], height=300)

        if st.button("Analyze Document"):
            with st.spinner("Analyzing the document using AI..."):
                review_output = review_ctd_document(document_text)

            if review_output:
                st.subheader("🔍 AI-Generated Review")
                st.text_area("Review Output", review_output, height=500)
            else:
                st.error("Failed to generate a review. Please try again.")
else:
    st.info("Please upload a CTD document to proceed.")
