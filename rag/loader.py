from langchain_community.document_loaders import DirectoryLoader, Docx2txtLoader
from config import DOCS_PATH

def load_docs():
    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.docx",
        loader_cls=Docx2txtLoader
    )
    documents = loader.load()
    return documents
