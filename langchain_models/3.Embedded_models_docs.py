from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
documents=[
                    "Delhi is the capital of India"
                    "Kolkata is the capital of web"
                    "islamabad is the capital of pakistan"
]
# Correct spelling + proper dimensions argument
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_documents(documents)
print(str(result))