from langchain_community.document_loaders import DirectoryLoader, Docx2txtLoader, TextLoader, UnstructuredMarkdownLoader
from config import DOCS_PATH
import os

def load_docs():
    # Load .docx files
    docx_loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.docx",
        loader_cls=Docx2txtLoader
    )
    docx_documents = docx_loader.load()

    # Load .md files
    md_loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader
    )
    md_documents = md_loader.load()

    documents = docx_documents + md_documents
    return documents
