# rag/chain.py

from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

from config import LLM_MODE
from rag.retriever import get_retriever
from rag.prompt import get_product_specialist_prompt
from rag.llm import get_cloud_llm, get_local_llm


def build_rag_chain():

    retriever = get_retriever()
    prompt = get_product_specialist_prompt()
    
    if LLM_MODE == "cloud":
        llm = get_cloud_llm()
    else:
        llm = get_local_llm()

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
