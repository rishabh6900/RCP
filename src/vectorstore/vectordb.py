from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks, embeddings):
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("faiss_index")
    return db

def load_vectorstore(embeddings):
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)