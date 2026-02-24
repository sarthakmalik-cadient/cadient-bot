from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer
from config import CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL
from rag.preprocessor import clean_text

def split_docs(documents):
    # Load tokenizer for token-based splitting
    try:
        tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL, trust_remote_code=True)
    except Exception as e:
        print(f"⚠️ Could not load tokenizer for {EMBEDDING_MODEL}. Falling back to standard tokenizer.")
        tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    
    # 1. Preprocess the text in each document
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)
    
    # 2. Initialize the splitter with the tokenizer
    text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    
    # 3. Split the documents
    chunks = text_splitter.split_documents(documents)
    return chunks
