from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

# Initialize Ollama model
model = OllamaLLM(model="phi3")
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

# Chat context storage
chat_contexts = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    session_id = data.get('session_id', 'default')

    if session_id not in chat_contexts:
        chat_contexts[session_id] = ""

    context = chat_contexts[session_id]

    # Generate response
    result = prompt | model
    response = result.invoke({"context": context, "question": user_input})
    chat_contexts[session_id] += f"\nYou: {user_input}\nSunny: {response}"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
