import streamlit as st
from dotenv import load_dotenv
import os

from src.ingestion.loader import load_pdf
from src.ingestion.chunker import chunk_documents
from src.embeddings.embedder import get_embeddings
from src.vectorstore.vectordb import create_vectorstore, load_vectorstore
from src.chains.rag_chain import run_rag
from src.prompts.prompts import planner_prompt
# from src.agents.intake_agent import intake_agent
from src.agents.verifier_agent import verifier_agent

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(page_title="AI Course Planner", layout="wide")

st.title("🎓 AI Course Planning Assistant")

uploaded_file = st.file_uploader("Upload Catalog PDF", type="pdf")

query = st.text_input("Ask your academic question:")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_pdf("temp.pdf")
    chunks = chunk_documents(docs)

    embeddings = get_embeddings()
    db = create_vectorstore(chunks, embeddings)

    st.success("PDF processed successfully!")

if "db" not in st.session_state and os.path.exists("faiss_index"):
    embeddings = get_embeddings()
    st.session_state.db = load_vectorstore(embeddings)

if query and "db" in st.session_state:
    with st.spinner("Thinking..."):
        retriever = st.session_state.db.as_retriever()

        # Direct RAG (Planner handles everything now)
        result = run_rag(llm, retriever, planner_prompt, query)

        # Verification
        verification = verifier_agent(query, result)

        st.markdown("### Answer / Plan")
        st.write(result)

        st.markdown("### Verification")
        st.write(verification)