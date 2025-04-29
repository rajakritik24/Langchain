from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "What is the capital of France?"
print("Length of embedding: ", len(embeddings.embed_query(text)))
print(embeddings.embed_query(text))

documents = [
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?",
]

document_embeddings = embeddings.embed_documents(documents)
print("Length of document embeddings: ", len(document_embeddings))
print(document_embeddings[0])