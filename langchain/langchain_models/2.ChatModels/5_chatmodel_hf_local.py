from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Set the cache directory for Hugging Face models
os.environ["HF_HOME"] = "D:/langchain_and_langgraph/langchain/huggingface_cache"  # Set the cache directory for Hugging Face models

llm = HuggingFacePipeline.from_model_id(
        model_id="mistralai/Mistral-7B-v0.1",
        task="text-generation",
        pipeline_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 100
            }
    )

model = ChatHuggingFace(
    llm=llm
)

result = model.invoke("What is the capital of India?")

print(result.content)