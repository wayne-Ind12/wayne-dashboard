import streamlit as st
import pandas as pd
import numpy as np
import time
import hashlib
import random
from datetime import datetime
import streamlit.components.v1 as components

# ==========================================
# 1. ARQUITECTURA VISUAL: LUXURY TECH (NEGRO/ORO)
# ==========================================
st.set_page_config(page_title="PASE TECH | DEFINITIVE EDITION", layout="wide", page_icon="🔱")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=JetBrains+Mono:wght@300;500&display=swap');
    
    .stApp { background-color: #000000; color: #e5e5e5; font-family: 'JetBrains Mono', monospace; }
    
    /* Encabezado de Oro */
    .header-text { font-family: 'Playfair Display', serif; color: #d4af37; font-size: 3.5rem; text-align: center; margin-bottom: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
    .sub-header { color: #888; text-align: center; letter-spacing: 5px; text-transform: uppercase; font-size: 0.8rem; margin-top: -10px; margin-bottom: 40px; }

    /* Tarjetas y Métricas */
    div[data-testid="stMetric"] { background: linear-gradient(180deg, #0a0a0a 0%, #111 100%); border: 1px solid #d4af37; border-radius: 0px; padding: 25px; box-shadow: 0 4px 20px rgba(212,175,55,0.1); }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.2rem !important; }

    /* Botones de Mando */
    .stButton>button { background: #d4af37; color: #000; border: none; font-weight: 800; border-radius: 0px; height: 55px; letter-spacing: 2px; transition: 0.4s; }
    .stButton>button:hover { background: #fff; color: #d4af37; box-shadow: 0 0 25px #d4af37; }

    /* Chat y Tabs */
    .stChatMessage { border-bottom: 1px solid #d4af37; background: transparent; padding: 20px; }
    .stTabs [data-baseweb="tab"] { color: #666; font-size: 12px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #d4af37; border-bottom: 2px solid #d4af37; }
    
    /* Input personalizado */
    .stTextInput>div>div>input { background-color: #0a0a0a; border: 1px solid #333; color: #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# Motor de Voz Oracle
def speak(text):
    if text:
        js = f"<script>var m = new SpeechSynthesisUtterance('{text}'); m.lang='es-ES'; m.rate=0.95; window.speechSynthesis.speak(m);</script>"
        components.html(js, height=0)

# ==========================================
# 2. LOGICA DE PERSONALIZACIÓN Y MEMORIA
# ==========================================
if 'user_name' not in st.session_state: st.session_state.user_name = "Guillermo"
if 'key_code' not in st.session_state: st.session_state.key_code = "vale"
if 'chat_log' not in st.session_state: st.session_state.chat_log = []

def ia_asistente(query):
    q = query.lower()
    name = st.session_state.user_name
    if "hola" in q or "quien eres" in q:
        return f"Hola, Señor {name}. Soy su asistente de Pase Tech. Mi misión es proteger su capital y expandir su influencia global. ¿En qué puedo asistirle hoy?"
    elif "dinero" in q or "patrimonio" in q:
        return f"Señor {name}, su patrimonio actual está optimizado. Sin embargo, detecto una oportunidad de arbitraje en Singapur que podría interesarle."
    elif "personalizar" in q or "ajustar" in q:
        return "He habilitado el módulo de Configuración del Imperio para que usted defina las reglas del sistema."
    return f"Entendido, Señor {name}. Procesando su solicitud con prioridad nivel 1."

# ==========================================
# 3. ACCESO DE SEGURIDAD
# ==========================================
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h1 class='header-text'>PASE TECH</h1><p class='sub-header'>Definitive Edition</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with col2 := c2:
        st.write("### 🔐 ACCESO RESTRINGIDO")
        pass_input = st.text_input("CLAVE TÁCTICA", type="password")
        if st.button("AUTENTICAR"):
            if pass_input == st.session_state.key_code:
                st.session_state.auth = True
                speak(f"Bienvenido, Señor {st.session_state.user_name}. Sistemas en línea.")
                st.rerun()
            else: st.error("ACCESO DENEGADO.")
else:
    # --- DASHBOARD CORPORATIVO ---
    st.sidebar.markdown(f"<h2 style='color:#d4af37'>SYSTEM: ONLINE</h2>", unsafe_allow_html=True)
    st.sidebar.write(f"DIRECTOR: **{st.session_state.user_name.upper()}**")
    
    # Parámetros Globales
    cash = st.sidebar.number_input("LIQUIDEZ ACTUAL (USD)", value=50000000)
    m2_total = st.sidebar.number_input("METROS CUADRADOS TOTALES", value=2500)
    
    if st.sidebar.button("CERRAR SESIÓN"):
        st.session_state.auth = False
        st.rerun()

    st.markdown(f"<h1 class='header-text'>COMMAND CENTER</h1><p class='sub-header'>Bienvenido, Señor {st.session_state.user_name}</p>", unsafe_allow_html=True)

    tabs = st.tabs(["🏛️ TESORERÍA", "🧠 ASISTENTE IA", "🎚️ CONFIGURACIÓN", "💹 MERCADOS", "🛡️ SEGURIDAD", "🛰️ ESTRATEGIA"])

    # --- TAB 1: TESORERÍA (CON ANÁLISIS) ---
    with tabs[0]:
        st.subheader("Estado Financiero del Imperio")
        net_worth = cash + (m2_total * 8500) # Valor promedio
        c1, c2, c3 = st.columns(3)
        c1.metric("PATRIMONIO NETO", f"${net_worth:,.2f}", "+2.4%")
        c2.metric("LIQUIDEZ LIBRE", f"${cash:,.2f}")
        c3.metric("EFICIENCIA FISCAL", "96%", "Optimizado")
        
        st.write("### Proyección de Crecimiento a 10 Años")
        proy = [net_worth * (1.10**i) for i in range(11)]
        st.line_chart(proy, color="#d4af37")

    # --- TAB 2: ASISTENTE IA (INTERACTIVO) ---
    with tabs[1]:
        st.subheader(f"Consultoría Directa para {st.session_state.user_name}")
        for m in st.session_state.chat_log:
            with st.chat_message(m["role"]): st.write(m["content"])
        
        if p := st.chat_input("Diga algo, Señor..."):
            st.session_state.chat_log.append({"role": "user", "content": p})
            with st.chat_message("user"): st.write(p)
            
            respuesta = ia_asistente(p)
            st.session_state.chat_log.append({"role": "assistant", "content": respuesta})
            with st.chat_message("assistant"):
                st.write(respuesta)
                speak(respuesta)

    # --- TAB 3: CONFIGURACIÓN (PERSONALIZACIÓN) ---
    with tabs[2]:
        st.subheader("Ajustes del Sistema Operativo")
        st.write("Personalice cómo el sistema debe interactuar con usted.")
        
        nuevo_nombre = st.text_input("Cambiar Título/Nombre del Director", value=st.session_state.user_name)
        nueva_clave = st.text_input("Actualizar Clave de Acceso", value=st.session_state.key_code, type="password")
        
        if st.button("GUARDAR CAMBIOS EN EL NÚCLEO"):
            st.session_state.user_name = nuevo_nombre
            st.session_state.key_code = nueva_clave
            st.success("Sincronización completa. El sistema ha sido actualizado.")
            speak("Configuración actualizada, Señor.")

    # --- TAB 4: MERCADOS ---
    with tabs[3]:
        st.subheader("Monitor de Activos en Tiempo Real")
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("BITCOIN", "$68,420", "+1.2%")
        m_col2.metric("ORO (OZ)", "$2,450", "+0.5%")
        m_col3.metric("PASE TECH STOCK", "$1,240", "+5.8%")
        st.area_chart(np.random.randn(20, 1), color="#d4af37")

    # --- TAB 5: SEGURIDAD ---
    with tabs[4]:
        st.subheader("Bóveda y Defensa")
        if st.button("GENERAR LLAVE DE ENCRIPTACIÓN"):
            code = hashlib.sha512(str(time.time()).encode()).hexdigest().upper()[:24]
            st.code(code)
            speak("Nueva llave generada. Protocolo de seguridad activo.")
        st.error("RED PROTEGIDA: Cifrado Cuántico Activo.")

    # --- TAB 6: ESTRATEGIA (SATÉLITES) ---
    with tabs[5]:
        st.subheader("Vigilancia Global")
        st.write("Mapa de Intereses Estratégicos")
        # Simulación de puntos calientes
        map_data = pd.DataFrame({
            'lat': [-34.9011, 47.3769, 25.2048, 1.3521],
            'lon': [-56.1645, 8.5417, 55.2708, 103.8198]
        })
        st.map(map_data)

st.divider()
st.caption(f"PASE TECH | DEFINITIVE EDITION v21.0 | OPERADO POR: {st.session_state.user_name.upper()} | {datetime.now().year}")


