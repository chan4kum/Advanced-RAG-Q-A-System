from dataclasses import dataclass
from typing import Optional

@dataclass
class RAGConfig:
    """Configuration settings for the RAG application"""
    chunk_size: int = 1000
    chunk_overlap: int = 200
    k_retrieval: int = 4
    model_name: str = "gemma-7b-it"
    embedding_model: str = "all-MiniLM-L6-v2"
    db_directory: str = "chroma_db"
    temperature: float = 0.1
    max_tokens: Optional[int] = None