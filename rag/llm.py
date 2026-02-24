# rag/llm.py

from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint, ChatHuggingFace
from transformers import pipeline
from config import LLM_MODEL, HF_TOKEN, TEMPERATURE, MAX_NEW_TOKENS


def get_local_llm():
    pipe = pipeline(
        "text-generation",
        model=LLM_MODEL,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE
    )
    return HuggingFacePipeline(pipeline=pipe)


def get_cloud_llm():
    llm = HuggingFaceEndpoint(
        repo_id=LLM_MODEL,
        huggingfacehub_api_token=HF_TOKEN,
        temperature=TEMPERATURE,
        max_new_tokens=MAX_NEW_TOKENS,
    )
    return ChatHuggingFace(llm=llm)
