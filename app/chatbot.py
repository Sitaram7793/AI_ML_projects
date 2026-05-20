import os
from dotenv import load_dotenv
from google import genai  # Correct modern import
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

client = genai.Client()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def ask_question(user_question):
    vector_store = FAISS.load_local(
        "vector_store/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    docs = vector_store.similarity_search(user_question)
    context = " ".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based only on the provided context.

    Context:
    {context}

    Question:
    {user_question}
    """

    # Use client.models.generate_content with the current model identifier
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Upgraded to a modern, supported version
        contents=prompt,
    )

    return response.text
