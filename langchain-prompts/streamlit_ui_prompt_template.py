import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

st.title("Research paper summarizer")
research_paper = st.selectbox("Select a research paper", ["Attention is all you need", "The Annotated Transformer", "The Annotated GPT"])
summary_length = st.selectbox("Select a summary length", ["Short (10-15 lines)", "Medium (20-30 lines)", "Long (40-50 lines)"])
summary_style = st.selectbox("Select a summary style", ["Mathematical", "Technical", "Narrative"])

## Common way to create a prompt template and use

# template = PromptTemplate(
#     input_variables=["research_paper", "summary_length", "summary_style"],
#     template="""
#     Summarize the following research paper:
#     {research_paper} with {summary_length} and {summary_style}
#     Make sure to include all the important details and equations. Keep it concise and to the point.
#     Include the analogies and metaphors to make it more engaging.
#     """,
#     validate_template=True
# )


template = load_prompt(os.path.join(os.path.dirname(__file__), "prompts", "prompt_template.json"))
prompt = template.invoke({
    "research_paper":research_paper, 
    "summary_length":summary_length, 
    "summary_style":summary_style
})

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

if st.button("Summarize"):
    st.write(model.invoke(prompt).content)







