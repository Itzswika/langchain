## 1. Make sure you have installed the necessary library:
# pip install langchain-google-genai python-dotenv

# 2. Import the required libraries
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 3. Load the environment variables from your .env file
# This function looks for the .env file and loads the GOOGLE_API_KEY
load_dotenv()

# 4. Initialize the ChatGoogleGenerativeAI model
# This line is the crucial change - it tells the script to use Google
print("Initializing Google Gemini model...")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 5. Invoke the model with your question
print("Sending request to Gemini...")
result = model.invoke("What is 81 divided by 9?")

# 6. Print the results
print("\n--- Full Result ---")
print(result)

print("\n--- Content Only ---")
print(result.content)

