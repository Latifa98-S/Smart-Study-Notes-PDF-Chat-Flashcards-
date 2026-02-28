import streamlit as st
from io import BytesIO
from pypdf import PdfReader
from .rag_engine import RAGEngine
from .llm_engine import LLMEngine

st.set_page_config(page_title="Smart Study Notes Generator", layout="wide")
st.title("📚 Smart Study Notes Generator")

# Persist objects
if "rag" not in st.session_state:
    st.session_state.rag = RAGEngine()

if "llm" not in st.session_state:
    st.session_state.llm = LLMEngine()

rag = st.session_state.rag
llm = st.session_state.llm

uploaded = st.file_uploader("Upload lecture PDF", type=["pdf"])

if uploaded:
    reader = PdfReader(BytesIO(uploaded.read()))

    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""

    chunks = rag.chunk_text(full_text)

    if st.button("Build Knowledge Base"):
        with st.spinner("Building AI knowledge base..."):
            rag.build_index(chunks)
            st.session_state.ready = True
        st.success(f"Indexed {len(chunks)} chunks!")

if st.session_state.get("ready"):
    
    st.divider()
    question = st.text_input("Ask your lecture")

    if question:

        if rag.index is None:
            st.warning("Please build knowledge base first!")
            st.stop()

        context = rag.search(question)

        st.subheader("📖 AI Answer")
        st.write(llm.generate_answer(question, context))

        st.subheader("🧠 Flashcards")
        st.text(llm.generate_flashcards(context))
