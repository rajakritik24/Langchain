import os 
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

class Review(BaseModel):
    review: str 
    sentiment: str 

class PydanticReview(BaseModel):
    summary: str = Field(description="A brief summary of the review")
    sentiment: str = Field(description = "The sentiment of the review")
    keywords: List[str] = Field(description="Extract the keywords from the review")
    pros: Optional[List[str]] = Field(default=None, description="The pros of the review")
    cons: Optional[List[str]] = Field(default=None, description="The cons of the review")
    literal_sentiment: Literal["pos", "neg", "neutral"] = Field(description="The sentiment of the review")

model = ChatOpenAI(model="gpt-4o-mini")

structured_model = model.with_structured_output(PydanticReview)

review = "I recently bought this laptop, and I'm blown away by how fast and smooth it is. The display is crystal clear, battery life easily lasts a full day, and the keyboard feels super comfortable. Highly recommend it!"

response = structured_model.invoke(review)
print(response)
print("--------------------------------")
print(response.model_dump_json())
# print("--------------------------------")
# print("Review: ", response["summary"])
# print("Sentiment: ", response["sentiment"])