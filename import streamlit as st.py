import streamlit as st
import pandas as pd
import numpy as np
import time
import hashlib
from datetime import datetime
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURACIÓN Y ESTILO (NEGRO/ORO)
# ==========================================
st.set_page_config(page_title="PASE TECH | GUILLERMO", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=JetBrains+Mono:wght@300;500&display=swap');
    .stApp { background-color: #000000; color: #e5e5e5; font-family: 'JetBrains Mono', monospace; }
    .header-text { font-family: 'Playfair Display', serif; color: #d4af37; font-size: 3.5rem; text-align: center; margin-bottom: 0; text-shadow: 2px 2px 10px rgba(212,175,55,0.3); }
    .sub-header { color: #888; text-align: center; letter-spacing: 5px; text-transform: uppercase; font-size: 0.8rem; margin-top: -10px; margin-bottom: 40px; }
    div[data-testid="stMetric"] { background: #0a0a0a; border: 1px solid #d4af37; border-radius: 4px; padding: 20px; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; }
    .stButton>button { background: #d4af37; color: #000; border: none; font-weight: 800; border-radius: 2px; width: 100%; transition: 0.3s; }
    .stButton>button:hover { background: #fff; box-shadow: 0 0 20px #d4af37; }
    .stTabs [data-baseweb="tab"] { color: #666; font-size: 14px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #d4af37; border-bottom: 2px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

def speak(text):
    if text:
        js_code = f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = 'es-ES';
        msg.rate = 0.9;
        window.speechSynthesis.speak(msg);
        </script>
        """
        components.html(js_code, height=0)

# ==========================================
# 2. ESTADO DEL SISTEMA
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False
if 'user_name' not in st.session_state: st.session_state.user_name = "Guillermo"
if 'key_code' not in st.session_state: st.session_state.key_code = "vale"
if 'history' not in st.session_state: st.session_state.history = []

# ==========================================
# 3. PANTALLA DE ACCESO
# ==========================================
if not st.session_state.auth:
    st.markdown("<h1 class='header-text'>PASE TECH</h1><p class='sub-header'>Definitive Edition</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.write("### 🔐 IDENTIFICACIÓN REQUERIDA")
        pass_input = st.text_input("PASSWORD", type="password")
        if st.button("INGRESAR AL SISTEMA"):
            if pass_input == st.session_state.key_code:
                st.session_state.auth = True
                speak(f"Bienvenido de nuevo, Señor {st.session_state.user_name}. El sistema está listo.")
                st.rerun()
            else:
                st.error("CLAVE INCORRECTA")
else:
    # Sidebar
    st.sidebar.markdown(f"<h2 style='color:#d4af37'>DIRECTOR: {st.session_state.user_name.upper()}</h2>", unsafe_allow_html=True)
    cash_flow = st.sidebar.number_input("Capital Liquido (USD)", value=100000000)
    
    if st.sidebar.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    st.markdown("<h1 class='header-text'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='sub-header'>Protocolo Activo: Señor {st.session_state.user_name}</p>", unsafe_allow_html=True)

    tabs = st.tabs(["🧠 ASISTENTE IA", "🏛️ TESORERÍA", "🔥 SIMULADOR CRISIS", "💹 MERCADOS", "⚙️ AJUSTES"])

    # --- TAB 1: ASISTENTE IA ---
    with tabs[0]:
        st.subheader("Consultoría Táctica")
        for chat in st.session_state.history:
            with st.chat_message(chat["role"]): st.write(chat["content"])
        if p := st.chat_input("¿Instrucciones?"):
            st.session_state.history.append({"role": "user", "content": p})
            ans = f"Señor {st.session_state.user_name}, he analizado su solicitud sobre '{p}'. Los sistemas de Pase Tech están procesando el impacto."
            st.session_state.history.append({"role": "assistant", "content": ans})
            st.rerun()

    # --- TAB 2: TESORERÍA ---
    with tabs[1]:
        st.subheader("Análisis de Patrimonio")
        c1, c2, c3 = st.columns(3)
        c1.metric("NET WORTH TOTAL", f"${cash_flow * 1.5:,.2f}", "+5.2%")
        c2.metric("EFICIENCIA FISCAL", "98%")
        c3.metric("RIESGO", "Bajo")
        st.area_chart(np.random.randn(20, 1).cumsum() + cash_flow)

    # --- TAB 3: SIMULADOR DE CRISIS (NUEVO) ---
    with tabs[2]:
        st.subheader("Simulación de Escenarios Extremos")
        st.warning("Advertencia: Estos escenarios calculan pérdidas patrimoniales severas.")
        
        col_c1, col_c2, col_c3 = st.columns(3)
        
        with col_c1:
            if st.button("🚨 COLAPSO CRIPTO"):
                perdida = cash_flow * 0.40
                st.error(f"Impacto: -${perdida:,.2f}")
                speak(f"Señor {st.session_state.user_name}, caída masiva del mercado cripto detectada. Pérdida del cuarenta por ciento del capital líquido. Activando protocolos de resguardo.")
        
        with col_c2:
            if st.button("🍞 HIPERINFLACIÓN"):
                st.info("Poder adquisitivo reducido en un 60%")
                speak(f"Señor {st.session_state.user_name}, la moneda está perdiendo valor aceleradamente. Sugiero convertir liquidez a oro físico de inmediato.")

        with col_c3:
            if st.button("⚔️ GUERRA TECH"):
                st.warning("Activos en MSFT y SONY congelados.")
                speak(f"Señor {st.session_state.user_name}, conflicto geopolítico detectado. Sus acciones tecnológicas han sido bloqueadas. Iniciando cifrado de activos en Suiza.")

        st.write("---")
        st.write("### Análisis de Estrés Patrimonial")
        st.latex(r"Riesgo = \frac{\Delta Assets}{\text{Liquidez}} \times \text{Volatilidad}")

    # --- TAB 4: MERCADOS ---
    with tabs[3]:
        st.subheader("Global Market Hub")
        m1, m2, m3 = st.columns(3)
        m1.metric("BITCOIN", "$68,500", "+2.1%")
        m2.metric("ORO (OZ)", "$2,455", "+0.3%")
        m3.metric("MSFT", "$422", "-0.1%")

    # --- TAB 5: AJUSTES ---
    with tabs[4]:
        st.subheader("Configuración")
        st.session_state.user_name = st.text_input("Nombre", value=st.session_state.user_name)
        st.session_state.key_code = st.text_input("Clave", value=st.session_state.key_code, type="password")
        if st.button("GUARDAR"):
            st.success("Sincronizado.")
            speak("Configuración guardada.")

st.divider()
st.caption(f"PASE TECH | DEFINITIVE EDITION v23.0 | {st.session_state.user_name.upper()}")
