import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==============================
# 🔐 API TOKENS
# ==============================

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# ==============================
# 🤖 LLM CONFIGURATION
# ==============================

# Choose: "local" or "cloud"
LLM_MODE = "cloud"

# HuggingFace model for generation
LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

# LLM generation parameters
MAX_NEW_TOKENS = 512
TEMPERATURE = 0.3

# ==============================
# 🧠 EMBEDDINGS CONFIGURATION
# ==============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==============================
# ✂️ TEXT SPLITTING
# ==============================

CHUNK_SIZE = 500  # Target tokens
CHUNK_OVERLAP = 50 # Token overlap

# Choose: "faiss" or "pinecone"
VECTOR_STORE_TYPE = "faiss"

# FAISS Configuration
FAISS_INDEX_PATH = "vectorstore/faiss_index"

# Pinecone Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# ==============================
# 📂 PATHS
# ==============================

DOCS_PATH = "docs"

# ==============================
# 🔎 RETRIEVER
# ==============================

TOP_K = 6

# ==============================
# 🌐 FLASK
# ==============================

FLASK_DEBUG = True
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
