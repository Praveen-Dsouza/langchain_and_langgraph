from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Text to be embedded
# text = "Delhi is the capital of India."

# vector = embedding.embed_query(text)

# Documents embedding
documents =[
    "Delhi is the capital of India."
    "Kolkata is the capital of West Bengal."
    "Mumbai is the capital of Maharashtra."
    ]

result = embedding.embed_documents(documents)

print(str(result))
 