# Problem langchain team faced while creating multiple libraries

import random

class FakeLLM:
    def __init__(self):
        print("LLM created")

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

    def format(self, input_dict):
        return self.template.format(**input_dict)

class FakeLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result["response"]

template = FakePromptTemplate(
    template="Write a {length} poem about {topic}",
    input_variables=["length", "topic"]
)

# prompt = template.format({"length": "short", "topic": "India"})

llm = FakeLLM()

chain = FakeLLMChain(llm, template)

result = chain.run({"length": "short", "topic": "India"})

print("result: ", result)