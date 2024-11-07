import openai
import numpy as np
import faiss
import json
import os

# Explicitly set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")  # Replace with your actual API key

# FAISS index setup
embedding_size = 1536  # Adjust based on the embedding model used
index = faiss.IndexFlatL2(embedding_size)  # L2 distance is standard for FAISS
embeddings = []  # Temporarily store embeddings for each entry
responses = []  # Store corresponding answers for retrieval

def get_embedding(text: str) -> np.ndarray:
    """
    Generate an embedding for the input text using OpenAI's API.
    Returns a numpy array of the embedding.
    """
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return np.array(response['data'][0]['embedding'])

def add_to_index(embedding: np.ndarray, response: str):
    """Add a new entry to the FAISS index."""
    global embeddings, responses
    embeddings.append(embedding)
    responses.append(response)
    index.add(np.array(embedding).reshape(1, -1).astype("float32"))

def setup_faiss_index():
    """Load dataset, generate embeddings, and add them to FAISS index."""
    with open("app/data/ulm_dataset.json", "r") as f:
        data = json.load(f)
    for item in data:
        question = item["question"]
        answer = item["answer"]
        embedding = get_embedding(question)
        add_to_index(embedding, answer)

def vector_search(query_embedding: np.ndarray, top_k=1, distance_threshold=0.5):
    """
    Searches the FAISS vector database for the most similar entries.
    Returns the closest response(s) if a match is found.
    
    Args:
        query_embedding (np.ndarray): The embedding of the user's query.
        top_k (int): The number of closest results to return.
        distance_threshold (float): The maximum distance for a result to be considered a match.

    Returns:
        list: A list of the closest responses, or None if no close matches are found.
    """
    if index.ntotal == 0:
        return None

    # Search the FAISS index
    query_vector = query_embedding.reshape(1, -1).astype("float32")  # Make sure the query is in the correct shape
    distances, indices = index.search(query_vector, top_k)
    
    print(f"Search results: Distances: {distances}, Indices: {indices}")
    
    results = []
    for i in range(top_k):
        print(f"Checking distance: {distances[0][i]} with threshold: {distance_threshold}")
        if distances[0][i] < distance_threshold:
            response_index = indices[0][i]
            print(f"Found matching response: {responses[response_index]}")
            results.append(responses[response_index])

    if len(results) == 0:
        print("No results found under the threshold.")
        return None

    return results



