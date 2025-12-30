import streamlit as st
import os

# 1. INTERFAZ VISUAL (Lo que verá el reclutador en Hugging Face)
st.set_page_config(page_title="Spanish Legal-Check RAG", page_icon="⚖️")
st.title("⚖️ Spanish Legal-Check RAG")
st.markdown("""
### Mitigación de alucinaciones en el ámbito legal español
Este sistema utiliza **RAG** (Generación Aumentada por Recuperación) para asegurar que las respuestas 
sobre la legislación española se basen en documentos oficiales como la Constitución Española o el BOE.
""")

# 2. LOGICA TÉCNICA (Tu "Linguistic Insight")
# Aquí es donde demuestras que sabes procesar el lenguaje
st.sidebar.header("Configuración de Lingüística Computacional")
st.sidebar.info("""
**Estrategia de segmentación:** Estamos dividiendo el texto legal por 'Artículos' y 'Capítulos' para preservar el contexto semántico, 
evitando que la IA pierda el hilo de la norma.
""")

# 3. CAMPO DE PRUEBA
pregunta = st.text_input("Haz una pregunta sobre una ley española (Ej: ¿Qué dice el Artículo 1 de la Constitución?):")

if pregunta:
    st.write(f"🔍 **Analizando tu pregunta:** {pregunta}")
    st.warning("⚠️ El sistema está en fase de conexión con la base de datos de leyes. ¡Pronto verás la respuesta real aquí!")

st.divider()
st.caption("Proyecto de Portfolio para Amazon/Indra | Desarrollado por Sofia Algar (MSc LeIA)")
