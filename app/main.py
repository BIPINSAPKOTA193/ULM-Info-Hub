from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api_router

# Initialize FastAPI app
app = FastAPI()

# Root route for testing
@app.get("/")
def read_root():
    return {"Hello": "World"}

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Register the routes
app.include_router(api_router)

# Run this script to start the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000, reload=True)
