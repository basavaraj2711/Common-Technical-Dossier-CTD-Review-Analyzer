# CTD PDF Review Analyzer

The **CTD PDF Review Analyzer** is a Streamlit-based application designed to streamline the review of Common Technical Dossiers (CTDs). This tool leverages Generative AI to provide detailed feedback on the content of CTDs, offering structured review comments and allowing users to download the review in an Excel format.

---

## Features

### 📄 PDF Upload and Text Extraction
- Upload CTD documents in PDF format.
- Extracts text from the PDF, ready for analysis.

### 🔍 AI-Powered Review
- Analyzes the extracted content using Google's Generative AI (Gemini).
- Provides a structured review of the document with detailed comments on:
  - **Section of CTD**
  - **Subsection of CTD**
  - **Name of Content**
  - **Review Comments**

### 📤 Excel Export
- Converts the AI-generated review into a structured Excel file.
- Provides an easy option to download the review for further use.

### 📋 User-Friendly Interface
- Interactive and intuitive UI built with Streamlit.
- Features real-time progress indicators and preview options.

---

## Installation

### Prerequisites
1. **Python** (version 3.8 or higher)
2. Install required libraries:

   ```bash
   pip install streamlit pandas google-generativeai PyPDF2 openpyxl
   ```

3. **Google Generative AI API Key**:
   - Set up your API key and export it as an environment variable:
     ```bash
     export GEMINI_API_KEY="YOUR_API_KEY"
     ```

---

## Usage

### 1. Run the Application
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### 2. Upload PDF
   - Drag and drop your CTD document (PDF format) into the file uploader.

### 3. Analyze the Document
   - Click **Analyze Document** to process the text with AI.
   - View the AI-generated review in the text area.

### 4. Download Review as Excel
   - Click **Download Review as Excel** to generate and download the structured review in an Excel file.

---

## File Descriptions

### `app.py`
The main application script that:
- Extracts text from PDF files.
- Divides text into manageable chunks.
- Sends the text chunks to the Generative AI for review.
- Displays the AI-generated review.
- Exports the review to an Excel file.

### Libraries Used
- **Streamlit**: For building the web interface.
- **PyPDF2**: For PDF text extraction.
- **pandas**: For creating and exporting structured data.
- **google-generativeai**: For AI-powered analysis.

---

## Key Functions

### `extract_text_from_pdf`
Extracts text from an uploaded PDF document.

### `divide_text_into_chunks`
Divides large text content into smaller chunks to comply with AI input limits.

### `review_ctd_document`
Analyzes the CTD content using Google's Generative AI and returns a detailed review.

### `generate_excel_from_review`
Parses the AI-generated review into structured data and exports it as an Excel file.

---

## Notes
- Ensure the Google Generative AI API key is correctly set in the environment.
- PDF files should be text-based (scanned images are not supported).

---

## Example Usage

1. **Upload PDF**:
   - Select a PDF file containing the CTD content.

2. **Analyze Document**:
   - Click on **Analyze Document** to generate a structured review.

3. **Download Excel**:
   - Export the review to an Excel file by clicking **Download Review as Excel**.

---

## Troubleshooting
- **No API Response**: Ensure the API key is valid and the environment variable is correctly set.
- **Empty Review**: Check that the uploaded PDF contains text-based content.



