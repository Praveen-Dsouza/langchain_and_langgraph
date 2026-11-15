from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load environment variables from .env file
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Embed the documents
document_embeddings = embedding.embed_documents(documents)

# Query to find similar documents
query = "tell me about ms dhoni?"

document_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Calculate cosine similarity between the query embedding and document embeddings
score = cosine_similarity([query_embedding], document_embeddings)[0]

index, score = sorted(list(enumerate(score), key=lambda x: x[1], reverse=True))

print(query)
print(documents[index])
print("Similarity Score:", score)

