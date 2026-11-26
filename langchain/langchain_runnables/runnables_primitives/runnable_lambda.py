# RunnableLambda is a runnable primitive that allows you to 
# "apply custom python functions" within an AI pipeline.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

# Load environment variables from .env file
load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatOpenAI(model="gpt-4.1", temperature=0.7)

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count) # pass function
    # "word_count": RunnableLambda(lambda x: len(x.split())) 
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

final_result = """"{} \n word count - {}""".format(result["joke"], result["word_count"])

print(final_result)
