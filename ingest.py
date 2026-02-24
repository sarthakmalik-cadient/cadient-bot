# ingest.py
from rag.vectorstore import create_vectorstore

if __name__ == "__main__":
    print("🎬 Starting document ingestion process...")
    create_vectorstore()
    print("✅ Ingestion complete!")
