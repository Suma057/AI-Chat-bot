import streamlit as st
from chatbot import generate_answer
import streamlit_authenticator as stauth

# Create credentials
names = ["User1"]
usernames = ["user1"]
passwords = ["password"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "cookie_name", "signature_key", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Welcome {name}")
    # Rest of the chatbot code here
elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")

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
