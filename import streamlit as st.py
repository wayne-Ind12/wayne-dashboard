import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN Y ESTILO
st.set_page_config(page_title="Pase Tech Intelligence", layout="wide", page_icon="🧠")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stChatMessage { background-color: #161b22; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MAESTRA (La fuente de conocimiento de la IA)
DB_GLOBAL = {
    "Uruguay": {"m2": 2800, "costo": 1200, "impuesto": 9, "ventaja": "Estabilidad jurídica y residencia fácil."},
    "EEUU": {"m2": 8000, "costo": 3500, "impuesto": 5, "ventaja": "Mercado más líquido del mundo y tecnología."},
    "España": {"m2": 4500, "costo": 1800, "impuesto": 10, "ventaja": "Puerta de entrada a Europa y calidad de vida."},
    "EAU (Dubái)": {"m2": 7500, "costo": 2800, "impuesto": 0, "ventaja": "0% impuestos y lujo extremo."},
    "Reino Unido": {"m2": 10000, "costo": 3200, "impuesto": 12, "ventaja": "Centro financiero global."},
    "Suiza": {"m2": 14000, "costo": 4500, "impuesto": 5, "ventaja": "Máxima seguridad bancaria y refugio de capital."}
}

# 3. EL CEREBRO DE PASE AI: Motor de Razonamiento
def cerebro_pase_ai(query):
    q = query.lower()
    
    # LÓGICA DE INVERSIÓN (Analiza la DB)
    if any(p in q for p in ["invertir", "mejor lugar", "donde compro", "dinero"]):
        # La IA busca el país con menos impuestos o mejor m2
        mejor_pais = "EAU (Dubái)" # Ejemplo de razonamiento por impuestos
        return (f"Análisis de Inversión Pase Tech: 📈\n\n"
                f"Si buscas rentabilidad bruta, el mejor lugar es **{mejor_pais}** debido a su política de 0% impuestos. "
                f"Sin embargo, si buscas seguridad a largo plazo, **Suiza** o **Uruguay** son las opciones ganadoras. "
                f"¿Tienes un presupuesto específico para decirte cuántos metros podrías comprar?")

    # LÓGICA DE VIAJES / MIGRACIÓN
    elif any(p in q for p in ["viajar", "vivir", "mudarse", "emigrar"]):
        destinos = ", ".join(DB_GLOBAL.keys())
        return (f"Planificación Global: 🌍\n\n"
                f"Tengo datos actualizados de: {destinos}. "
                f"España es ideal por el idioma y clima, pero EEUU ofrece sueldos más altos en tecnología. "
                f"¿Cuál es tu prioridad: calidad de vida o ganar más dinero?")

    # LÓGICA DE SEGURIDAD
    elif any(p in q for p in ["seguridad", "protección", "ataque", "hacker"]):
        return ("Protocolo Táctico Pase Tech: 🛡️\n\n"
                "Detecto interés en blindaje. Recomiendo cifrado de punta a punta y uso de redes VPN. "
                "Nunca operes activos financieros en redes WiFi públicas. ¿Quieres que auditemos un sistema?")

    # SALUDO Y PERSONALIDAD
    elif any(p in q for p in ["hola", "buen", "quien", "ayuda"]):
        return ("¡Hola! Soy la IA central de Pase Tech. ⚡\n\n"
                "Mi base de datos contiene información financiera, inmobiliaria y estratégica de todo el mundo. "
                "Pregúntame lo que quieras: desde '¿dónde es más barato vivir?' hasta '¿cómo protejo mis datos?'.")
    
    # RESPUESTA ABIERTA (Si no sabe algo específico, intenta ayudar)
    else:
        return ("Procesando requerimiento... No tengo una respuesta exacta en mi base de datos principal, "
                "pero como IA de Pase Tech, puedo inferir que estás buscando optimizar tus recursos. "
                "¿Te gustaría que comparemos precios de diferentes países sobre ese tema?")

# 4. INTERFAZ DE USUARIO
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("🧠 NÚCLEO IA: PASE TECH")

# Diseño de Chat
for m in st.session_state.chat_history:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Hazle una pregunta a Pase AI..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Pensamiento de la IA
    with st.spinner("Consultando satélites y bases de datos..."):
        respuesta = cerebro_pase_ai(prompt)
        st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.markdown(respuesta)

st.divider()
st.caption("Pase Tech AI v10.0 | Sistema de Inferencia Global Activo")

