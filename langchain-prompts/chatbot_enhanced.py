import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

chat_history = [
    SystemMessage(content="You are a helpful assistant that can answer questions and help with tasks."),
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Exiting...")
        break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)

print("Chat History: ", chat_history)
