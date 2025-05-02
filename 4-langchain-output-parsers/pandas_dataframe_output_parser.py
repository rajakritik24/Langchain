from dotenv import load_dotenv
import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PandasDataFrameOutputParser
from langchain_core.prompts import PromptTemplate

# Load .env variables
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Define model and parser
model = ChatOpenAI(model="gpt-4o", temperature=0.7)
parser = PandasDataFrameOutputParser(dataframe=pd.DataFrame(columns=["name", "age", "gender", "address"]))

# Create template first (without partials)
template = PromptTemplate(
    template="""
    Provide a markdown table with 3 {race} people.
    
    - Use the columns: name, age, gender, address (all lowercase).
    - Do not include any explanation.
    - Only return the table.

    {format_instructions}
    """,
    input_variables=["race", "format_instructions"],
)

# Apply partial variables manually
prompt = template.partial(format_instructions=parser.get_format_instructions())

# Chain
chain = prompt | model | parser

# Run
response = chain.invoke({"race": "South American"})
print(response)

## Code could fail sometimes due to error in the parser, which is not able to parse the output.


