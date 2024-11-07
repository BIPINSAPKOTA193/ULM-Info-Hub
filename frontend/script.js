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
        previousResponsesList.innerHTML = "<li>No previous questions available.</li>";
        document.getElementById("pagination").style.display = "none";
        document.getElementById("clearHistoryBtn").style.display = "none";
    } else {
        pageResponses.forEach((item) => {
            const listItem = document.createElement("li");
            listItem.textContent = item.question;
            listItem.classList.add("clickable-question");

            listItem.onclick = () => {
                document.getElementById("responseText").textContent = item.response;
            };

            previousResponsesList.appendChild(listItem);
        });

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
        const responses = data.response;
        
        // Check if responses contain multiple items
        if (Array.isArray(responses) && responses.length > 0) {
            const responseText = responses.map(r => `<p><strong>${r.question}</strong>: ${r.answer}</p>`).join("");
            document.getElementById("responseText").innerHTML = responseText;
            saveResponse(query, responseText);
        } else if (typeof responses === "string") {
            document.getElementById("responseText").textContent = responses;
            saveResponse(query, responses);
        } else {
            document.getElementById("responseText").textContent = "No relevant information found.";
        }

        // Clear input field and load previous responses
        document.getElementById("queryInput").value = "";
        loadPreviousResponses();
    })
    .catch((error) => {
        console.error("Fetch error:", error);
        document.getElementById("responseText").textContent = "Sorry, there was an error processing your request.";
    });
}

// Clear history and update the UI accordingly
function clearHistory() {
    localStorage.removeItem("previousResponses");
    currentPage = 1;
    loadPreviousResponses();
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

// Debounce function to limit rapid calls
function debounce(func, delay) {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

// Function to start voice recognition for the user's query
function startVoiceRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        alert("Sorry, your browser doesn't support voice recognition.");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = function (event) {
        const voiceQuery = event.results[0][0].transcript;
        document.getElementById("queryInput").value = voiceQuery;
        debounce(sendQuery, 500)();  // Debounce to prevent multiple calls
    };

    recognition.start();
}
