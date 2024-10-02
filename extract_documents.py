import os
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text_from_files():
    # Define paths to your documents here
    documents = [
        'data/Plagirism Form.pdf',
        'data/PGPM 2024- Welcome Note - Nov 20, 2023.pdf',
        'data/id card photo guidelines.docx',
        'data/Day 1 guidelines.docx',
        'data/SPJIMR CAMPUS-GUIDE MAP.pdf',
        'data/Enclosure - 2 - Student Handbook 2024.pdf',
        'data/program guidelines.pdf'
    ]
    
    document_text = ""
    for doc in documents:
        if doc.endswith(".pdf"):
            document_text += extract_text_from_pdf(doc) + "\n"
        elif doc.endswith(".docx"):
            document_text += extract_text_from_docx(doc) + "\n"
    return document_text
