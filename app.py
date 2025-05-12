# Import necessary classes from the flask library
from flask import Flask, request, jsonify

# --- Simple Chatbot Logic ---
# For this PoC, we'll use basic keyword matching.
# For more complex bots, you'd integrate NLU libraries or services here.

def get_chatbot_response(user_message):
    """
    Generates a simple chatbot response based on the user's message.
    """
    user_message = user_message.lower() # Convert message to lowercase for easier matching

    if "hello" in user_message or "hi" in user_message:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_message:
        return "I'm a computer program, so I don't have feelings, but I'm ready to chat!"
    elif "news" in user_message:
        # In a real application, you'd fetch news here.
        # For a PoC, we'll give a canned response.
        return "I can tell you about general topics and news. What specifically are you interested in?"
    elif "what is your name" in user_message:
        return "I am a simple chatbot created for demonstration purposes."
    elif "bye" in user_message or "goodbye" in user_message:
        return "Goodbye! Have a great day."
    else:
        return "I'm still learning! Can you tell me more about what you'd like to discuss?"

# --- Flask Application Setup ---

# Create an instance of the Flask application.
app = Flask(__name__)

# Define the route for the root URL ('/').
@app.route('/')
def index():
    """
    This function serves the main HTML content including the chat interface.
    """
    # HTML content to display including the chat interface
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chatbot Integration PoC</title>
        <style>
            body {
                font-family: sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
                color: #333;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px; /* Add some space below the container */
            }
            h1 {
                color: #555;
                margin-bottom: 20px;
            }
            img, iframe {
                margin: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                max-width: 100%;
                height: auto;
            }
            iframe {
                 width: 784px;
                 height: 441px;
                 max-width: 100%;
                 aspect-ratio: 16 / 9;
            }
            #chat-box {
                border: 1px solid #ccc;
                height: 300px;
                width: 400px;
                overflow-y: scroll;
                padding: 10px;
                margin-top: 20px;
                text-align: left; /* Align chat messages to the left */
                display: flex;
                flex-direction: column; /* Stack messages vertically */
            }
            .message {
                margin-bottom: 10px;
                padding: 8px;
                border-radius: 5px;
                max-width: 80%; /* Limit message width */
                word-wrap: break-word; /* Break long words */
            }
            .user-message {
                background-color: #dcf8c6; /* Light green for user messages */
                align-self: flex-end; /* Align user messages to the right */
            }
            .bot-message {
                background-color: #e5e5ea; /* Light grey for bot messages */
                align-self: flex-start; /* Align bot messages to the left */
            }
            #user-input {
                margin-top: 10px;
                width: calc(100% - 70px); /* Adjust width to fit button */
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            #send-button {
                margin-top: 10px;
                padding: 8px 15px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
             #send-button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Test page by Shibin Antony Boban.</h1>
            <p>This is Proof of Concept</p>

            <iframe width="784" height="441" src="https://www.youtube-nocookie.com/embed/AyzJyWGqm0c?si=oEckVtcRg3zhFTwT&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

            <img src="https://centralofsuccess.com/wp-content/uploads/2017/11/There-is-simply-no-substitute-for-hard-work-when-it-comes-to-achieving-success..png" alt="Placeholder Image 1">
            <img src="https://theinspiringjournal.com/wp-content/uploads/2023/04/keep-working-hard-quotes.jpg" alt="Placeholder Image 2">
            <img src="https://placehold.co/400x250/3357FF/white?text=Image+3" alt="Placeholder Image 3">

            <div id="chat-container">
                <h2>Simple Chatbot</h2>
                <div id="chat-box">
                    <div class="message bot-message">Hello! Ask me about general topics or news.</div>
                </div>
                <input type="text" id="user-input" placeholder="Type your message...">
                <button id="send-button">Send</button>
            </div>

        </div>

        <script>
            const chatBox = document.getElementById('chat-box');
            const userInput = document.getElementById('user-input');
            const sendButton = document.getElementById('send-button');

            function sendMessage() {
                const message = userInput.value.trim();
                if (message === "") {
                    return; // Don't send empty messages
                }

                // Display user message
                appendMessage(message, 'user-message');

                // Clear the input field
                userInput.value = '';

                // Send message to backend
                fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: message })
                })
                .then(response => response.json())
                .then(data => {
                    // Display bot response
                    appendMessage(data.response, 'bot-message');
                })
                .catch(error => {
                    console.error('Error sending message:', error);
                    appendMessage("Error: Could not get a response.", 'bot-message');
                });
            }

            function appendMessage(message, type) {
                const messageElement = document.createElement('div');
                messageElement.classList.add('message', type);
                messageElement.textContent = message;
                chatBox.appendChild(messageElement);
                // Auto-scroll to the bottom
                chatBox.scrollTop = chatBox.scrollHeight;
            }

            // Send message on button click
            sendButton.addEventListener('click', sendMessage);

            // Send message on Enter key press in the input field
            userInput.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    event.preventDefault(); // Prevent default form submission
                    sendMessage();
                }
            });
        </script>

    </body>
    </html>
    """
    return html_content

# Define the new route for handling chat messages
@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles incoming chat messages and returns a chatbot response.
    """
    data = request.get_json() # Get JSON data from the request
    user_message = data.get('message', '') # Extract the message

    # Get the chatbot's response
    bot_response = get_chatbot_response(user_message)

    # Return the response as JSON
    return jsonify({'response': bot_response})

# This block allows you to run the Flask application locally for testing
if __name__ == '__main__':
    # Run the Flask development server.
    # For production on Azure, you would typically rely on the WSGI server (Gunicorn)
    # to bind to the correct port specified by Azure.
    app.run(host='0.0.0.0', port=8080)
