import nltk
import random
import string
import re
# Download the NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Preprocessing  the functions
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Responses sample
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Greetings! How may I assist you?", "How can I help you sir!!"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!","See you soon", "Take care!", "Have a good day!!", "Nice to meet you"],
    "thanks": ["You're welcome!", "No problem!", "Most welcome!!", "Fine, All Good"],
    "default": ["I'm not sure. Can you rephrase again?", "Could you elaborate on?", "I'm here to help, but I need more information.", "You tell me again, I don't understand??", "I need more information to hepling you!!"]
}

# Function can determine intent of the user's msg!!
def get_intent(user_input):
    user_input = preprocess_text(user_input)
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "greeting"
    elif "bye" in user_input:
        return "goodbye"
    elif "thank" in user_input:
        return "thanks"
    else:
        return "default"

# Chatbot function is here!!
def chatbot():
    print("Chatbot: Hi!! I'm your friendly chatbot. Type the 'exit' you can end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye & Great meet with you!!")
            break
        
        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()