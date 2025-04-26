from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
documents = [
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?",
]
document_embeddings = embeddings.embed_documents(documents)
print(len(document_embeddings))
print(document_embeddings[0])