# Dynamic Form Generator (Generative UI)

A Flask-based web application that generates dynamic, functional forms from natural language user prompts using a Large Language Model (LLM).

## Overview
- Converts free-text form requirements into a structured JSON schema
- Dynamically renders forms on the frontend
- Safely generates HTML from JSON (no raw HTML from LLM)
- Maps submitted form inputs to semantic meta-tags
- Focuses on a clean and happy-path implementation

## Tech Stack
- Backend: Flask (Python)
- LLM: OpenRouter (Llama 3.3 70B)
- Frontend: HTML, JavaScript
- Styling: Bootstrap (CDN)

## Run Locally
```bash
pip install -r requirements.txt
python app.py
