async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (!message) {
        return;
    }

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = message;

    chatBox.appendChild(userMessage);

    input.value = "";

    // Display typing message
    const loadingMessage = document.createElement("div");
    loadingMessage.className = "message bot";
    loadingMessage.textContent = "Typing...";

    chatBox.appendChild(loadingMessage);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        loadingMessage.textContent = data.reply;

    } catch (error) {

        loadingMessage.textContent =
            "Unable to connect to the chatbot. Please try again.";

    }

    chatBox.scrollTop = chatBox.scrollHeight;
}


function clearChat() {

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML = `
        <div class="message bot">
            Hello! 👋 I'm your medical information assistant.
            <br><br>
            You can ask me about common topics such as fever, cold,
            cough, headache, diabetes, allergies, and more.
        </div>
    `;
}


document.getElementById("user-input").addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    }
);