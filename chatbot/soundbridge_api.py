import requests

# Azure OpenAI Deployment Details
API_BASE_URL = "https://ai-mariajosesalasmiranda-6808.openai.azure.com/"  # Replace with your endpoint base URL
DEPLOYMENT_NAME = "Phi-3-medium-4k-instruct-xwzwa"  # Replace with your deployment name
API_VERSION = "2023-03-15-preview"  # Use the API version specific to your deployment
API_KEY = "4L95rUetZClDjVWMkZiDENE7ju1Oka8IHpXTDLZTcyd63x2zxJlMJQQJ99ALACHYHv6XJ3w3AAAAACOG3REc"  # Replace with your API key

# Function to interact with the deployed model
def query_model(prompt, max_tokens=1000, temperature=0.7):
    """
    Queries the Azure OpenAI deployment and returns the response.

    :param prompt: The input prompt to send to the model
    :param max_tokens: The maximum number of tokens in the response
    :param temperature: Sampling temperature (creativity level)
    :return: Response from the model
    """
    url = f"{API_BASE_URL}openai/deployments/{DEPLOYMENT_NAME}/completions?api-version={API_VERSION}"
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 1.0,
        "stop": ["User:", "Bot:"],  # Adjust based on your specific needs
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    print("Welcome to SoundBridge!")
    print("Type 'exit' to end the session.\n")
    
    conversation_history = ""  # To maintain context

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Append user input to the conversation history
        conversation_history += f"User: {user_input}\n"

        # Query the model
        response = query_model(conversation_history)

        if response:
            print(f"SoundBridge: {response}")
            # Append bot response to the conversation history
            conversation_history += f"Bot: {response}\n"
        else:
            print("SoundBridge: Sorry, I couldn't process your request.")
