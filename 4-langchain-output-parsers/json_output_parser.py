import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

## Example of using partial variable, there are inputs that need to be filled in earlier.

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
prompt_template = PromptTemplate(
    template="""Hi my name is {name} and my hobby is {hobby}.""",
    input_variables=["name","hobby"],
    partial_variables={"name": "Ritik"} # This is a partial variable, it is not a variable that is passed in the input.
)

prompt = prompt_template.format(hobby="Coding")
# print(prompt)

parser = JsonOutputParser()

## Using JSON output parser
template = PromptTemplate(
    template="Generate name, hobby and address of a fictional character. {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
prompt = template.format()
print(prompt)
response = model.invoke(prompt)
print(parser.parse(response.content))

## Easier way to do this
chain = template | model | parser
print(chain.invoke({}))


new_prompt = PromptTemplate.from_template("Generate a joke about {subject}. \
                                          The response object should have only joke and punchline \
                                          as keys. {format_instructions}")
new_prompt = new_prompt.partial(format_instructions=parser.get_format_instructions())
new_chain = new_prompt | model | parser
print(new_chain.invoke({"subject": "Coding"}))








