def get_response(message):
    message = message.lower()
    if message == "hi":
        return "Namaskar!"
    elif "how are you" in message:
        return "I am as cool as Thala!"
    elif "your name" in message:
        return "I'm FunBot."
    elif "tell me the president of india" in message:
        return "The President of India is Droupadi Murmu."
    elif "which country won t20 world cup of 2024" in message:
        return "Mera pyara Bharat!"
    elif "can i go" in message:
        return "To jana roka kisne hai?"
    else:
        return "I'm sorry, I don't understand that question."

def main():
    print("Welcome to FunBot!")
    print("You can start chatting with me. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("FunBot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print("FunBot:", response)

if __name__ == "__main__":
    main()
