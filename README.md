# YukTravel Chatbot (Local & Offline)

![Python](https://img.shields.io/badge/Python-3.9.6-blue)
![Ollama](https://img.shields.io/badge/Ollama-Llama3-orange)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)

**YukTravel Chatbot** adalah asisten virtual berbasis AI yang berjalan sepenuhnya secara **lokal (offline)** di komputer Anda. Chatbot ini dirancang untuk membantu pengguna mencari, membandingkan, dan memahami paket wisata dari [YukTravel.com](https://www.yuktravel.com/).

Menggunakan teknologi **RAG (Retrieval-Augmented Generation)**, chatbot ini tidak hanya "mengarang" jawaban, tetapi membaca data aktual dari database paket wisata sebelum menjawab pertanyaan Anda.

---

## Arsitektur & Teknologi
1.  **Otak (LLM):** [Ollama](https://ollama.com/) menjalankan model **Llama 3** untuk memproses bahasa manusia.
2.  **Orkestrator:** [LangChain](https://www.langchain.com/) bertugas mengatur alur percakapan dan menghubungkan LLM dengan data.
3.  **Database:** [ChromaDB](https://www.trychroma.com/) (Vector Database) untuk menyimpan data paket wisata agar mudah dicari.
4.  **Embedding:** Menggunakan model **BGE (BAAI General Embedding)** untuk menerjemahkan teks menjadi vektor angka.


## Fitur Utama
1. **100% Offline:** Data tidak dikirim ke server cloud (OpenAI/Google), menjaga privasi dan hemat biaya API.
2. **Context Aware (RAG):** Menjawab berdasarkan data nyata dari file JSON, meminimalisir halusinasi.
3. **Conversational Memory:** Dapat mengingat konteks percakapan sebelumnya.
4. **High Performance Search:** DapPencarian semantik menggunakan Vector Search (bukan sekadar keyword matching).

## Prasyarat (Prerequisites)
1. **Python** Versi 3.9.6
2. **Git**
3. **Ollama** Install Ollama [Disini](https://ollama.com/download)

## Cara Instalasi & Menjalankan

### 1. Siapkan Model 
```bash
ollama pull llama3
```

### 2. Clone repository
```bash
git clone https://github.com/zuhdipati/chatbot_yuktravel.git
cd chatbot_yuktravel
pip install -r requirements.txt
```

### 3. Jalankan ollama pada terminal lain
```bash
ollama serve
```

### 4. Jalankan project, lalu anda akan berinteraksi di terminal
```bash
python -m chatbot
```

Note:
1. Disarankan menggunakan virtual env sebelum pip install
2. Anda bisa menggunakan data json anda sendiri
