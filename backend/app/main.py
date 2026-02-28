from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypdf import PdfReader
from .llm_engine import LLMEngine

app = FastAPI()

# CORS (already correct)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = LLMEngine()

# ---------- MODELS ----------
class AskRequest(BaseModel):
    question: str
    context: str = ""


# ---------- ROUTES ----------
@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(req: AskRequest):
    answer = llm.generate_answer(req.question, req.context)
    print("Context length:", len(req.context))
    return {"answer": answer}


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    reader = PdfReader(file.file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return {
        "text": text[:15000]  # safety limit
    }