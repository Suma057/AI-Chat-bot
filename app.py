import streamlit as st
from chatbot import generate_answer

st.title("AI Chatbot using GPT4All")

# Sidebar for uploading documents
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx"])

if uploaded_file is not None:
    # Extract text from the uploaded document (You can use your extract_documents.py logic here)
    # For simplicity, let's assume you have the document text
    document_text = "This is some example document text."

    st.write("Document uploaded successfully!")

    # Query input
    query = st.text_input("Ask me anything:")

    if query:
        answer = generate_answer(query, document_text)
        st.write("Answer:", answer)
