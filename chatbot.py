from gpt4all import GPT4All

gpt_model = GPT4All("gpt4all-lora-quantized")

small_talk_responses = {
    "how are you": "I'm doing great! How can I assist you with your academic needs today?",
    "what's your name": "I'm your academic assistant, here to help you succeed.",
    "tell me a joke": "Why did the student bring a ladder to school? To go to high school!"
}

def handle_small_talk(user_input):
    for phrase in small_talk_responses:
        if phrase in user_input.lower():
            return small_talk_responses[phrase]
    return None

def generate_conversational_answer(query, document_text):
    prompt = f"You're a friendly, professional academic assistant. Here’s the context: {document_text}. Now, answer the query politely: '{query}'."
    return gpt_model.generate(prompt)

def chatbot_conversation(user_name, query, document_text):
    small_talk_response = handle_small_talk(query)
    if small_talk_response:
        return f"{small_talk_response} Anything else I can help you with today?"

    # Generate an answer based on the documents
    answer = generate_conversational_answer(query, document_text)
    if answer:
        return f"Hi {user_name}, here’s what I found: {answer}"
    else:
        return "Sorry, I couldn't find anything. Could you ask that differently?"
