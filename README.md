# DCCT AI Tutor 🤖

An AI-based teaching assistant for **Digital Communication and Coding Theory (DCCT)**.

The system uses a Large Language Model (LLM) hosted through Hugging Face to answer DCCT questions, explain concepts, solve numerical problems, maintain short-term conversation context, and generate quiz questions for practice.

## Features

* 💬 Ask questions about Digital Communication and Coding Theory
* 📚 Concept explanations with intuitive and technical descriptions
* 🧮 Step-by-step guidance for numerical problems
* 🧠 Short-term conversation memory
* 🎯 Quiz Me feature for DCCT practice
* 🗑 Clear Chat functionality
* 🌐 Simple web-based interface

## System Architecture

```text
Student
   ↓
HTML / CSS / JavaScript
   ↓
Flask Backend
   ↓
DCCT Teaching Agent
   ↓
Hugging Face Inference API
   ↓
Qwen LLM
   ↓
Generated Response
   ↓
Web Interface
```

## Technologies Used

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **JavaScript**
* **Hugging Face Inference API**
* **Qwen/Qwen3-4B-Instruct-2507**
* **python-dotenv**

## Project Structure

```text
DCCT-AI-Tutor/
│
├── app.py
├── agent.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## How It Works

### 1. Student asks a question

The student enters a DCCT question through the web interface.

### 2. Frontend sends the question

JavaScript sends the question to the Flask backend using an HTTP POST request.

### 3. Flask receives the request

The Flask application receives the question through the `/ask` endpoint.

### 4. AI Teaching Agent processes the question

The teaching agent combines the DCCT-specific system instructions with the conversation context and student's question.

### 5. Hugging Face generates the response

The request is sent to the hosted Qwen LLM through the Hugging Face Inference API.

### 6. Response is displayed

The generated explanation is returned through Flask and displayed in the web interface.

## Quiz Me

The **Quiz Me** feature sends a separate request to the AI agent.

The model generates one DCCT multiple-choice question containing:

* A question
* Four options
* The correct answer
* A short explanation

This provides a simple practice mode for students.

## Conversation Memory

The tutor maintains short-term conversation history while the application is running.

For example:

```text
Student: What is BPSK?

AI: BPSK is Binary Phase Shift Keying...

Student: What happens to its amplitude?

AI: In BPSK, the carrier amplitude remains constant...
```

The second question can therefore refer to the concept discussed previously.

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd DCCT-AI-Tutor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## API Token Setup

Create a `.env` file in the project root:

```text
HF_TOKEN=your_hugging_face_token
```

Do **not** upload the `.env` file to GitHub.

The `.gitignore` file is configured to prevent the token from being committed.

## Running the Application

Run:

```bash
python app.py
```

Then open the local address shown by Flask in your browser, typically:

```text
http://127.0.0.1:5000
```

## Future Improvements

Possible future extensions include:

* Interactive quiz answer selection
* Score tracking
* Topic-wise quizzes
* Difficulty selection
* Long-term student progress tracking
* Retrieval-Augmented Generation (RAG) using DCCT notes

## Conclusion

The DCCT AI Tutor demonstrates how a hosted Large Language Model can be integrated with a web application to create a simple educational AI agent for Digital Communication and Coding Theory.
