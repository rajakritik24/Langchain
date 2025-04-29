from langchain_core.prompts import ChatPromptTemplate

prompt_1 = ChatPromptTemplate.from_template("Translate the following into {language}: {text}")
print(prompt_1.invoke({"language": "French", "text": "I love programming in Python"}))

prompt_2 = ChatPromptTemplate(
    messages=[
        ("system", "Translate the following into {language}: {text}"),
        ("human", "{text}"),
    ]
)
print(prompt_2.invoke({"language": "French", "text": "I love programming in Python"}))

prompt_3 = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "Translate the following into {language}: {text}"),
        ("human", "{text}"),
    ]
)
print(prompt_3.invoke({"language": "French", "text": "I love programming in Python"}))
