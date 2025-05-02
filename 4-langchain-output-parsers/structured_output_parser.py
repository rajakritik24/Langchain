from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from typing import Union
import os

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

response_schemas = [
    ResponseSchema(name="facts", description="Give me a list of facts about the subject", type='list'),
    ResponseSchema(name="keywords", description="Extract relevant keywords from the fact. This could be a list of words or a single word.", type='list')
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="""
    Generate a list of 3 facts and keywords about {subject}. {format_instructions}.
    """,
    input_variables=["subject"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.format(subject="Cricket")
print("Printing prompt..\n", prompt)

response = model.invoke(prompt)
# print("Printing response..\n", response)

parsed = parser.parse(response.content)
print("Printing parsed response..\n", parsed)
print("--------------------------------")
print(f"Length of facts: {len(parsed['facts'])}")
print("Facts: ", parsed["facts"])

## Doing it through the chain
chain = template | model | parser

response = chain.invoke({"subject": "AI"})
print("Printing response from chain..\n", response)






