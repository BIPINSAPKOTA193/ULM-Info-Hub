# 🎓 ULM Information Hub

Welcome to the **ULM Information Hub**! This project is a FastAPI-based web application designed to answer frequently asked questions about the University of Louisiana Monroe (ULM). Users can type questions into the front-end interface and receive responses from a predefined dataset or through intelligent matching.

---

## 🌟 Features

- **📖 Ask Questions about ULM**: Type a question, and the app provides relevant answers about ULM’s history, programs, campus life, and more.
- **🎤 Voice Input**: Use the microphone to ask questions with voice input.
- **🕑 Search History**: Stores previous questions and answers for reference, with options to clear or paginate through history.

---

## 🛠️ Technologies Used

- **FastAPI**: For building the backend API.
- **JavaScript (Fetch API)**: For sending requests from the frontend.
- **HTML/CSS**: For creating and styling the user interface.
- **Python**: For backend scripting and query handling.
- **Git/GitHub**: For version control and project hosting.

---

## 🚀 Installation

### Prerequisites

- **Python 3.7** or later
- **Git** (for cloning the repository)
- **Node.js** (optional, for additional front-end work)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BIPINSAPKOTA193/ULM-Info-Hub.git
   cd ULM-Info-Hub
   
2. **Create a Virtual Environment**:
`bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Create a Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Start the FastAPI Server:

bash
Copy code
uvicorn app.main:app --reload --host 127.0.0.1 --port 3000
Open the Frontend:

Open index.html in your browser. Ensure it points to http://127.0.0.1:3000 for API requests.

📋 Usage
Ask a Question: Type your question and click "Submit" to receive an answer.
Voice Input: Click the 🎤 icon to use voice input.
View Previous Questions: See a list of past questions and answers with pagination.
Clear History: Click "Clear History" to remove all previous questions and answers.
🗂️ Project Structure
graphql
Copy code
ULM-Info-Hub/
├── app/
│   ├── main.py          # Main FastAPI application
│   ├── routes.py        # API routes for handling queries
│   ├── utils.py         # Utility functions (query processing, etc.)
│   └── models.py        # Data models for handling requests
├── frontend/
│   ├── index.html       # Main HTML file for the UI
│   ├── styles.css       # CSS file for styling
│   └── script.js        # JavaScript for handling frontend logic
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
🤝 Contributing
Contributions are welcome! Here’s how to get started:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Commit your changes and push them to your fork:
bash
Copy code
git push origin feature-name
Open a pull request with a detailed description of your changes.
📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.


