from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api_router
import os
import openai
from dotenv import load_dotenv


load_dotenv()

import dotenv

config = dotenv.dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

# Initialize FastAPI app
app = FastAPI()
# Root route for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the ULM Information Hub API!"}

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins in production, e.g., ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Register the routes
app.include_router(api_router)

# Run this script to start the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=3000,
        reload=True,  # Set to False in production
        log_level="info"  # Use "warning" or "error" in production for less verbosity
    )
