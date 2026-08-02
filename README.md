# 🩺 Medical AI Chatbot

An AI-powered Medical Chatbot built using **Streamlit**, **LangChain**, **FAISS**, **Hugging Face Embeddings**, and **Groq LLM**. The chatbot answers medical questions based on a custom medical knowledge base using Retrieval-Augmented Generation (RAG).

## 🔗 Live Demo

- **🌐 Streamlit App:** https://medical-ai-chatbot-dwtkryttogysy3tqinncv6.streamlit.app/
- **💻 GitHub Repository:** https://github.com/ABHISHEK830SHARMA/Medical-AI-Chatbot

---

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Medical document-based question answering
- 🔎 FAISS vector database for semantic search
- 🤖 Groq Llama 3.1 (8B Instant) language model
- 📝 Sentence Transformers for embeddings
- ⚡ Fast and lightweight architecture

---

## 🛠️ Tech Stack

- Python 3.11+
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Sentence Transformers
- Groq API
- Transformers
- PyTorch

---

## 📂 Project Structure

```text
Medical-AI-Chatbot/
│
├── data/
│   └── Medical Documents
│
├── templates/
│
├── vectorstore/
│   └── db_faiss/
│       ├── index.faiss
│       └── index.pkl
│
├── app.py
├── streamlit_app.py
├── create_memory_llm.py
├── connect_memory_with_llm.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ABHISHEK830SHARMA/Medical-AI-Chatbot.git
```

```bash
cd Medical-AI-Chatbot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

For Streamlit Cloud, add the key inside **App Settings → Secrets**

```toml
GROQ_API_KEY="your_groq_api_key"
```

---

## ▶️ Run the Application

### Streamlit

```bash
streamlit run streamlit_app.py
```

### Flask (Optional)

```bash
python app.py
```

---

## 💡 How It Works

1. Medical documents are converted into embeddings.
2. Embeddings are stored in a FAISS vector database.
3. User enters a medical question.
4. Relevant documents are retrieved using semantic search.
5. Retrieved context is sent to the Groq Llama model.
6. The chatbot generates an answer based only on the retrieved documents.

---

## 📦 Dependencies

Main libraries used:

- streamlit
- langchain
- langchain-community
- langchain-groq
- langchain-huggingface
- sentence-transformers
- transformers
- faiss-cpu
- torch
- python-dotenv

---

## 📸 Demo

Add screenshots of your application here.

```
images/
    home.png
    chatbot.png
```

---

## 🚀 Deployment

The application can be deployed on:

- Streamlit Community Cloud
- Render
- Railway
- Azure App Service

---

## ⚠️ Disclaimer

This chatbot is intended for educational and informational purposes only.

It should not be considered a substitute for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional regarding medical concerns.

---

## 👨‍💻 Author

**Abhishek Sharma**

GitHub:
https://github.com/ABHISHEK830SHARMA

---

## ⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork the repository

🐞 Report issues

🤝 Submit pull requests

---

## 📄 License

This project is licensed under the MIT License.
