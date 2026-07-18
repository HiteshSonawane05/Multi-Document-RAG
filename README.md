# Multi-Document-RAG System

## 📖 Project Overview

The Multi-PDF RAG System is an AI-powered application that enables users to ask questions across multiple PDF documents and receive accurate, context-aware responses.

The system extracts text from uploaded PDF files, splits the content into smaller chunks, stores them in a ChromaDB vector database, retrieves the most relevant information based on the user's query, and generates answers using Groq's Llama 3.3 language model through LangChain.

This project demonstrates the practical implementation of Retrieval-Augmented Generation (RAG), semantic search, vector databases, and Large Language Models (LLMs) for intelligent document question answering.

## 🚀 Features

- Upload and process multiple PDF documents
- Extract text using PyPDF2
- Intelligent document chunking
- Store document chunks in ChromaDB
- Semantic similarity search
- Context-aware response generation
- Multi-document Retrieval-Augmented Generation (RAG)
- Chat history support
- Metadata retrieval (PDF name and page number)
- Powered by Groq Llama 3.3 through LangChain

## 🛠️ Tech Stack

### Programming Language
- Python

### AI / LLM
- Groq
- Llama 3.3 70B Versatile

### Framework
- LangChain

### Vector Database
- ChromaDB

### Document Processing
- PyPDF2

### Text Processing
- RecursiveCharacterTextSplitter

### Environment Management
- python-dotenv

### Version Control
- Git
- GitHub

## 🔄 Project Workflow

1. User uploads one or more PDF documents.
2. The system extracts text from each PDF.
3. The extracted text is divided into smaller chunks.
4. Each chunk is stored inside ChromaDB.
5. User asks a question.
6. ChromaDB performs semantic similarity search.
7. The most relevant document chunks are retrieved.
8. Retrieved context and chat history are combined.
9. LangChain sends the prompt to Groq Llama 3.3.
10. The LLM generates a context-aware response.
11. The system returns the final answer along with document metadata.

```text

                 User
                   │
                   ▼
            Upload PDF Files
                   │
                   ▼
           Text Extraction
               (PyPDF2)
                   │
                   ▼
      Recursive Text Splitter
                   │
                   ▼
             ChromaDB
         (Vector Database)
                   │
                   ▼
            User Question
                   │
                   ▼
         Similarity Search
                   │
                   ▼
      Relevant Document Chunks
                   │
                   ▼
       Chat History + Context
                   │
                   ▼
      LangChain Prompt Builder
                   │
                   ▼
      Groq Llama 3.3 LLM
                   │
                   ▼
          Generated Answer
                   │
                   ▼
                User
```


# 📂 Folder Structure

```text
Multi-Document-RAG/
│
├── app.py
├── generator.py
├── load_documents.py
├── model.py
├── requirements.txt
├── README.md
├── .gitignore
└── pdfs/ (ignored)
```


## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Multi-Modal-RAG.git
```

Move into the project

```bash
cd Multi-Modal-RAG
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
```

Run the application

```bash
python app.py
```

## 🔮 Future Improvements

- Support image-based documents
- OCR integration for scanned PDFs
- FastAPI REST APIs
- Authentication
- Persistent vector database
- Hybrid Search (BM25 + Vector Search)
- Support for DOCX and PPT files
- Citation highlighting

## 👨‍💻 Author

**Hitesh Sonawane**

AI Engineer | GenAI Developer | Python Developer

LinkedIn: https://linkedin.com/in/hitesh-sonawane-014802376

GitHub: https://github.com/HiteshSonawane05
