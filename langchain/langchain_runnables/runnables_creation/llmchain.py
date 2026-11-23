from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# 1. Initialize the LLM
llm = ChatOpenAI(model="gpt-4.1", temperature=0.7)

# 2. Create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],  # Defines the required input variable
    template="Suggest a catchy blog title about {topic}."
)


# 3. Create an LCEL chain
# Connect the prompt template with the LLM
chain = prompt | llm


# 4. Run the chain with a specific topic
topic = input("Enter a topic: ")

# Pass the input to the chain
response = chain.invoke({"topic": topic})


# 5. Print the generated output
print("Generated Blog Title:", response.content)
