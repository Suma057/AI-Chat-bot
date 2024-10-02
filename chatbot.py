from gpt4all import GPT4All

gpt_model = GPT4All("gpt4all-lora-quantized")

def generate_answer(query, document_text):
    prompt = f"Based on the document: {document_text}, answer the following query: {query}"
    return gpt_model.generate(prompt)
