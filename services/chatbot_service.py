# services/chatbot_service.py

from rag.chain import build_rag_chain

rag_chain = build_rag_chain()

def ask_question(question: str):
    return rag_chain.invoke(question)
