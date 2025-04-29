import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from typing import TypedDict, List, Annotated, Literal
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

class Review(TypedDict):
    review: str 
    sentiment: str 

class AnnotatedReview(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review"]
    keywords: Annotated[List[str], "Extract the keywords from the review"]
    pros: Annotated[List[str], "The pros of the review"]
    cons: Annotated[List[str], "The cons of the review"]
    literal_sentiment: Annotated[Literal["pos", "neg", "neutral"], "The sentiment of the review"]

# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
model = ChatOpenAI(model="gpt-4o-mini")

structured_model = model.with_structured_output(AnnotatedReview)

review = "I recently bought this laptop, and I’m blown away by how fast and smooth it is. The display is crystal clear, battery life easily lasts a full day, and the keyboard feels super comfortable. Highly recommend it!"

response = structured_model.invoke(review)
print(response)
print("--------------------------------")
print("Review: ", response["summary"])
print("Sentiment: ", response["sentiment"])