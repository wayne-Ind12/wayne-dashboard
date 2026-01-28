import streamlit as st
import pandas as pd
import random
import time
import hashlib
from datetime import datetime

# 1. CONFIGURACIÓN CINEMATOGRÁFICA
st.set_page_config(page_title="PASE TECH - COMMAND CENTER", layout="wide", page_icon="🦇")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    [data-testid="stMetricValue"] { color: #00d4ff; font-family: 'Share Tech Mono', monospace; }
    .stTabs [data-baseweb="tab"] { color: #888; font-weight: bold; border-bottom: 2px solid #1a1a1a; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #00d4ff; border-bottom: 2px solid #00d4ff; }
    .stChatMessage { border-radius: 5px; border-left: 5px solid #00d4ff; background-color: #0d1117; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ESTRATÉGICA (CALIDAD PREMUM)
DB_GLOBAL = {
    "Uruguay": {"m2": 2800, "Costo": 1200, "Impuesto": 9, "Status": "Estable"},
    "Suiza": {"m2": 15500, "Costo": 4800, "Impuesto": 5, "Status": "Máxima Seguridad"},
    "EAU (Dubái)": {"m2": 7800, "Costo": 2900, "Impuesto": 0, "Status": "Paraíso Fiscal"},
    "EEUU (Miami)": {"m2": 8200, "Costo": 3600, "Impuesto": 5, "Status": "Hub Tecnológico"},
    "Japón (Tokio)": {"m2": 9800, "Costo": 2600, "Impuesto": 8, "Status": "Alta Tecnología"}
}

# 3. NÚCLEO DE INTELIGENCIA (EL CEREBRO)
def motor_ia_bruno(query):
    q = query.lower()
    if any(p in q for p in ["mejor", "invertir", "dinero", "ganar"]):
        return "🧠 **Análisis:** Para preservar anonimato y capital, **Suiza** es la base ideal. Si buscas expansión rápida sin drenaje de impuestos, **Dubái** es la zona de operación recomendada."
    elif any(p in q for p in ["seguridad", "protección", "hack", "contraseña"]):
        return "🛡️ **Seguridad:** Protocolo de encriptación activado. Usa la pestaña 'THE VAULT' para generar llaves de acceso nivel 7. No uses la misma clave en dos servidores."
    elif any(p in q for p in ["hola", "estás", "quien"]):
        return "🦇 **Sistemas Activos:** Soy el asistente táctico de Pase Tech. Estoy monitoreando tus activos globales y el estado del traje. ¿Cuál es el siguiente paso?"
    else:
        return f"Procesando... Mi base de datos sugiere que '{query}' tiene relevancia estratégica. ¿Deseas un análisis de riesgo detallado?"

# 4. SISTEMA DE SEGURIDAD (THE VAULT)
def generar_password(length=24):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    return "".join(random.choice(chars) for _ in range(length))

# --- INTERFAZ DE COMANDO ---
if 'acceso_concedido' not in st.session_state: st.session_state.acceso_concedido = False

if not st.session_state.acceso_concedido:
    st.title("🔐 ACCESO RESTRINGIDO - PASE TECH")
    password = st.text_input("Ingresa Código de Acceso Táctico", type="password")
    if st.button("AUTENTICAR"):
        if password == "bruno": # CAMBIA TU CLAVE AQUÍ
            st.session_state.acceso_concedido = True
            st.success("Identidad verificada. Bienvenido, Señor.")
            st.rerun()
        else:
            st.error("Acceso denegado. Intento de intrusión registrado.")
else:
    # EL DASHBOARD UNIFICADO
    st.title("🦇 PASE TECH: COMMAND CENTER")
    tabs = st.tabs(["🧠 PASE AI", "🔑 THE VAULT", "🌍 GLOBAL PLANNER", "🏢 INMUEBLES PRO", "🦾 TACTICAL & BIO"])

    # 1. PASE AI
    with tabs[0]:
        st.subheader("Interfase de Inteligencia")
        if 'msgs' not in st.session_state: st.session_state.msgs = []
        for m in st.session_state.msgs:
            with st.chat_message(m["role"]): st.write(m["content"])
        if p := st.chat_input("Escribe una orden..."):
            st.session_state.msgs.append({"role": "user", "content": p})
            with st.chat_message("user"): st.write(p)
            res = motor_ia_bruno(p)
            st.session_state.msgs.append({"role": "assistant", "content": res})
            with st.chat_message("assistant"): st.write(res)

    # 2. THE VAULT (EXCLUSIVO)
    with tabs[1]:
        st.subheader("🔒 Bóveda de Encriptación")
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.write("Genera contraseñas imposibles de romper por fuerza bruta.")
            long = st.slider("Longitud de Bits", 12, 64, 32)
            if st.button("GENERAR LLAVE MAESTRA"):
                nueva_clave = generar_password(long)
                st.code(nueva_clave, language='text')
                st.warning("⚠️ Guarda esta clave en un lugar físico. No la subas a la nube.")
        with col_v2:
            st.write("Verificador de Integridad (Hash)")
            texto = st.text_input("Texto para encriptar")
            if texto:
                st.write("Hash SHA-256:")
                st.code(hashlib.sha256(texto.encode()).hexdigest())

    # 3. GLOBAL PLANNER
    with tabs[2]:
        st.subheader("🌍 Inteligencia de Relocalización")
        dest = st.selectbox("Destino Operativo", list(DB_GLOBAL.keys()))
        info = DB_GLOBAL[dest]
        st.metric(f"Costo de Vida - {dest}", f"USD {info['Costo']}")
        st.write(f"**Estatus:** {info['Status']} | **Visa:** {info['m2']}")

    # 4. INMUEBLES PRO
    with tabs[3]:
        st.subheader("🏢 Adquisición de Sedes")
        p_sel = st.selectbox("Mercado", list(DB_GLOBAL.keys()), key="inmo")
        m2 = st.number_input("Superficie necesaria (m²)", 50, 5000, 200)
        costo_base = DB_GLOBAL[p_sel]["m2"] * m2
        impuestos = costo_base * (DB_GLOBAL[p_sel]["Impuesto"]/100)
        st.metric("Inversión de Capital", f"USD {costo_base + impuestos:,.0f}")

    # 5. TACTICAL & BIO
    with tabs[4]:
        st.subheader("🦾 Estado del Traje y Satélites")
        c_t1, c_t2 = st.columns(2)
        with c_t1:
            st.metric("Integridad del Traje", "94%", "+2%")
            bpm = st.slider("Bio-Ritmo", 40, 180, 72)
            if bpm > 130: st.error("ALERTA: Frecuencia cardíaca alta.")
        with c_t2:
            st.write("Posición Satelital: PASE-SAT 1")
            st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=600")

st.divider()
st.caption(f"PASE TECH OS v12.0 | Proyectado para Industrias Pase | {datetime.now().year}")
