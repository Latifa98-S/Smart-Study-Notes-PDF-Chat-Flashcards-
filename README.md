# Smart Study Notes (PDF Chat + Flashcards)

Upload a PDF, extract text, and chat with your document using a local LLM (Ollama) via FastAPI + React (Vite).

## Tech Stack
- Backend: FastAPI (Python)
- Frontend: React + Vite
- PDF parsing: pypdf
- LLM: Ollama (local)

## Run locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
