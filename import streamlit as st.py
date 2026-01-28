import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN Y ESTILO RESPONSIVE
st.set_page_config(page_title="Pase Tech Global", layout="wide", page_icon="⚡")

# CSS para que se vea como App y tenga mejores fuentes
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #58a6ff; }
    .stTabs [data-baseweb="tab"] { padding: 10px; }
    /* Estilo de burbujas de chat personalizadas */
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MAESTRA EXPANDIDA (VIP)
DB_GLOBAL = {
    "Uruguay": {"Montevideo": 2800, "Costo_Vida": 1200, "Visa": "Mercosur", "Impuesto": 0.09},
    "EEUU": {"Miami": 6500, "Nueva York": 12000, "Costo_Vida": 3500, "Visa": "H1-B", "Impuesto": 0.05},
    "España": {"Madrid": 4800, "Barcelona": 4200, "Costo_Vida": 1800, "Visa": "Nómada Digital", "Impuesto": 0.10},
    "Reino Unido": {"Londres": 11000, "Manchester": 5500, "Costo_Vida": 3200, "Visa": "Skilled Worker", "Impuesto": 0.12},
    "EAU": {"Dubái": 7500, "Abu Dabi": 6800, "Costo_Vida": 2800, "Visa": "Golden Visa", "Impuesto": 0.00},
    "Australia": {"Sídney": 8500, "Melbourne": 7200, "Costo_Vida": 3000, "Visa": "Skilled Nominated", "Impuesto": 0.06},
    "Corea del Sur": {"Seúl": 9000, "Busan": 4500, "Costo_Vida": 2100, "Visa": "E-7 (Especializada)", "Impuesto": 0.07}
}

# 3. ENTRENAMIENTO DE LA IA (Personalidad Avanzada)
def respuesta_ia_avanzada(query):
    q = query.lower()
    
    # Saludos
    if any(palabra in q for palabra in ["hola", "buen día", "hey", "inicio"]):
        return ("¡Hola! Soy el núcleo de inteligencia de Pase Tech. 🛡️\n\n"
                "Estoy listo para asesorarte en inversiones inmobiliarias, "
                "relocalización global o protocolos de ciberseguridad. ¿Por dónde te gustaría empezar hoy?")
    
    # Consejos de Inversión
    elif "invertir" in q or "rentabilidad" in q:
        return ("Análisis Estratégico: Actualmente Dubái es un paraíso fiscal (0% impuestos), "
                "mientras que Montevideo ofrece estabilidad única en Latam. Si buscas ROI alto, "
                "mira el sector tecnológico en Londres o Seúl.")
    
    # Seguridad
    elif "seguridad" in q or "proteger" in q or "hack" in q:
        return ("Protocolo de Blindaje: La primera línea de defensa es la 'Zero Trust'. "
                "No confíes en ninguna IP externa. Te recomiendo auditar tus contraseñas y "
                "activar llaves físicas de seguridad (U2F).")
    
    # Respuesta por defecto más humana
    else:
        return ("Entiendo. Mis algoritmos están procesando tu solicitud sobre '" + query + "'.\n\n"
                "Para darte una respuesta de nivel VIP, ¿podrías decirme si te interesa más el área de "
                "costos, seguridad táctica o planificación de carrera?")

# 4. INTERFAZ PRINCIPAL
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("⚡ PASE TECH GLOBAL")

# Tabs para organización responsive
tabs = st.tabs(["🧠 PASE AI", "🌍 GLOBAL PLANNER", "🏢 INMUEBLES", "🛡️ TACTICAL"])

# --- TAB 1: IA MEJORADA ---
with tabs[0]:
    st.subheader("Centro de Inteligencia")
    
    # Contenedor de chat
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if p := st.chat_input("Escribe tu consulta estratégica..."):
        st.session_state.messages.append({"role": "user", "content": p})
        with st.chat_message("user"): st.markdown(p)
        
        # Respuesta con delay simulado para que parezca que piensa
        with st.spinner("Analizando datos globales..."):
            r = respuesta_ia_avanzada(p)
            st.session_state.messages.append({"role": "assistant", "content": r})
            with st.chat_message("assistant"): st.markdown(r)

# --- TAB 2: GLOBAL PLANNER (CIUDADES VIP) ---
with tabs[1]:
    st.subheader("💎 Planificador de Relocalización VIP")
    c1, c2 = st.columns([1, 1])
    with c1:
        dest = st.selectbox("Seleccione Destino Internacional", list(DB_GLOBAL.keys()))
        prof = st.selectbox("Perfil de Usuario", ["Estudiante", "Programador IT", "Inversor Senior", "Médico"])
    with c2:
        costo = DB_GLOBAL[dest]["Costo_Vida"]
        visa = DB_GLOBAL[dest]["Visa"]
        st.metric(f"Costo de Vida ({dest})", f"USD {costo:,.0f}/mes")
        st.info(f"🛂 Requisito Legal: {visa}")

# --- TAB 3: INMUEBLES ---
with tabs[2]:
    st.subheader("Inversión de Capital")
    # Usamos columnas para que en móvil se apilen
    col_inv = st.columns(2)
    with col_inv[0]:
        p_inv = st.selectbox("País de interés", list(DB_GLOBAL.keys()), key="inv")
        ciudad_inv = st.selectbox("Ciudad", [k for k in DB_GLOBAL[p_inv].keys() if k not in ["Costo_Vida", "Visa", "Impuesto"]])
    with col_inv[1]:
        m2 = st.slider("Tamaño de Propiedad (m²)", 30, 300, 70)
        precio_f = DB_GLOBAL[p_inv][ciudad_inv] * m2
        st.metric("Inversión Estimada", f"USD {precio_f + (precio_f * DB_GLOBAL[p_inv]['Impuesto']):,.0f}")

# --- TAB 4: TACTICAL ---
with tabs[3]:
    st.subheader("Control Táctico")
    if st.button("🔔 TEST: NOTIFICACIÓN PUSH"):
        st.toast("Enlace con el dispositivo móvil verificado.", icon="⚡")
    st.write("Sistemas operativos al 100%. Red de satélites Pase Tech en órbita.")

st.divider()
st.caption(f"Pase Tech Suite v9.0 | Inteligencia Estratégica | {datetime.now().strftime('%d/%m/%Y')}")
