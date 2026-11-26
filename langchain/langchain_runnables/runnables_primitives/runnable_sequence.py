# Runnable Sequence is a sequential chain of runnables in LangChain 
# that executes each step one after another, passing the output of 
# one step as the input to the next

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI(model="gpt-4.1", temperature=0.7)

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=["text"]
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "AI"})

print(result)

# LCEL (LangChain Expression Language)
# We can pass RunnableSequence as r1 | r2 | r3 using pipe operator