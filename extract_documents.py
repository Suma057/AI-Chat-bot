import os
from PyPDF2 import PdfReader
from docx import Document
import pandas as pd

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()

def extract_all_files(directory):
    text_data = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".pdf"):
            text_data.append(extract_text_from_pdf(file_path))
        elif filename.endswith(".docx"):
            text_data.append(extract_text_from_docx(file_path))
        elif filename.endswith(".xlsx"):
            text_data.append(extract_text_from_excel(file_path))
    return text_data
