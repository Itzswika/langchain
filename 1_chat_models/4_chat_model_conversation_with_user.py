# Imports for Google Gemini
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# #Load environment variables (needs GOOGLE_API_KEY in .env)
load_dotenv()

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# The rest of the code is identical as it uses standard LangChain components
chat_history = []

# Set an initial system message
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"AI: {response}")

print("\n---- Message History ----")
print(chat_history)