from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fuzzywuzzy import process  # Install this library with: pip install fuzzywuzzy[speedup]
from app.utils import get_university_info, process_user_input

# Initialize the API router
api_router = APIRouter()

# Define a Pydantic model for the input structure
class PromptInput(BaseModel):
    query: str

# Sample Q&A data for fuzzy matching
answers = {
    "Where is ULM located?": "ULM is located in Monroe, Louisiana, USA, on the banks of the Ouachita River.",
    "What is ULM's mission?": "ULM’s mission is to provide affordable and quality education, fostering personal growth and preparing students for success.",
    # Add more Q&A pairs as needed
}

# Endpoint to return general ULM info
@api_router.get("/getULMInfo")
async def get_info():
    return get_university_info()

# Endpoint to process user input with improved query handling
@api_router.post("/getULMInfo")
async def process_prompt(request: PromptInput):
    query = request.query.strip()
    
    # Check if the query is too short
    if len(query) < 3:
        return {"response": "Your question is too vague. Try asking something like: 'Where is ULM located?' or 'What programs does ULM offer?'"}

    # Fuzzy match the query to find the closest question-answer pair
    best_match, score = process.extractOne(query, answers.keys())
    
    # Set a minimum score threshold to ensure relevance
    if score > 90:
        response = answers[best_match]
    else:
        response = process_user_input(query)  # Fall back to custom processing if no close match found

    return {"response": response}
