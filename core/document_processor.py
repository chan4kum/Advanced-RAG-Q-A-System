from typing import List
import os
from pathlib import Path
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from config.settings import RAGConfig

class DocumentProcessor:
    """Handles document loading and splitting operations"""
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap
        )
    
    def process_uploaded_files(self, uploaded_files) -> List[Document]:
        """Process uploaded PDF files and return document chunks"""
        documents = []
        
        for uploaded_file in uploaded_files:
            temp_file_path = Path(f"temp_{uploaded_file.name}")
            try:
                # Save uploaded file temporarily
                temp_file_path.write_bytes(uploaded_file.getvalue())
                
                # Load and split the document
                loader = PyPDFLoader(str(temp_file_path))
                docs = loader.load()
                split_docs = self.text_splitter.split_documents(docs)
                documents.extend(split_docs)
                
            except Exception as e:
                print(f"Error processing file {uploaded_file.name}: {str(e)}")
                raise
            
            finally:
                # Clean up temporary file
                if temp_file_path.exists():
                    temp_file_path.unlink()
        
        return documents