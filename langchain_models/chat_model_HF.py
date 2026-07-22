# 4_chatmodel.py
# Example: Using Hugging Face model with LangChain (Local pipeline)
# Using HuggingFacePipeline with transformers (local inference) instead of
# HuggingFaceEndpoint (HTTP API) because huggingface-hub v1.22.0 has a
# known bug causing "StopIteration" in provider auto-detection.

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.messages import HumanMessage, SystemMessage


# Step 1: Load a small local model via transformers pipeline
# "gpt2" is small (~500MB) and works offline once downloaded
local_pipeline = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=150,
    temperature=0.7,
    top_p=0.95,
    pad_token_id=50256  # GPT-2 specific EOS token ID
)

# Step 2: Wrap the pipeline with LangChain's LLM interface
llm = HuggingFacePipeline(pipeline=local_pipeline)

# Step 3: Test the model with a simple query
response = llm.invoke("What is the capital of India?")
print(response)
