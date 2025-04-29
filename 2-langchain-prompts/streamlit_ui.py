import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os 
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

st.header("Research paper summarizer")

user_input = st.text_input("Enter your research paper here")
if user_input and st.button("Summarize"):
    st.write(model.invoke(user_input).content)











