import os
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI

"""
Steps to replicate this example:
(See updated setup instructions below the code)
"""

# #Load environment variables from .env file (for GOOGLE_API_KEY)
load_dotenv()

# --- Setup Firebase Firestore ---
PROJECT_ID = "langchain-8b399"  # Your Google Cloud/Firebase Project ID
SESSION_ID = "user_session_gemini_1"  # A unique ID for the conversation
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# --- Initialize Google Gemini AI Model ---
# This is the main change from the original code
print("Initializing Google Gemini Model...")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
print("Model Initialized.")

print("\nStart chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    # Add user message to Firestore history
    chat_history.add_user_message(human_input)

    # Invoke the model with the entire chat history
    ai_response = model.invoke(chat_history.messages)
    
    # Add AI response to Firestore history
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")