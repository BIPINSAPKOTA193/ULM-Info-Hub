from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fuzzywuzzy import process
from app.utils import get_embedding, vector_search
import openai
import json
import os

# Initialize the API router
api_router = APIRouter()

class PromptInput(BaseModel):
    query: str

# Load Q&A data from JSON file for fuzzy matching
with open("app/data/ulm_dataset.json", "r") as f:
    data = json.load(f)
    answers = {item["question"]: item["answer"] for item in data}

@api_router.post("/getULMInfo")
async def process_prompt(request: PromptInput):
    try:
        query = request.query.strip()

        if len(query) < 3:
            return {"response": "Your question is too vague. Try asking something like: 'Where is ULM located?' or 'What programs does ULM offer?'"}

            # Step 1: Vector-based search
        query_embedding = get_embedding(query)  # Call get_embedding to get the embedding for the query
        vector_response = vector_search(query_embedding)  # Pass the embedding to vector_search

        if vector_response:
            return {"response": vector_response[0]}  # Return the best response


        # Step 2: Fuzzy matching for predefined answers
        best_match, score = process.extractOne(query, answers.keys())
        if score > 90:
            response = answers[best_match]
        else:
            # Step 3: ChatGPT as fallback
            response = chatgpt_fallback(query)

        return {"response": response}

    except Exception as e:
        # Log the error and return a 500 Internal Server Error response
        print(f"Error processing prompt: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error occurred while processing the prompt.")

def chatgpt_fallback(query: str) -> str:
    """Uses OpenAI's API to answer questions as a fallback."""
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Replace with your actual API key
    chatgpt_prompt = f"Answer the following question based on general knowledge about the University of Louisiana Monroe (ULM):\n\n{query}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in providing information about the University of Louisiana Monroe (ULM)."},
                {"role": "user", "content": chatgpt_prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error with ChatGPT fallback: {e}")
        return "I'm sorry, I couldn't retrieve an answer at the moment."