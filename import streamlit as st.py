import streamlit as st
import pandas as pd
import numpy as np
import time
import hashlib
import random
from datetime import datetime
import streamlit.components.v1 as components

# ==========================================
# 1. ARQUITECTURA VISUAL Y SISTEMA DE VOZ
# ==========================================
st.set_page_config(page_title="PASE TECH | THE ORACLE", layout="wide", page_icon="🎙️")

# CSS Estilo "Cyber-Industrial"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #020305; color: #00d4ff; font-family: 'Share Tech Mono', monospace; }
    .main-header { font-family: 'Syncopate', sans-serif; color: #ffffff; text-shadow: 0 0 10px #00d4ff; }
    div[data-testid="stMetric"] { background: #080c12; border: 1px solid #00d4ff; padding: 20px; border-radius: 5px; }
    .stTabs [data-baseweb="tab"] { color: #555; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Voz (JavaScript Bridge)
def voice_component(text_to_speak=""):
    # Este script permite que la web hable
    if text_to_speak:
        js_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{text_to_speak}');
        msg.lang = 'es-ES';
        msg.rate = 1.0;
        window.speechSynthesis.speak(msg);
        </script>
        """
        components.html(js_code, height=0)

# ==========================================
# 2. DATA MASTER (GLOBAL INTELLIGENCE)
# ==========================================
DB_GLOBAL = {
    "Suiza": {"m2": 15800, "Tax": 5, "Costo": 4900, "Safe": 98, "Tech": 92},
    "EAU": {"m2": 7900, "Tax": 0, "Costo": 3100, "Safe": 90, "Tech": 94},
    "Uruguay": {"m2": 2850, "Tax": 9, "Costo": 1250, "Safe": 82, "Tech": 75},
    "Singapur": {"m2": 18500, "Tax": 2, "Costo": 4200, "Safe": 99, "Tech": 97}
}

ASSETS = {"BTC": 66450, "GOLD": 2380, "SONY": 94, "MSFT": 425}

# ==========================================
# 3. FUNCIONES DE IA Y TESORERÍA
# ==========================================
def process_command(cmd, wealth):
    cmd = cmd.lower()
    if "quien" in cmd or "quién" in cmd:
        return "Soy The Oracle, la interfaz de inteligencia de Pase Tech. Estoy a su servicio, señor."
    elif "inversión" in cmd or "invertir" in cmd:
        return f"Con un patrimonio de ${wealth:,.0f}, mi recomendación táctica es diversificar en Dubái por su tasa impositiva cero."
    elif "status" in cmd or "estado" in cmd:
        return "Sistemas operativos al cien por ciento. Red de satélites sincronizada. Sin amenazas detectadas."
    return "Comando procesado. Esperando instrucciones adicionales."

# ==========================================
# 4. DASHBOARD PRINCIPAL
# ==========================================

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h1 class='main-header'>PASE TECH | ORACLE LOGIN</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        pin = st.text_input("IDENTIDAD BIOMÉTRICA (PASSWORD)", type="password")
        if st.button("ACCEDER"):
            if pin == "vale":
                st.session_state.auth = True
                voice_component("Acceso concedido. Bienvenido, Señor.")
                st.rerun()
else:
    # --- INTERFAZ ACTIVA ---
    st.sidebar.markdown("<h2 class='main-header'>ORACLE OS</h2>", unsafe_allow_html=True)
    cash = st.sidebar.number_input("Liquidez (USD)", value=1500000)
    m2_total = st.sidebar.number_input("Inmuebles (m2)", value=300)
    loc = st.sidebar.selectbox("Base de Datos Regional", list(DB_GLOBAL.keys()))
    
    total_wealth = cash + (m2_total * DB_GLOBAL[loc]["m2"])

    tabs = st.tabs(["🧠 NEURAL CORE", "💹 TREASURY", "🏢 REAL ESTATE", "🛡️ SECURITY", "🧬 BIOTECH", "🛰️ SPACE OPS"])

    # --- TAB 1: NEURAL CORE (VOZ ACTIVA) ---
    with tabs[0]:
        st.subheader("Interfase de Voz y Mente")
        if 'chat' not in st.session_state: st.session_state.chat = []
        
        for m in st.session_state.chat:
            with st.chat_message(m["role"]): st.write(m["content"])

        if p := st.chat_input("Hable o escriba su comando..."):
            st.session_state.chat.append({"role": "user", "content": p})
            with st.chat_message("user"): st.write(p)
            
            res = process_command(p, total_wealth)
            st.session_state.chat.append({"role": "assistant", "content": res})
            
            with st.chat_message("assistant"):
                st.write(res)
                voice_component(res) # LA IA HABLA AQUÍ

    # --- TAB 2: TREASURY (PROYECCIONES) ---
    with tabs[1]:
        st.subheader("Financial Intelligence")
        col_t1, col_t2 = st.columns(2)
        col_t1.metric("NET WORTH", f"${total_wealth:,.0f}")
        col_t2.metric("ASSET CLASS", "A-1 EXTREME")
        
        st.write("### Proyección de Crecimiento Intergeneracional")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Propiedades', 'Acciones', 'Cripto']
        ).cumsum()
        st.line_chart(chart_data)
        
        # Fórmula de valoración
        st.latex(r"Empire\_Value = \sum (V_{assets}) + (Area \times P_{m2}) - \text{Tax}_{liability}")

    # --- TAB 3: REAL ESTATE ---
    with tabs[2]:
        st.subheader("Global HQ Acquisition")
        col_r1, col_r2 = st.columns([2, 1])
        with col_r1:
            st.write("Comparativa de Mercados Globales")
            df_glob = pd.DataFrame(DB_GLOBAL).T
            st.bar_chart(df_glob[['Safe', 'Tech']])
        with col_r2:
            st.info(f"Análisis en {loc}:")
            st.write(f"Impuestos: {DB_GLOBAL[loc]['Tax']}%")
            st.write(f"Costo Vida: ${DB_GLOBAL[loc]['Costo']}")

    # --- TAB 4: SECURITY (CRYPTO VAULT) ---
    with tabs[3]:
        st.subheader("Cybersecurity Command")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            if st.button("BLOQUEO DE EMERGENCIA"):
                voice_component("Protocolo de emergencia activado. Cerrando accesos.")
                st.error("TODOS LOS ACCESOS EXTERNOS HAN SIDO ELIMINADOS.")
        with col_s2:
            st.write("Generador de Encriptación Cuántica")
            if st.button("GENERAR HASH RSA"):
                h = hashlib.sha256(str(time.time()).encode()).hexdigest()
                st.code(h)

    # --- TAB 5: BIOTECH ---
    with tabs[4]:
        st.subheader("Elite Performance Lab")
        bpm = st.slider("Ritmo Cardíaco (Traje)", 40, 180, 70)
        if bpm > 140:
            st.warning("⚠️ Adrenalina fuera de rango operativo.")
            voice_component("Señor, su ritmo cardíaco es elevado. Inicie protocolo de respiración.")
        st.line_chart(np.random.normal(70, 5, 50))

    # --- TAB 6: SPACE OPS ---
    with tabs[5]:
        st.subheader("Satellite Reconnaissance")
        st.write("Ubicación de Satélite: PASE-SAT 01")
        # Simulación de coordenadas
        lat, lon = 34.0522, -118.2437
        st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

st.divider()
st.caption(f"PASE TECH | THE ORACLE v17.0 | Sincronización de Voz Activa | {datetime.now().year}")


