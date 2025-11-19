from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from .config import EMBEDDING_MODEL, CHROMA_DIR

def build_vectorstore(chunks):
    print("membuat embedding dgn bge dan masuk ke chroma..")
    embedding = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    db = Chroma.from_documents(chunks, embedding, persist_directory=CHROMA_DIR)
    print("chroma selesai dibuat")
    return db
