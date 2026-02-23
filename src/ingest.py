import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore

def main():
    load_dotenv()

    openai_key = os.getenv("OPENAI_API_KEY")
    pinecone_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    if not openai_key or not pinecone_key or not index_name:
        raise ValueError("Faltan variables en .env. Revisa OPENAI_API_KEY, PINECONE_API_KEY y PINECONE_INDEX_NAME")

    # 1) Leer texto de ejemplo
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        text = f.read().strip()

    # 2) Crear documento
    docs = [Document(page_content=text, metadata={"source": "sample.txt"})]

    # 3) Crear embeddings (OpenAI)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # 4) Guardar en Pinecone
    PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name=index_name,
    )

    print(f"✅ Ingesta completada. Documentos indexados en Pinecone: {index_name}")

if __name__ == "__main__":
    main()