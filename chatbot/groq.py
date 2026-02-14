from groq import Groq

# Put your API key directly for now
client = Groq(api_key="api-key")

print("🤖 Groq AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Bye 👋")
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    print("Chatbot:", response.choices[0].message.content)
