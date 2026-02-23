# 🚀 Lab 2 — Implementación de un RAG con OpenAI + Pinecone + LangChain

## 📌 Descripción del Proyecto

Este proyecto implementa un sistema de **Retrieval-Augmented Generation (RAG)** utilizando:

- **OpenAI** para embeddings y modelo de lenguaje (LLM)
- **Pinecone** como base de datos vectorial
- **LangChain** para orquestar el flujo completo

El objetivo es construir un pipeline donde el modelo no responde solo con su conocimiento interno, sino que primero recupera información relevante desde una base vectorial y luego genera la respuesta utilizando ese contexto.

---

## 🎯 Objetivos del Laboratorio

- Comprender el funcionamiento de los embeddings.
- Crear y configurar un índice en Pinecone.
- Indexar documentos en una base vectorial.
- Implementar un sistema de recuperación (retriever).
- Integrar el contexto recuperado en un prompt.
- Generar respuestas aumentadas mediante un LLM.

---

## 🏗 Arquitectura del Sistema RAG

```
Usuario
   ↓
Embedding (OpenAI)
   ↓
Pinecone (Vector Database - búsqueda por similitud)
   ↓
Retriever (LangChain)
   ↓
Prompt con contexto recuperado
   ↓
LLM (OpenAI)
   ↓
Respuesta final
```

---

## 🔎 Explicación de Componentes

### 🔹 OpenAI Embeddings
Convierte texto en vectores numéricos de dimensión 1536 utilizando el modelo:

```
text-embedding-3-small
```

Estos vectores permiten realizar búsquedas semánticas.

---

### 🔹 Pinecone
Base de datos vectorial donde se almacenan los embeddings.
Configuración utilizada:

- Vector type: Dense
- Dimensión: 1536
- Métrica: cosine
- Deployment: Serverless

---

### 🔹 LangChain
Framework que conecta:

- Embeddings
- Vector store (Pinecone)
- Retriever
- LLM
- PromptTemplate

Permite construir el pipeline completo de RAG de forma modular.

---

## 🧰 Tecnologías Utilizadas

- Python 3.11
- LangChain
- OpenAI API
- Pinecone
- python-dotenv
- Entorno virtual (.venv)

---

## 📁 Estructura del Proyecto

```
rag-openai-pinecone-langchain/
├── data/
│   └── sample.txt
├── src/
│   ├── ingest.py
│   └── ask.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone <URL_DEL_REPO>
cd rag-openai-pinecone-langchain
```

---

### 2️⃣ Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno virtual:

En Git Bash (Windows):

```bash
source .venv/Scripts/activate
```

En PowerShell:

```bash
.venv\Scripts\activate
```

---

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar variables de entorno

Crear un archivo `.env` basado en `.env.example`:

```
OPENAI_API_KEY=tu_api_key
PINECONE_API_KEY=tu_api_key
PINECONE_INDEX_NAME=rag-lab-index
```

⚠️ IMPORTANTE:
- No subir el archivo `.env` a GitHub.
- El índice debe existir previamente en Pinecone.
- El índice debe tener dimensión 1536 y métrica cosine.

---

## ▶️ Flujo de Ejecución

### 1️⃣ Ingestar documentos

Este paso convierte el texto en embeddings y los almacena en Pinecone:

```bash
python src/ingest.py
```

Salida esperada:

```
Ingesta completada. Documentos indexados en Pinecone.
```

---

### 2️⃣ Realizar consulta (RAG)

```bash
python src/ask.py
```

El sistema:

1. Convierte la pregunta en embedding.
2. Busca documentos similares en Pinecone.
3. Inserta el contexto recuperado en el prompt.
4. Genera la respuesta usando el modelo OpenAI.

---

## 🧠 Ejemplo de Uso

Pregunta:

```
¿Qué es Pinecone y para qué sirve?
```

El sistema recupera el contenido relevante desde `sample.txt` y genera una respuesta contextualizada.

---

## 🏁 Conclusiones

Este proyecto permitió:

- Comprender el funcionamiento interno de un sistema RAG.
- Implementar recuperación semántica mediante embeddings.
- Integrar Pinecone como base vectorial.
- Construir un flujo completo de generación aumentada.
- Diferenciar entre un LLM simple y un sistema RAG.

Este repositorio representa la implementación completa de un sistema RAG utilizando herramientas modernas de IA.

---

## 👨‍💻 Autor

Estudiante del laboratorio de Introducción a Retrieval-Augmented Generation con OpenAI y Pinecone.