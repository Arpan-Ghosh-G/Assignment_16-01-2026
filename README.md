# Dynamic Form Generator (Generative UI)

A Flask-based web application that generates dynamic, functional forms from natural language user prompts using a Large Language Model (LLM).

---

## 🖼 Application Preview

![UI](./WhatsApp%20Image%202026-01-16%20at%2013.51.53.jpeg)

> *The UI dynamically renders forms based on user prompts and maps submitted data to semantic meta-tags.*

---

## 🔍 Overview

- Converts free-text form requirements into a structured JSON schema using an LLM
- Dynamically renders forms on the frontend
- Safely generates HTML from JSON (no raw HTML from LLM)
- Maps submitted form inputs to semantic meta-tags
- Focuses on a clean, minimal, and happy-path implementation

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **LLM:** OpenRouter (Llama models)
- **Frontend:** HTML, JavaScript
- **Styling:** Bootstrap (CDN)

---

## ▶️ Run Locally

### 1. Take a new LLM API key from Openrouter and after running the code, give the API key 2 times as asked by the code in the terminal then visit the local URL
### 2. Install dependencies
```bash
pip install -r requirements.txt
