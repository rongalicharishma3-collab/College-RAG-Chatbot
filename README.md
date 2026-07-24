# 🎓 College Information Chatbot (RAG-Based AI Assistant)

An AI-powered College Information Chatbot built using **Python, LangChain, Streamlit, FAISS, Hugging Face Embeddings, and Groq Llama 3.3**.

The chatbot uses **Retrieval-Augmented Generation (RAG)** to answer user questions only from uploaded college PDF documents, ensuring accurate and context-aware responses while preventing hallucinations.

---

# 📌 Project Overview

Students often struggle to find important information such as:

- Attendance Rules
- Examination Guidelines
- Fee Structure
- Hostel Rules
- Placement Policies
- Academic Regulations

Instead of manually searching lengthy PDF documents, this chatbot allows users to simply ask questions in natural language.

The chatbot retrieves the most relevant information from uploaded documents and generates an accurate answer using a Large Language Model (LLM).

---

# 🚀 Features

✅ Upload College PDF Documents

✅ Automatic PDF Text Extraction

✅ Intelligent Text Chunking

✅ Vector Embedding Generation

✅ FAISS Vector Database

✅ Semantic Search

✅ Context-aware Question Answering

✅ Groq Llama 3.3 Integration

✅ Prompt Engineering

✅ Conversation History

✅ Source Document Display

✅ Hallucination Prevention

---

# 🏗️ System Architecture

```
                User Question
                      │
                      ▼
             Streamlit Web Interface
                      │
                      ▼
             FAISS Vector Retriever
                      │
                      ▼
        Top Relevant Document Chunks
                      │
                      ▼
          Prompt + Retrieved Context
                      │
                      ▼
          Groq Llama 3.3 Language Model
                      │
                      ▼
               Final AI Response
```

---

# 📂 Project Structure

```
College-RAG-Chatbot/
│
├── app.py
├── .env
├── requirements.txt
│
├── data/
│   ├── CollegeRuleBook.pdf
│   ├── StudentHandbook.pdf
│   └── AcademicPolicy.pdf
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
└── utils/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── vector_store.py
    └── rag_chain.py
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Framework |
| Groq API | Large Language Model |
| Llama 3.3 70B | AI Model |
| FAISS | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| PyPDFLoader | PDF Processing |
| RecursiveCharacterTextSplitter | Text Chunking |

---

# ⚙️ Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/College-RAG-Chatbot.git
```

---

## Step 2

Go inside the project

```bash
cd College-RAG-Chatbot
```

---

## Step 3

Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Step 4

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5

Create `.env`

```
GROQ_API_KEY=your_groq_api_key
```

---

## Step 6

Run Application

```bash
streamlit run app.py
```

---

# 📚 Workflow

## Step 1

Upload College PDF Documents.

↓

## Step 2

Load PDFs using **PyPDFLoader**

↓

## Step 3

Split documents into chunks.

↓

## Step 4

Generate embeddings using

```
sentence-transformers/all-MiniLM-L6-v2
```

↓

## Step 5

Store vectors inside FAISS.

↓

## Step 6

User asks a question.

↓

## Step 7

Retriever searches similar chunks.

↓

## Step 8

Retrieved context is sent to Groq Llama 3.3.

↓

## Step 9

LLM generates final answer.

↓

## Step 10

Display answer with source documents.

---

# 🧠 Prompt Engineering

The chatbot follows strict rules:

- Answer only from retrieved context.
- Never use outside knowledge.
- Never hallucinate.
- If information is unavailable, reply:

```
This information was not found in the uploaded documents.
```

- Keep answers concise.
- Mention relevant rules whenever available.

---

# 📖 Context Engineering

To improve answer quality:

- Retrieves Top-3 relevant chunks.
- Removes duplicate chunks.
- Combines retrieved chunks into a single context.
- Sends only relevant information to the LLM.
- Displays source documents.

---

# 🔍 Vector Search

Embeddings are generated using:

```
sentence-transformers/all-MiniLM-L6-v2
```

Vector Database:

```
FAISS
```

Advantages:

- Fast similarity search
- Semantic retrieval
- Scalable
- Lightweight

---

# 💬 Example Questions

```
What is the attendance requirement?

What is the placement eligibility?

What are the library timings?

How many internal exams are conducted?

What is the hostel fee?

Explain the examination policy.
```

---


# 🔮 Future Enhancements

- Multi-PDF Support
- Voice Input
- OCR for Scanned PDFs
- Chat Memory
- Admin Dashboard
- Authentication
- Multi-language Support
- Cloud Deployment
- Document Upload through UI
- Citation Highlighting

---

# 📈 Learning Outcomes

Through this project, I learned:

- Retrieval-Augmented Generation (RAG)
- LangChain
- Vector Databases
- FAISS
- HuggingFace Embeddings
- Prompt Engineering
- Context Engineering
- Groq API Integration
- Streamlit Development
- Semantic Search

---

# 👨‍💻 Author

**Rongali Charishma**

B.Tech Integrated in Data Science

GitHub: https://github.com/rongalicharishma3-collab

LinkedIn: https://www.linkedin.com/in/charishma-rongali-80a8b831/

---

# ⭐ If you found this project helpful, please consider giving it a Star!
