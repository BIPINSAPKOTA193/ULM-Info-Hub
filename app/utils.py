import json

# Load ULM dataset (question-answer pairs)
def load_ulm_dataset():
    with open("app/data/ulm_dataset.json", "r") as file:
        return json.load(file)

def get_university_info():
    # Return the entire dataset of Q&A
    return load_ulm_dataset()

def process_user_input(prompt: str):
    # Load dataset
    dataset = load_ulm_dataset()

    # Search for a matching question
    for entry in dataset:
        if prompt.lower() in entry['question'].lower():
            return entry['answer']
    
    # Default response if no match is found
    return "Sorry, I don't have an answer to that question."
