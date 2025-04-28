import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(f"{user_input}")
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Exiting...")
        break
    response = model.invoke(chat_history)
    chat_history.append(f"{response.content}")
    print("AI: ", response.content)

print("Chat History: ", chat_history)