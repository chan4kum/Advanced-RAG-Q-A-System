# 🤖 Advanced RAG (Retrieval-Augmented Generation) Q&A System
## PDF Document Analysis with LangChain and Groq LLM

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://python.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A sophisticated document question-answering system that leverages state-of-the-art RAG architecture to provide accurate, context-aware responses from your PDF documents. Built with LangChain, Groq LLM, and modern vector storage technology.

## 🌟 Key Features

- **📄 PDF Processing**: Efficiently processes multiple PDF documents with smart text chunking
- **🔍 Advanced Search**: Implements semantic search with contextual compression for improved relevance
- **💾 Vector Storage**: Persistent document embeddings using Chroma vector store
- **🎯 Context-Aware**: Utilizes LLM-based document compression for precise context extraction
- **⚡ High Performance**: Powered by Groq's fast LLM infrastructure
- **🎨 Interactive UI**: Clean and intuitive Streamlit interface with real-time processing feedback

## 🛠️ Technical Architecture

```
rag_application/
├── config/         # Configuration settings and environment variables
├── core/           # Core RAG functionality modules
├── utils/          # Helper functions and utilities
└── ui/            # Streamlit user interface components
```

## 🚀 Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/chan4kum/Advanced-RAG-Q-A-System.git
cd Advanced-RAG-Q-A-System
```

2. **Set Up Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure Environment Variables**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

4. **Run the Application**
```bash
streamlit run main.py
```

## 💻 Usage

1. Launch the application and enter your Groq API key
2. Upload one or more PDF documents
3. Configure chunking and retrieval parameters in the sidebar
4. Ask questions about your documents
5. View detailed answers with supporting context

## 🔧 Technical Details

### Core Components

- **Document Processor**: 
  - Implements RecursiveCharacterTextSplitter for intelligent document chunking
  - Handles multiple PDF formats and encodings
  - Efficient temporary file management

- **Vector Store Manager**: 
  - Uses HuggingFace embeddings for document vectorization
  - Implements Chroma for persistent vector storage
  - Optimized for quick retrieval and updates

- **RAG Chain**: 
  - Contextual compression for improved relevance
  - LLM-based document extraction
  - Configurable response generation

### Performance Optimizations

- Session state management for processed files
- Incremental document processing
- Efficient vector store updates
- Smart caching of embeddings

## 🛡️ Dependencies

- `streamlit`: Web interface
- `langchain-groq`: LLM integration
- `langchain-community`: RAG components
- `chromadb`: Vector store
- `python-dotenv`: Environment management
- `huggingface-hub`: Embeddings
- `pypdf`: PDF processing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 About the Developer

Built with ❤️ by [Chandan Kumar]
- LinkedIn: [https://www.linkedin.com/in/chan4kum/]
- GitHub: [[Your GitHub Profile](https://github.com/chan4kum)]

## 🙏 Acknowledgments

- LangChain community for the excellent RAG frameworks
- Groq for providing fast LLM infrastructure
- Streamlit team for the amazing UI framework

---

*Note: This project was developed as part of exploring modern RAG architectures and their practical applications in document analysis.*

