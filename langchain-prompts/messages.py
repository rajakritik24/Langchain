import os
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

system_message = SystemMessage(content="You are a helpful assistant that can answer questions and help with tasks.")
human_message = HumanMessage(content="What is the capital of France?")

chat_history = [system_message, human_message]
print(model.invoke(chat_history))
