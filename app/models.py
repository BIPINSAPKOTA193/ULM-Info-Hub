from pydantic import BaseModel
import openai
import os
import numpy as np
# Explicitly set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set; raise an error if not (useful for testing)
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set. Please configure it explicitly.")

# Define data models for structured information
class UniversityInfo(BaseModel):
    name: str
    location: str
    established: str
    campus: str
    website: str

class UserPrompt(BaseModel):
    prompt: str

def get_embedding(text: str) -> np.ndarray:
    """
    Generate an embedding for the input text using OpenAI's API.
    Returns a numpy array of the embedding.
    """
    try:
        response = openai.Embedding.create(
            input=[text],  # Wrap text in a list for compatibility
            model="text-embedding-ada-002"  # Model name remains the same
        )
        return np.array(response['data'][0]['embedding'])
    except Exception as e:
        print(f"Error generating embedding: {e}")
        raise
