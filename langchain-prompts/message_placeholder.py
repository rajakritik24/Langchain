from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_history = MessagesPlaceholder(variable_name="chat_history")

prompt = ChatPromptTemplate(
    [('system', 'You are a helpful assistant. You are given a conversation history and a new question. You need to answer the question based on the conversation history.'),
     chat_history,
     ('human', '{query}')]
)

chat_history = []
with open('chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())

# print(chat_history)
print(prompt.invoke({"chat_history": chat_history, "query": "Where is my refund?"}))