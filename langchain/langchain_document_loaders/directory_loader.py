# DirectoryLoader is a document loader that lets you load multiple 
# documents from a directory(folder) or files.

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

print(len(docs))

print(docs[325].page_content)
print(docs[325].metadata)