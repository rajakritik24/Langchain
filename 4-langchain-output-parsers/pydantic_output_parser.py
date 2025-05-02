from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt=18, lt=100, description="The age of the person")
    gender: str = Field(description="The gender of the person")
    address: str = Field(description="The address of the person")

class PersonList(BaseModel):
    people: list[Person] = Field(description="A list of people")

parser = PydanticOutputParser(pydantic_object=PersonList)
template = PromptTemplate(
    template="""Give me a list of 3 {race} people. {format_instructions}""",
    input_variables=["race"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.format(race="Asian")
print("Printing prompt..\n", prompt)

print("****************************")
print("Response from LLM:")
response = model.invoke(prompt)
print(parser.parse(response.content).model_dump_json())
print(parser.parse(response.content))

print("****************************")

# Using chain 
print("Output using chains: ")
chain = template | model | parser
response = chain.invoke({"race": "Europian"})
# print(response.content)
print(response.model_dump_json())
print(response)


