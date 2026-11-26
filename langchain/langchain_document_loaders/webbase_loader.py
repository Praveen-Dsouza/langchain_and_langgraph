# WebBaseLoader is a document loader in LangChain used to load and 
# extract text content from web page(URLs).

from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.in/s?k=samsung+s26+ultra&crid=30YJCWXCU7WS4&sprefix=sam%2Caps%2C495&ref=nb_sb_ss_mvt-t11-ranker_4_3"
loader = WebBaseLoader(url)

model = ChatOpenAI(model="gpt-4.1", temperature=0.7)

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({"question": "What is the peak brightness of this product?", "text": docs[0].page_content})

print(result)