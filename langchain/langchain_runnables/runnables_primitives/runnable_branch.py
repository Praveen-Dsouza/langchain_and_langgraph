# RunnableBranch is a control flow component in LangChain that allows
# you to conditionally route input data to different chains or 
# runnables based on custom logic.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI(model="gpt-4.1", temperature=0.7)

prompt1 = PromptTemplate(
    template="Write a detailed repport on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser # LCEL

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "Russia Vs Ukraine"})

print(result)
