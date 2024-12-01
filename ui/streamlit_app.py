import os
import streamlit as st
from pathlib import Path
from config.settings import RAGConfig
from core.document_processor import DocumentProcessor
from core.vector_store import VectorStoreManager
from core.rag_chain import RAGChain
from utils.helpers import ensure_directory, cleanup_temp_files, get_env_variable

def initialize_session_state():
    """Initialize session state variables"""
    if 'processed_files' not in st.session_state:
        st.session_state.processed_files = set()
    if 'vectorstore' not in st.session_state:
        st.session_state.vectorstore = None

def render_sidebar():
    """Render sidebar with configuration options"""
    with st.sidebar:
        st.header("Configuration")
        chunk_size = st.slider("Chunk Size", 500, 2000, 1000, 100)
        chunk_overlap = st.slider("Chunk Overlap", 0, 500, 200, 50)
        k_retrieval = st.slider("Number of Retrieved Documents", 1, 10, 4)
        
        return RAGConfig(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            k_retrieval=k_retrieval
        )

def main():
    st.title("📚 Advanced RAG Q&A System")
    
    # Initialize session state
    initialize_session_state()
    
    # Render sidebar and get configuration
    config = render_sidebar()
    
    # Get API key
    api_key = st.text_input("Enter your Groq API key:", type="password")
    if not api_key:
        st.warning("Please enter your Groq API key to continue.")
        return
    
    os.environ["GROQ_API_KEY"] = api_key
    
    # File upload
    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type="pdf",
        accept_multiple_files=True
    )
    
    if uploaded_files:
        # Process only new files
        new_files = [f for f in uploaded_files 
                    if f.name not in st.session_state.processed_files]
        
        if new_files:
            with st.spinner("Processing new documents..."):
                # Initialize components
                doc_processor = DocumentProcessor(config)
                vectorstore_manager = VectorStoreManager(config)
                
                # Process documents
                documents = doc_processor.process_uploaded_files(new_files)
                
                # Update vector store
                st.session_state.vectorstore = vectorstore_manager.create_or_load_vectorstore(documents)
                
                # Update processed files
                st.session_state.processed_files.update(f.name for f in new_files)
                
                st.success(f"Processed {len(documents)} new document chunks")
        
        # Initialize RAG chain
        rag_chain = RAGChain(config)
        retriever = rag_chain.setup_retrieval_chain(st.session_state.vectorstore)
        response_chain = rag_chain.create_response_chain()
        
        # Query interface
        query = st.text_input("Ask a question about your documents:")
        if query:
            with st.spinner("Generating response..."):
                # Retrieve relevant documents
                retrieved_docs = retriever.get_relevant_documents(query)
                
                # Generate response
                response = response_chain.invoke({
                    "context": retrieved_docs,
                    "question": query
                })
                
                # Display results
                st.write("### Answer")
                st.write(response)
                
                # Show relevant passages
                with st.expander("View relevant passages"):
                    for i, doc in enumerate(retrieved_docs):
                        st.write(f"**Passage {i+1}:**")
                        st.write(doc.page_content)
                        st.write("---")