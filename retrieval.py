import numpy as np
from openai import OpenAI
from data import documents

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Creating document embeddings...")
doc_embeddings = [get_embedding(doc) for doc in documents]
print("Ready.\n")

def search_documents(query, top_k=3):
    query_embedding = get_embedding(query)

    similarities = [
        cosine_similarity(query_embedding, doc_embedding)
        for doc_embedding in doc_embeddings
    ]

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    return [documents[i] for i in top_indices]