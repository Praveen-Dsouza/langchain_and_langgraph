# Convert LLM component classes to runnables, to have a common structure

import random
from abc import ABC, abstractmethod

# Runnable abstract class
class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

class FakeLLM(Runnable):
    def __init__(self):
        print("LLM created")

    def invoke(self, prompt):
        response_list = [
                    "Delhi is the capital of India",
                    "IPL is a cricket league",
                    "AI stands for Artificial Intelligence"
                ]
        
        return {"response": random.choice(response_list)}
    
    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]

        return {"response": random.choice(response_list)}

class FakePromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)

class FakeStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data["response"]

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            # storing previous step output into cuurent input
            input_data = runnable.invoke(input_data)

        return input_data
    

template = FakePromptTemplate(
    template="Write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)

llm = FakeLLM()

parser = FakeStrOutputParser()

# chain = RunnableConnector([prompt, llm])
chain = RunnableConnector([template, llm, parser])

result = chain.invoke({"length": "long", "topic": "India"})

print(result)

template1 = FakePromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

template2 = FakePromptTemplate(
    template="Explain the following joke {response}",
    input_variables=["response"]
)

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])

result = final_chain.invoke({"topic": "AI"})

print("final result:", result)
