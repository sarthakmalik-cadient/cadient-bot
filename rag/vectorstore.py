import os
from langchain_community.vectorstores import FAISS
from langchain_pinecone import PineconeVectorStore
from config import VECTOR_STORE_TYPE, FAISS_INDEX_PATH, PINECONE_API_KEY, PINECONE_INDEX_NAME
from rag.embeddings import get_embeddings
from rag.loader import load_docs
from rag.splitter import split_docs
from pinecone import Pinecone, ServerlessSpec

def create_vectorstore():
    """Builds index from docs and saves it (local FAISS or cloud Pinecone)."""
    print("🚀 Loading documents...")
    docs = load_docs()
    print(f"📄 Loaded {len(docs)} documents.")
    
    print("✂️ Splitting documents into chunks...")
    chunks = split_docs(docs)
    print(f"🧩 Created {len(chunks)} chunks.")
    
    embeddings = get_embeddings()
    
    # Dynamically determine the dimension from the embedding model
    print("📏 Determining embedding dimensions...")
    sample_embedding = embeddings.embed_query("test")
    model_dimension = len(sample_embedding)
    print(f"✅ Model dimension: {model_dimension}")
    
    if VECTOR_STORE_TYPE == "pinecone":
        print(f"🌲 Connecting to Pinecone...")
        pc = Pinecone(api_key=PINECONE_API_KEY)
        
        # Check if index exists and verify dimensions
        existing_indexes = pc.list_indexes().names()
        if PINECONE_INDEX_NAME in existing_indexes:
            desc = pc.describe_index(PINECONE_INDEX_NAME)
            if desc.dimension != model_dimension:
                print(f"⚠️ Dimension mismatch: Index has {desc.dimension} but model needs {model_dimension}.")
                print(f"🗑️ Deleting incompatible index '{PINECONE_INDEX_NAME}'...")
                pc.delete_index(PINECONE_INDEX_NAME)
                existing_indexes = pc.list_indexes().names()

        # Create index if it doesn't exist (either new or deleted due to mismatch)
        if PINECONE_INDEX_NAME not in existing_indexes:
            print(f"🆕 Creating new Pinecone index: {PINECONE_INDEX_NAME} ({model_dimension} dimensions)")
            pc.create_index(
                name=PINECONE_INDEX_NAME,
                dimension=model_dimension,
                metric='cosine',
                spec=ServerlessSpec(cloud='aws', region='us-east-1')
            )
        
        vectorstore = PineconeVectorStore.from_documents(
            chunks, 
            embeddings, 
            index_name=PINECONE_INDEX_NAME
        )
        print("✨ Successfully uploaded embeddings to Pinecone.")
        return vectorstore

    else:
        print("🧠 Generating embeddings and building FAISS index...")
        vectorstore = FAISS.from_documents(chunks, embeddings)
        print(f"✨ Successfully generated and indexed {vectorstore.index.ntotal} embeddings.")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
        vectorstore.save_local(FAISS_INDEX_PATH)
        print(f"📦 Vectorstore saved to {FAISS_INDEX_PATH}")
        return vectorstore

def get_vectorstore():
    """Loads existing index or creates a new one."""
    embeddings = get_embeddings()

    if VECTOR_STORE_TYPE == "pinecone":
        print(f"✅ Connecting to Pinecone index: {PINECONE_INDEX_NAME}")
        return PineconeVectorStore(
            index_name=PINECONE_INDEX_NAME, 
            embedding=embeddings
        )

    else:
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
