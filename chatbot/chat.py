from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model="phi3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_convervation():
    context = ""
    print("Welcome to SoundBridge! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Sunny: ", result)
        context += f"\nYou: {user_input}\nSunny: {result}"
    
if __name__ == "__main__":
    handle_convervation()
