import requests
import time

# API Endpoint and Headers
url = "https://api.hyperbolic.xyz/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjaGlhaW11dDk0QGdtYWlsLmNvbSJ9.B6qDIppKFykhCTPxPX_zc40l3P0T-A4VK_m4qFd3G-w"  # Replace with your actual API key
}

# Function to send a message to the chatbot
def chat_with_ai(message, chat_history=[]):
    chat_history.append({"role": "user", "content": message})  # Append user message

    payload = {
        "messages": chat_history,
        "model": "Qwen/QwQ-32B",  # Replace with your desired model
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        ai_reply = response.json()["choices"][0]["message"]["content"]
        chat_history.append({"role": "assistant", "content": ai_reply})  # Append AI response
        return ai_reply, chat_history
    else:
        return f"Error {response.status_code}: {response.text}", chat_history

# Automated Chat Loop
chat_history = []
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    ai_response, chat_history = chat_with_ai(user_input, chat_history)
    print(f"Chatbot: {ai_response}")

    time.sleep(1)  # Pause to simulate response time
