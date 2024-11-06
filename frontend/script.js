const pageSize = 5; // Number of questions per page
let currentPage = 1; // Track the current page

// Function to load previous responses and handle empty history
function loadPreviousResponses() {
    const previousResponses = JSON.parse(localStorage.getItem("previousResponses")) || [];
    const totalPages = Math.ceil(previousResponses.length / pageSize);
    const start = (currentPage - 1) * pageSize;
    const end = start + pageSize;
    const pageResponses = previousResponses.slice(start, end);

    const previousResponsesList = document.getElementById("previousResponsesList");
    previousResponsesList.innerHTML = ""; // Clear current list

    if (previousResponses.length === 0) {
        // Show a message if no history is available
        previousResponsesList.innerHTML = "<li>No previous questions available.</li>";
        document.getElementById("pagination").style.display = "none"; // Hide pagination controls
        document.getElementById("clearHistoryBtn").style.display = "none"; // Hide clear history button
    } else {
        // Display each question as a clickable list item
        pageResponses.forEach((item) => {
            const listItem = document.createElement("li");
            listItem.textContent = item.question;
            listItem.classList.add("clickable-question");

            // Display corresponding answer when clicked
            listItem.onclick = () => {
                document.getElementById("responseText").textContent = item.response;
            };

            previousResponsesList.appendChild(listItem);
        });

        // Show pagination and clear history controls if history exists
        document.getElementById("pagination").style.display = totalPages > 1 ? "flex" : "none";
        document.getElementById("clearHistoryBtn").style.display = "inline-block";
        document.getElementById("pageInfo").textContent = `Page ${currentPage} of ${totalPages}`;
    }
}

// Function to save a new question and response in local storage
function saveResponse(question, response) {
    const previousResponses = JSON.parse(localStorage.getItem("previousResponses")) || [];
    previousResponses.push({ question, response });
    localStorage.setItem("previousResponses", JSON.stringify(previousResponses));
}

// Function to handle query submission
function sendQuery() {
    const query = document.getElementById("queryInput").value.trim();

    if (query.length < 3) {
        alert("Please enter a more specific question.");
        return;
    }

    fetch("http://localhost:3000/getULMInfo", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: query }),
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        const responseText = data.response;
        document.getElementById("responseText").textContent = responseText;
        saveResponse(query, responseText);  // Save to local storage
        loadPreviousResponses();  // Refresh the previous questions list
    })
    .catch((error) => {
        console.error("Fetch error:", error);
        document.getElementById("responseText").textContent = "Sorry, there was an error processing your request.";
    });
}

// Clear history and update the UI accordingly
function clearHistory() {
    localStorage.removeItem("previousResponses");
    currentPage = 1;  // Reset to first page
    loadPreviousResponses();  // Refresh the display to show "No previous questions available."
    document.getElementById("responseText").textContent = "Search history has been cleared.";
}

// Pagination control functions
function nextPage() {
    const previousResponses = JSON.parse(localStorage.getItem("previousResponses")) || [];
    const totalPages = Math.ceil(previousResponses.length / pageSize);
    if (currentPage < totalPages) {
        currentPage++;
        loadPreviousResponses();
    }
}

function previousPage() {
    if (currentPage > 1) {
        currentPage--;
        loadPreviousResponses();
    }
}

// Load previous responses on page load
window.onload = loadPreviousResponses;

// Function to start voice recognition for the user's query
function startVoiceRecognition() {
    // Check if the browser supports SpeechRecognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        alert("Sorry, your browser doesn't support voice recognition.");
        return;
    }

    // Initialize the voice recognition
    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    // When voice recognition ends, send the recognized query
    recognition.onresult = function (event) {
        const voiceQuery = event.results[0][0].transcript;
        document.getElementById("queryInput").value = voiceQuery;
        sendQuery();
    };

    // Start listening for voice input
    recognition.start();
}
