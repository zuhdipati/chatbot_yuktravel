# 🧭 YukTravel Chatbot

Travel Assistant Chatbot adalah sistem AI berbasis LLM (Large Language Model) yang  dijalankan Ollama untuk model llm3. berfungsi sebagai asisten virtual untuk membantu pengguna menemukan, membandingkan, dan memahami berbagai paket join trip dari [YukTravel.com](https://www.yuktravel.com/).

Chatbot ini membaca ratusan data paket dari file JSON, lalu menggunakan kombinasi RAG (Retrieval-Augmented Generation), embedding Hugging Face, dan Chroma vector database untuk memberikan jawaban yang akurat dan kontekstual dan dijalankan dengan Python.

---

## ✨ Fitur Utama

- LLM + RAG — menghasilkan jawaban berdasarkan pengetahuan nyata dari data paket wisata.
- JSON Data Loader — membaca ratusan paket perjalanan dari file JSON.
- Embedding Hugging Face — untuk representasi semantik teks paket wisata.
- Chroma Vector Store — penyimpanan embedding untuk pencarian cepat dan efisien.
- Conversational Memory — mampu mengingat konteks percakapan sebelumnya.

## 🚀 Cara Menjalankan

### 1. Jalankan ollama pada terminal lain
```bash
ollama serve
```

### 2. Clone repository
```bash
git clone https://github.com/zuhdipati/chatbot_yuktravel.git
cd chatbot_yuktravel
pip install -r requirements.txt
python -m chatbot
