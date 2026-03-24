import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==============================
# 🔐 API TOKENS
# ==============================

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ==============================
# 🤖 LLM CONFIGURATION
# ==============================

# Choose: "huggingface" or "anthropic"
LLM_PROVIDER = "anthropic"

# Model for generation
# For huggingface: "google/gemma-2-9b-it" 
# For anthropic: "claude-3-haiku-20240307"
LLM_MODEL = "claude-3-haiku-20240307"

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

CHUNK_SIZE = 400  # Target tokens
CHUNK_OVERLAP = 40 # Token overlap

# ==============================
# 🧠 VECTOR STORE (FAISS)
# ==============================
FAISS_INDEX_PATH = "vectorstore/faiss_index"

# ==============================
# 📂 PATHS
# ==============================

DOCS_PATH = "docs"

# ==============================
# 🔎 RETRIEVER
# ==============================

TOP_K = 3

# ==============================
# 🌐 FLASK
# ==============================

FLASK_DEBUG = True
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
