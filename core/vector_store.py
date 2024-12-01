from typing import List
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config.settings import RAGConfig

class VectorStoreManager:
    """Manages vector store operations"""
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self.embeddings = HuggingFaceEmbeddings(
            model_name=config.embedding_model
        )
    
    def create_or_load_vectorstore(self, documents: List[Document]) -> Chroma:
        """Create a new vector store or load existing one"""
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.config.db_directory
        )