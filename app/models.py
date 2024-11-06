from pydantic import BaseModel

class UniversityInfo(BaseModel):
    name: str
    location: str
    established: str
    campus: str
    website: str

class UserPrompt(BaseModel):
    prompt: str
