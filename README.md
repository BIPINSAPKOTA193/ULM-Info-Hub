# 🎓 ULM Information Hub

Welcome to the **ULM Information Hub**! This project is a **FastAPI-based web application** designed to answer frequently asked questions about the University of Louisiana Monroe (ULM). Users can type questions into the front-end interface and receive responses from a curated dataset or through intelligent matching.

## 🌟 Key Features

- **Ask Questions About ULM**  
  Get quick answers about ULM’s history, academic programs, campus life, and more by typing a question.
  
- **Voice Input**  
  Ask questions using voice input through the built-in microphone feature.
  
- **Search History**  
  View and refer back to previously asked questions and their responses, with options to clear history or navigate through past entries.

## 🛠️ Technologies Used

- **FastAPI** for backend API development
- **JavaScript (Fetch API)** for frontend requests
- **HTML/CSS** for the user interface
- **Python** for backend scripting and query handling
- **Git/GitHub** for version control and project hosting

## 🚀 Installation

### Prerequisites

- **Python 3.7 or later**
- **Git** for cloning the repository
- **Node.js** (optional, for additional front-end work)

### Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/BIPINSAPKOTA193/ULM-Info-Hub.git
    cd ULM-Info-Hub
    ```
2. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Start the FastAPI Server:**
    ```bash
    uvicorn app.main:app --reload --host 127.0.0.1 --port 3000
    ```
5. **Open the Frontend:**
    - Open `index.html` in your browser.
    - Ensure it points to `http://127.0.0.1:3000` for API requests.

## 📋 Usage

- **Ask a Question:** Type your question and click "Submit" to receive an answer.
- **Voice Input:** Click the 🎤 icon to use voice input.
- **View Previous Questions:** See a list of past questions and answers with pagination.
- **Clear History:** Click "Clear History" to remove all previous questions and answers.

## 🗂️ Project Structure

```graphql
ULM-Info-Hub/
├── app/
│   ├── main.py       # Main FastAPI application
│   ├── routes.py     # API routes for handling queries
│   ├── utils.py      # Utility functions (query processing, etc.)
│   └── models.py     # Data models for handling requests
├── frontend/
│   ├── index.html    # Main HTML file for the UI
│   ├── styles.css    # CSS file for styling
│   └── script.js     # JavaScript for handling frontend logic
├── .gitignore        # Git ignore file
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! To get started:

1. **Fork** the repository on GitHub.
2. **Clone** your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR-USERNAME/ULM-Info-Hub.git
    cd ULM-Info-Hub
    ```
3. **Create a new branch** for your feature or fix:
    ```bash
    git checkout -b feature-branch-name
    ```
4. **Make your changes** to the codebase.
5. **Commit** your changes with a clear and descriptive message:
    ```bash
    git commit -m "Add feature: brief description"
    ```
6. **Push** your changes to your forked repository:
    ```bash
    git push origin feature-branch-name
    ```
7. Open a **pull request** to the main repository with a detailed description of your changes. Make sure to link any relevant issues.

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project, provided that you include the original copyright and license notice in any copies of the work.

For more information, see the [LICENSE](LICENSE) file.

