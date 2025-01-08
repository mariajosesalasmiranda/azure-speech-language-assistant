const apiBaseUrl = "https://Phi-3-medium-4k-instruct-xwzwa.eastus2.models.ai.azure.com/v1/chat/completions"; // Replace with your endpoint
const apiKey = "L3zgDrSQtiVv5c6wjcAedtFuEOrEA739"; // Replace with your API key
const engine = "Phi-3-medium-4k-instruct-xwzwa"; // Replace with your deployed model name
const apiVersion = "2023-03-15-preview";

let conversationHistory = ""; // To maintain chat context

// Function to call Azure OpenAI API
async function callChatbotAPI(prompt) {
    const url = `${apiBaseUrl}openai/deployments/${engine}/completions?api-version=${apiVersion}`;

    const requestData = {
        prompt: conversationHistory + `User: ${prompt}\nBot:`,
        max_tokens: 100,
        temperature: 0.7,
        top_p: 1.0,
        stop: ["User:", "Bot:"],
    };

    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "api-key": apiKey,
        },
        body: JSON.stringify(requestData),
    });

    const data = await response.json();
    return data.choices[0].text.trim();
}

// Function to send message and display responses
async function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    // Display user message
    addMessage(userInput, "user");

    // Add user input to conversation history
    conversationHistory += `User: ${userInput}\n`;

    // Call the chatbot API
    const botResponse = await callChatbotAPI(userInput);

    // Add bot response to conversation history and display
    conversationHistory += `Bot: ${botResponse}\n`;
    addMessage(botResponse, "bot");

    // Clear input field
    document.getElementById("user-input").value = "";
}

// Function to add messages to the chat interface
function addMessage(message, sender) {
    const messagesDiv = document.getElementById("messages");
    const messageDiv = document.createElement("div");
    messageDiv.className = sender;
    messageDiv.textContent = message;
    messagesDiv.appendChild(messageDiv);

    // Scroll to the bottom
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
