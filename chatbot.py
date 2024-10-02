from transformers import pipeline

# Use a Hugging Face model like "gpt2"
chat_model = pipeline('text-generation', model="gpt2")

def generate_conversational_answer(query, document_text):
    prompt = f"You're a friendly academic assistant. {document_text}. Now answer the query politely: '{query}'."
    return chat_model(prompt, max_length=200)[0]['generated_text']
