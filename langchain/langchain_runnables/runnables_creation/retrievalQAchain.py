from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Load the document
# TextLoader reads the content from docs.txt
loader = TextLoader("docs.txt", encoding="utf-8")
documents = loader.load()


# 2. Split the document into smaller chunks
# chunk_size = maximum characters in each chunk
# chunk_overlap = overlapping characters between chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# 3. Convert text into embeddings and store in FAISS
# Embeddings convert text into numerical vectors
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# FAISS stores the vectors for similarity searching
vectorstore = FAISS.from_documents(docs, embeddings)

# 4. Create a retriever
# Retrieves relevant document chunks based on the question
retriever = vectorstore.as_retriever()

# 5. Initialize the LLM
llm = ChatOpenAI(model="gpt-4.1", temperature=0.7)

# 6. Create the RetrievalQA chain
# chain_type="stuff" combines retrieved documents into one context
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# 7. Ask a question
query = "What are the key takeaways from the document?"

# Invoke the RetrievalQA chain
# The input key for RetrievalQA is "query"
response = qa_chain.invoke({"query": query})

# 8. Print the generated answer
# RetrievalQA returns the answer under the "result" key
print("Answer:", response["result"])
