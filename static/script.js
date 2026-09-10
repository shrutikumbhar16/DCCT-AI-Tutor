async function askQuestion() {

    const questionInput = document.getElementById("question");
    const chatBox = document.getElementById("chat-box");
    const askButton = document.getElementById("ask-button");

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }


    // Show student's message

    const userMessage = document.createElement("div");

    userMessage.classList.add(
        "message",
        "user-message"
    );

    userMessage.innerText = question;

    chatBox.appendChild(userMessage);


    // Clear input

    questionInput.value = "";


    // Disable button while waiting

    askButton.disabled = true;


    // Show loading message

    const tutorMessage = document.createElement("div");

    tutorMessage.classList.add(
        "message",
        "tutor-message"
    );

    tutorMessage.innerText = "🤔 Thinking...";

    chatBox.appendChild(tutorMessage);


    chatBox.scrollTop = chatBox.scrollHeight;


    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        const data = await response.json();


        if (response.ok && data.answer) {

            tutorMessage.innerText = data.answer;

        } else {

            tutorMessage.innerText =
                data.error || "Something went wrong.";

        }


    } catch (error) {

        tutorMessage.innerText =
            "Unable to connect to the server.";

        console.error(error);

    }


    // Enable button again

    askButton.disabled = false;


    chatBox.scrollTop = chatBox.scrollHeight;
}


async function clearChat() {

    try {

        const response = await fetch("/clear", {
            method: "POST"
        });

        const data = await response.json();

        if (response.ok) {

            const chatBox = document.getElementById("chat-box");

            chatBox.innerHTML = `
                <div class="message tutor-message">
                    👋 Hi! I'm your DCCT AI Tutor.
                    Ask me anything about Digital Communication
                    or Coding Theory.
                </div>
            `;

        }

    } catch (error) {

        console.error(error);

    }
}
document
    .getElementById("question")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {
            askQuestion();
        }

    });
    
async function startQuiz() {
    const quizButton = document.getElementById("quiz-button");

    quizButton.disabled = true;
    quizButton.innerText = "🤔 Generating...";

    try {
        const response = await fetch("/quiz", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        });

        const data = await response.json();

        const chatBox = document.getElementById("chat-box");

        const quizMessage = document.createElement("div");
        quizMessage.className = "message tutor-message";
        quizMessage.innerText = "🎯 DCCT Quiz\n\n" + data.question;

        chatBox.appendChild(quizMessage);

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        console.error("Quiz error:", error);

        const chatBox = document.getElementById("chat-box");

        const errorMessage = document.createElement("div");
        errorMessage.className = "message tutor-message";
        errorMessage.innerText = "Sorry, I couldn't generate a quiz right now.";

        chatBox.appendChild(errorMessage);

    } finally {
        quizButton.disabled = false;
        quizButton.innerText = "🎯 Quiz Me";
    }
}