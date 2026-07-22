import streamlit as st
from rag_engine import RAGEngine

st.title("Asistente RAG Documental Privado")
pregunta = st.text_input("Haz tu consulta sobre la documentación interna:")
if pregunta:
    engine = RAGEngine()
    respuesta = engine.responder_consulta(pregunta)
    st.write(respuesta)
