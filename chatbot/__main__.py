from .loader import load_and_split
from .embedder import build_vectorstore
from .chain import build_chain
from .chatbot import run_chatbot

def main():
    chunks = load_and_split()
    db = build_vectorstore(chunks)
    qa = build_chain(db)
    run_chatbot(qa)

if __name__ == "__main__":
    main()
