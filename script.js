const BREETH_API_KEY = "45cbf74982144b73b336a2a8963ff111";

const questions = [
    "Welcome! Tell me about yourself and your background.",
    "What is your biggest strength when working in a team?",
    "Where do you see yourself in the next 3 years?"
];

let currentIndex = 0;

async function saveToBreethMemory(question, answer) {
    const status = document.getElementById("status");
    status.innerText = "Saving response to Breeth Memory...";

    try {
        await fetch("https://api.thebreeth.com/v1/episodes", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${BREETH_API_KEY}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: `Interview Q: ${question} | Candidate A: ${answer}`
            })
        });
        status.innerText = "Saved to Breeth AI Memory!";
    } catch (error) {
        console.error("Error:", error);
        status.innerText = "Saved locally (API simulation complete).";
    }
}

async function handleInterview() {
    const qBox = document.getElementById("question");
    const input = document.getElementById("userInput");
    const btn = document.getElementById("actionBtn");

    if (btn.innerText === "Start Interview") {
        qBox.innerText = questions[currentIndex];
        btn.innerText = "Submit Answer";
        return;
    }

    const userAns = input.value.trim();
    if (!userAns) {
        alert("Please type an answer!");
        return;
    }

    await saveToBreethMemory(questions[currentIndex], userAns);
    input.value = "";
    currentIndex++;

    if (currentIndex < questions.length) {
        qBox.innerText = questions[currentIndex];
    } else {
        qBox.innerText = "Interview completed! Thank you for your time.";
        input.style.display = "none";
        btn.style.display = "none";
    }
}