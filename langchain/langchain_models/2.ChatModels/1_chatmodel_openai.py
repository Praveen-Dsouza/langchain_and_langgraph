from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model="gpt-6-luna", temperature=0, max_completion_tokens=10)

result = model.invoke("Suggest me 5 indian cuisines")

print(result.content)