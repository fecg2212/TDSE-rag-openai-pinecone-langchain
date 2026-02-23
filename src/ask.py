import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate

def main():
    load_dotenv()

    openai_key = os.getenv("OPENAI_API_KEY")
    pinecone_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    if not openai_key or not pinecone_key or not index_name:
        raise ValueError("Faltan variables en .env. Revisa OPENAI_API_KEY, PINECONE_API_KEY y PINECONE_INDEX_NAME")

    # Embeddings para consultas
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # VectorStore (Pinecone)
    vectorstore = PineconeVectorStore(
        index_name=index_name,
        embedding=embeddings,
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "Responde en español usando SOLO el contexto. "
         "Si el contexto no es suficiente, responde: 'No tengo suficiente información en los documentos'."),
        ("human", "Contexto:\n{contexto}\n\nPregunta:\n{pregunta}")
    ])

    pregunta = input("Pregunta: ").strip()

    docs = retriever.invoke(pregunta)
    contexto = "\n\n".join([d.page_content for d in docs])

    chain = prompt | llm
    respuesta = chain.invoke({"contexto": contexto, "pregunta": pregunta})

    print(f"\n📄 Documentos recuperados: {len(docs)}")
    print("\n✅ Respuesta:\n", respuesta.content)

if __name__ == "__main__":
    main()