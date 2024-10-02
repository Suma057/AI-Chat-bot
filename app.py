import streamlit as st
from extract_documents import extract_text_from_files
from chatbot import chatbot_conversation

# Page title
st.title("Academic AI Chatbot")

# Extract the document text
document_text = extract_text_from_files()

# Display success message after extracting document text
st.success("Documents processed and loaded successfully!")

# Input: User's name
user_name = st.text_input("Please enter your name:")

# Input: Query from the user
query = st.text_input("Ask me anything about the documents:")

# If a query is provided, generate a response
if query and user_name:
    response = chatbot_conversation(user_name, query, document_text)
    st.write(response)
