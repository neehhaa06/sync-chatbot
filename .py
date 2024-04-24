# Define a dictionary with sample responses
responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thank you!",
    "bye": "Goodbye, take care!"
}

# Function to get response based on user input
def get_response(user_input):
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

# Main function to interact with the chatbot
def main():
    print("Welcome to SkillSync Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
