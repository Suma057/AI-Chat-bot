from transformers import pipeline

# Use a Hugging Face model like "distilbert-base-uncased"
chat_model = pipeline('text-generation', model="gpt2")

def generate_answer(query, document_text):
    prompt = f"Based on the document: {document_text}, answer the following query: {query}"
    return chat_model(prompt, max_length=200)[0]['generated_text']
