from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# 1. Initialize the LLM
# ChatOpenAI is used to generate answers using an OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.7
)


# 2. Load the document
# TextLoader reads the content from docs.txt
loader = TextLoader("docs.txt", encoding="utf-8")
documents = loader.load()


# 3. Split the document into smaller chunks
# chunk_size = maximum characters in each chunk
# chunk_overlap = number of overlapping characters between chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)


# 4. Convert text into embeddings and store them in FAISS
# OpenAIEmbeddings converts text into numerical vectors
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# FAISS stores the generated vectors for similarity search
vectorstore = FAISS.from_documents(
    docs,
    embeddings
)


# 5. Create a retriever
# The retriever fetches relevant document chunks based on a query
retriever = vectorstore.as_retriever()


# 6. Define the user query and retrieve relevant documents
query = "What are the key takeaways from the document?"

# invoke() retrieves the relevant documents from the vector store
retrieved_docs = retriever.invoke(query)


# 7. Combine retrieved document content into a single string
# This text will be passed to the LLM as context
retrieved_text = "\n".join(
    [doc.page_content for doc in retrieved_docs]
)


# 8. Create a prompt using the retrieved context and user query
prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"

# 9. Pass the prompt to the LLM
# invoke() is the modern LangChain method for calling chat models
answer = llm.invoke(prompt)


# 10. Print the generated answer
# response.content extracts the actual text from the AIMessage
print("Answer:", answer.content)
