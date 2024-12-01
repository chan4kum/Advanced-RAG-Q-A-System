import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_community.vectorstores import Chroma
from config.settings import RAGConfig

class RAGChain:
    """Manages the RAG pipeline and query processing"""
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=config.model_name,
            temperature=config.temperature,
            max_tokens=config.max_tokens
        )
        
        self.prompt = ChatPromptTemplate.from_template("""
            You are a helpful assistant. Use the following context to answer the question.
            If you cannot find the answer in the context, say "I cannot find the answer in the provided context."
            
            Context: {context}
            
            Question: {question}
            
            Answer: """)
    
    def setup_retrieval_chain(self, vectorstore: Chroma) -> ContextualCompressionRetriever:
        """Set up the retrieval chain with compression"""
        base_retriever = vectorstore.as_retriever(
            search_kwargs={"k": self.config.k_retrieval}
        )
        
        compressor = LLMChainExtractor.from_llm(self.llm)
        
        return ContextualCompressionRetriever(
            base_compressor=compressor,
            base_retriever=base_retriever
        )
    
    def create_response_chain(self):
        """Create the document chain for generating responses"""
        return create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.prompt
        )
