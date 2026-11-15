from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = OpenAI(model_name="gpt-6-luna")

result = llm.invoke("What is the capital of India?")

print(result)
