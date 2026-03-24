import os
from langchain_community.vectorstores import FAISS
from config import FAISS_INDEX_PATH
from rag.embeddings import get_embeddings
from rag.loader import load_docs
from rag.splitter import split_docs

def create_vectorstore():
    """Builds index from docs and saves it using local FAISS."""
    print("🚀 Loading documents...")
    docs = load_docs()
    print(f"📄 Loaded {len(docs)} documents.")
    
    print("✂️ Splitting documents into chunks...")
    chunks = split_docs(docs)
    print(f"🧩 Created {len(chunks)} chunks.")
    
    embeddings = get_embeddings()
    
    print("🧠 Generating embeddings and building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    print(f"✨ Successfully generated and indexed {vectorstore.index.ntotal} embeddings.")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
    vectorstore.save_local(FAISS_INDEX_PATH)
    print(f"📦 Vectorstore saved to {FAISS_INDEX_PATH}")
    return vectorstore

def get_vectorstore():
    """Loads existing FAISS index or creates a new one."""
    embeddings = get_embeddings()
    index_file = os.path.join(FAISS_INDEX_PATH, "index.faiss")
    
    if os.path.exists(index_file):
        print("✅ Loading existing local vectorstore...")
        return FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings, 
            allow_dangerous_deserialization=True
        )
    else:
        print("⚠️ No local vectorstore found. Creating new one...")
        return create_vectorstore()
