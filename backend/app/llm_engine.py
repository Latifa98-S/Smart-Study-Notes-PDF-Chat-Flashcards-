# llm_engine.py
"""
LLM Engine using Ollama
Compatible with smart-study-notes app
Supports:
- AI answers
- Flashcard generation
"""

import requests


class LLMEngine:
    def __init__(
        self,
        model: str = "gpt-oss:120b-cloud",
        base_url: str = "http://localhost:11434",
        timeout: int = 120,
    ):
        self.model = model
        self.url = f"{base_url}/api/generate"
        self.timeout = timeout

    # --------------------------------------------------
    # AI ANSWER (Q&A)
    # --------------------------------------------------
    def generate_answer(self, question: str, context: str = "") -> str:
        prompt = self._build_answer_prompt(question, context)
        return self._call_llm(prompt)

    # --------------------------------------------------
    # FLASHCARDS
    # --------------------------------------------------
    def generate_flashcards(self, context: str) -> str:
        """
        Generates compact study flashcards from given context
        """
        prompt = self._build_flashcard_prompt(context)
        return self._call_llm(prompt)

    # --------------------------------------------------
    # INTERNAL LLM CALL
    # --------------------------------------------------
    def _call_llm(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2

            
            }
        }                                   

        response = requests.post(
            self.url,
            json=payload,
            timeout=self.timeout,
        )
        response.raise_for_status()

        return response.json().get("response", "")

    # --------------------------------------------------
    # PROMPT BUILDERS
    # --------------------------------------------------
    def _build_answer_prompt(self, question: str, context: str) -> str:
        if context:
            return f"""
You are a helpful AI tutor.

Context:
{context}

Question:
{question}

Provide a clear, structured, and concise answer suitable for study notes.
"""
        else:
            return f"""
You are a helpful AI tutor.

Question:
{question}

Provide a clear, structured, and concise answer suitable for study notes.
"""

    def _build_flashcard_prompt(self, context: str) -> str:
        return f"""
You are an AI tutor.

From the following content, generate concise flashcards.
Each flashcard should contain:
- A short question
- A short, precise answer

Rules:
- Be compact but complete
- Suitable for exam preparation
- Use bullet points or numbering

Content:
{context}

Flashcards:
"""