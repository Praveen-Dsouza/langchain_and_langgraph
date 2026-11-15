from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Mumbai is the capital of Maharashtra."
]

result = embedding.embed_documents(documents)

print(str(result))