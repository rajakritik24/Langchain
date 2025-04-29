import os 
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

## json_schema -> Title and description are mandatory fields when using with_structured_output json schema
json_schema = {
    "title": "ReviewAnalyzer",
    "description": "Analyzes a product review and extracts key information",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "description": "The sentiment of the review"
        },
        "keywords": {
            "type": "array",
            "description": "Extract the keywords from the review",
            "items": {
                "type": "string"
            }
        },
        "pros": {
            "type": "array",
            "description": "The pros of the review",
            "items": {
                "type": "string"
            }
        },
        "cons": {
            "type": "array",
            "description": "The cons of the review",
            "items": {
                "type": "string"
            }
        },
        "literal_sentiment": {
            "type": "string",
            "description": "The sentiment of the review",
            "enum": ["pos", "neg", "neutral"]
        }
    },
    "required": ["summary", "sentiment", "keywords", "literal_sentiment"]
}

model = ChatOpenAI(model="gpt-4o-mini")

structured_model = model.with_structured_output(json_schema)

review = "I recently bought this laptop, and I'm blown away by how fast and smooth it is. The display is crystal clear, battery life easily lasts a full day, and the keyboard feels super comfortable. Highly recommend it!"

response = structured_model.invoke(review)
print(response)
print("--------------------------------")
# print(response.model_dump_json())