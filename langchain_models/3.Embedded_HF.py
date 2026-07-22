from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

result = embedding.embed_query("Delhi is the capital of India")
print(result[:10])  # just print first 10 numbers for readability
