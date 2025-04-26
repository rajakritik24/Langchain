from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", max_tokens=15, temperature=0.5)
result = model.invoke("Describe cricket in a sentence.")
print(result.content)