from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def load_and_split():
    print("load data json...")
    loader = JSONLoader(file_path=DATA_PATH, jq_schema=".[]", text_content=False)
    docs = loader.load()
    print(f"{len(docs)} dokumen berhasil dimuat.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(docs)
    print(f"total {len(chunks)} potongan teks siap diembed")
    return chunks
