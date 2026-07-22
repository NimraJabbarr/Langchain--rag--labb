from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=320)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of web",
    "Islamabad is the capital of Pakistan",
    "My name is Nimra Jabbar",
    "I am student of BSSE4"
]

query = "tell me the capital of pakistan"

# Generate embeddings
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Compute cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Sort scores in descending order
sorted_scores = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[:3]

# Best match
index, score = sorted_scores[0]
print("Best match:", documents[index])
print("Similarity score:", score)
print("Query:", query)
