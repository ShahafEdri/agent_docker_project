class ChatbotAgent:
    def __init__(self):
        # Predefined responses
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "how are you": "I'm a bot, so I don't have feelings, but thank you for asking!",
            "what is your name": "I'm a bot created by OpenAI. Nice to meet you!",
            "bye": "Goodbye! Have a nice day!"
        }

    def respond(self, message):
        # Convert message to lowercase
        message = message.lower()

        if message in self.responses:
            return self.responses[message]
        else:
            return "I'm sorry, I didn't understand that. Can you rephrase?"

# Test the chatbot
chatbot = ChatbotAgent()

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print(chatbot.respond(user_input))
        break
    else:
        print("Chatbot: " + chatbot.respond(user_input))
