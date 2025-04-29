from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = ["Cricket: Sachin Tendulkar, often hailed as the 'God of Cricket,' amassed numerous records during his illustrious career, inspiring a generation of players and fans across the globe with his masterful batting.",
"Football: Lionel Messi, the Argentine forward renowned for his extraordinary dribbling and goal-scoring prowess, has won multiple Ballon d'Or awards, cementing his legacy as one of football's all-time greats.",
"Science (Physics): Albert Einstein, a German-born theoretical physicist, fundamentally changed our understanding of the universe with his theory of relativity (E=mc²), becoming an icon of scientific genius.",
"Technology: Steve Jobs, the visionary co-founder of Apple Inc., revolutionized personal technology through iconic products like the Macintosh, iPod, and iPhone, emphasizing intuitive design and user experience.",
"Activism: Malala Yousafzai, a Pakistani advocate for female education and the youngest Nobel Prize laureate, courageously speaks out for the right of all children, especially girls, to receive an education, even after surviving an assassination attempt."
]

query = "What is the most popular sport in the world?"

document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

similarity_matrix = cosine_similarity([query_embedding], document_embeddings) ## Make sure to pass a 2D array

similarity_scores = list(enumerate(similarity_matrix[0]))

sorted_similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

print(f"Query: {query}")
print("-"*100)
print(f"Most Similar Document: {documents[sorted_similarity_scores[0][0]]}")
print("-"*100)
print(f"Similarity Scores: {sorted_similarity_scores[0][1]}")

