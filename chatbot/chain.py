from langchain_community.llms import Ollama
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from .config import MODEL_NAME

PROMPT_TEMPLATE = """
Kamu adalah asisten customer service travel yang hanya menjawab berdasarkan data berikut.

{context}

Pertanyaan: {question}

Jawablah berdasarkan data di atas. Jika tidak ada informasi yang cocok, jawab dengan:
"Maaf, saya tidak menemukan data tersebut."
"""

def build_chain(db):
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    llm = Ollama(model=MODEL_NAME, temperature=0.2)
    retriever = db.as_retriever(search_kwargs={"k": 5})

    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )
    return qa
