# RunnablePassthrough is a special Runnable primitive that simply 
# returns the input as output without modifying it.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI(model="gpt-4.1", temperature=0.7)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=["text"]
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

joke_gen_chain.invoke({"topic": "AI"})

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)