from operator import itemgetter
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

from config import LLM_PROVIDER
from rag.retriever import get_retriever
from rag.prompt import get_product_specialist_prompt
from rag.llm import get_cloud_llm, get_local_llm, get_anthropic_llm

class ChatResponse(BaseModel):
    """Structured response from the chatbot."""
    message: str = Field(default="", description="The conversational sales response to the user's question.")
    product_list: List[str] = Field(default_factory=list, description="A list of specific Cadient products or features mentioned (e.g., ['SmartMatch™', 'Decision Point™']).")

def build_rag_chain():

    retriever = get_retriever()
    prompt = get_product_specialist_prompt()
    
    if LLM_PROVIDER == "anthropic":
        llm = get_anthropic_llm()
    elif LLM_PROVIDER == "huggingface":
        llm = get_cloud_llm()
    else:
        llm = get_local_llm()

    # Wrap LLM for structured output
    structured_llm = llm.with_structured_output(ChatResponse)

    rag_chain = (
        {
            "context": itemgetter("question") | retriever, 
            "question": itemgetter("question"),
            "chat_history": itemgetter("chat_history")
        }
        | prompt
        | structured_llm
    )

    return rag_chain
