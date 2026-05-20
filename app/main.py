import streamlit as st
from pdf_processor import extract_text_from_pdf
from utils import get_text_chunks
from embeddings import create_vector_store
from chatbot import ask_question

st.set_page_config(page_title="PDF Chatbot")

st.title("AI PDF Chatbot")

st.caption("Maximum allowed PDF size: 1 MB")

uploaded_pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_pdf is not None:

    # PDF size limit: 1 MB
    if uploaded_pdf.size > 1 * 1024 * 1024:

        st.error("PDF size should be less than 1 MB")

    else:

        try:

            with st.spinner("Processing PDF..."):

                raw_text = extract_text_from_pdf(uploaded_pdf)

                text_chunks = get_text_chunks(raw_text)

                create_vector_store(text_chunks)

            st.success("PDF processed successfully!")

            question = st.text_input(
                "Ask question about PDF"
            )

            if question:

                with st.spinner("Generating answer..."):

                    answer = ask_question(question)

                st.subheader("Answer")

                st.write(answer)

        except Exception as e:

            st.error(f"Error: {str(e)}")