# DCCT AI Tutor 🤖

An AI-based teaching assistant for **Digital Communication and Coding Theory (DCCT)** developed as part of the CSPML Laboratory.

The application uses the **Qwen3-4B-Instruct-2507** Large Language Model through the **Hugging Face Inference API** to answer DCCT-related questions, explain concepts, provide guidance for numerical problems, maintain short-term conversation context, and generate practice quizzes.

---

## 1. Project Overview

The **DCCT AI Tutor** is a web-based AI teaching assistant designed to help undergraduate students learn Digital Communication and Coding Theory.

The application provides an interactive interface where students can:

- Ask questions related to DCCT.
- Receive concept explanations.
- Get step-by-step guidance for numerical problems.
- Ask follow-up questions using short-term conversation context.
- Generate DCCT multiple-choice questions using the **Quiz Me** feature.
- Clear the current conversation and start a new one.

The application consists of a **Flask backend**, a web-based frontend, and an AI teaching agent connected to the **Qwen3-4B-Instruct-2507** model through the Hugging Face Inference API.

---

## 2. Live Application

The application is deployed on Railway and can be accessed here:

**Live Application:**  
https://dcct-ai-tutor-production.up.railway.app

---

## 3. Source Code

The complete source code is available on GitHub:

**GitHub Repository:**  
https://github.com/shrutikumbhar16/DCCT-AI-Tutor

---

## 4. Features

The application provides the following features:

- **Question Answering** – Ask questions related to Digital Communication and Coding Theory.
- **Concept Explanation** – Provides intuitive as well as technical explanations.
- **Numerical Problem Guidance** – Provides step-by-step solutions for numerical problems.
- **Conversation Memory** – Maintains short-term conversation context while the application is running.
- **Quiz Me** – Generates DCCT multiple-choice questions for practice.
- **Clear Chat** – Clears the current conversation history.
- **Web-Based GUI** – Provides a simple interface for interaction.
- **Cloud Deployment** – Application is deployed using Railway.

---

# 5. System Architecture

```text
                    Student
                       │
                       ▼
              HTML / CSS / JavaScript
                       │
                       ▼
                 Flask Backend
                       │
                       ▼
              DCCT Teaching Agent
                       │
                       ▼
           Hugging Face Inference API
                       │
                       ▼
          Qwen3-4B-Instruct-2507
                       │
                       ▼
              Generated Response
                       │
                       ▼
                Web Interface

