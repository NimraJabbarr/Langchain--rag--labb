
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Initialize LLM with OpenRouter key
model = ChatOpenRouter(
    model="openai/gpt-3.5-turbo-instruct",   # model name OpenRouter format mein
    api_key=os.getenv("OPENROUTER_API_KEY")  # yahan tumhari OpenRouter key hogi
)

# Run query
result = model.invoke("What is the capital of Pakistan")
print(result)
