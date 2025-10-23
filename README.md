# YukTravel Chatbot Lokal (Offline)

Travel Assistant Chatbot berbasis LLM yang dijalankan Ollama (dijalankan lokal) menggunakan  model LLM3. berfungsi sebagai asisten virtual untuk membantu pengguna menemukan, membandingkan, dan memahami berbagai paket join trip dari [YukTravel.com](https://www.yuktravel.com/).

Chatbot ini membaca ratusan data paket dari file JSON, lalu menggunakan kombinasi RAG, embedding BGE, dan Chroma vector database untuk memberikan jawaban yang akurat dan kontekstual dan dijalankan dengan Python.

---

## Fitur Utama

- RAG — Menggabungkan kemampuan LLM dengan data internal agar jawaban tetap akurat.
- Embedding (BGE) & Vector DB (Chroma) — Mengubah deskripsi paket wisata menjadi representasi vektor untuk pencarian semantik.
- LLM Integration (Ollama) - Menggunakan model llm3 melalui Ollama untuk menghasilkan respon natural dan kecepatan bergantung pada device
- Conversational Memory — mampu mengingat konteks percakapan sebelumnya.

## Cara Menjalankan

### 1. Clone repository
```bash
git clone https://github.com/zuhdipati/chatbot_yuktravel.git
pip install -r requirements.txt
python -m chatbot
```

### 2. Jalankan ollama pada terminal lain
```bash
ollama serve
```

### 3. Jalankan project, lalu anda akan berinteraksi di terminal
```bash
python -m chatbot
```


