const apiUrl = "http://127.0.0.1:5000/chat"; // URL of your Flask API
let sessionId = "default"; // Unique session ID (could use UUID for real applications)

async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Add user message to chat
    addMessage("user", userInput);

    // Clear input field
    document.getElementById("user-input").value = "";

    // Send request to backend
    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userInput, session_id: sessionId })
        });

        const data = await response.json();
        addMessage("bot", data.response);
    } catch (error) {
        console.error("Error communicating with backend:", error);
        addMessage("bot", "Sorry, there was an error. Please try again.");
    }
}

function addMessage(sender, text) {
    const messagesDiv = document.getElementById("messages");

    const messageDiv = document.createElement("div");
    messageDiv.className = sender; // 'user' or 'bot'
    messageDiv.textContent = text;

    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
