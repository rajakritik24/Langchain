import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

# Example: prompt -> LLM -> Essay -> LLM -> Summary

## Step 1: Prompt -> LLM -> Essay
essay_prompt_template = PromptTemplate(
    template="""
    Write an essay about {topic}
    """,
    input_variables=["topic"]
)

essay_prompt = essay_prompt_template.format(topic="AI")
essay = model.invoke(essay_prompt)
essay_content = essay.content
print("Essay generated..")


## Step 2: Essay -> LLM -> Summary
print("Generating summary..")
summary_prompt_template = PromptTemplate(
    template="""
    Write a concise summary of the following essay:
    {essay}
    """,
    input_variables=["essay"]
)

summary_prompt = summary_prompt_template.format(essay=essay_content)
summary = model.invoke(summary_prompt)
summary_content = summary.content

print(summary_content)

## Using StrOutputParser

parser = StrOutputParser()
chain = essay_prompt_template | model | parser | summary_prompt_template | model | parser

result = chain.invoke({"topic": "AI"})
print(result)







