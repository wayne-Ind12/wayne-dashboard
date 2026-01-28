import streamlit as st
import pandas as pd
import numpy as np
import time
import hashlib
import random
from datetime import datetime
import streamlit.components.v1 as components

# ==========================================
# 1. CORE ARCHITECTURE & NEURAL UI
# ==========================================
st.set_page_config(page_title="PASE TECH | GENESIS", layout="wide", page_icon="🔱", initial_sidebar_state="expanded")

# Estilo Industrial de Élite (Gold & Obsidian)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700&family=JetBrains+Mono&display=swap');
    .stApp { background-color: #050505; color: #e2e8f0; font-family: 'Montserrat', sans-serif; }
    .main-header { font-size: 3rem; font-weight: 700; color: #d4af37; letter-spacing: -1px; text-shadow: 0 0 20px rgba(212,175,55,0.3); }
    div[data-testid="stMetric"] { background: #0a0a0a; border-left: 5px solid #d4af37; border-radius: 0px; padding: 25px; }
    .stButton>button { background: #d4af37; color: black; border: none; font-weight: 900; text-transform: uppercase; border-radius: 0px; width: 100%; height: 50px; transition: 0.5s; }
    .stButton>button:hover { background: #ffffff; box-shadow: 0 0 30px #d4af37; }
    .stTabs [data-baseweb="tab"] { font-size: 11px; letter-spacing: 2px; color: #666; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #d4af37; border-bottom: 2px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# Motor de Voz de Mando (JS Bridge)
def voice_oracle(text):
    if text:
        js = f"<script>var m = new SpeechSynthesisUtterance('{text}'); m.lang='es-ES'; m.rate=0.9; window.speechSynthesis.speak(m);</script>"
        components.html(js, height=0)

# ==========================================
# 2. MASTER DATABASE (THE WORLD BANK)
# ==========================================
DB = {
    "Suiza": {"m2": 16200, "Tax": 5, "Safety": 99, "Power": 92, "Visa": "Elite Permisson"},
    "EAU": {"m2": 8100, "Tax": 0, "Safety": 95, "Power": 95, "Visa": "Golden Residency"},
    "USA": {"m2": 9500, "Tax": 8, "Safety": 85, "Power": 100, "Visa": "EB-1 Extraordinary"},
    "Singapur": {"m2": 19000, "Tax": 2, "Safety": 100, "Power": 90, "Visa": "VCC Fund Entry"},
    "Uruguay": {"m2": 2900, "Tax": 7, "Safety": 88, "Power": 70, "Visa": "Tax Holiday 10y"}
}

MARKETS = {"BTC": 68400, "GOLD": 2450, "PT_CORP": 1250, "S&P500": 5200}

# ==========================================
# 3. NÚCLEO DE INTELIGENCIA ESTRATÉGICA
# ==========================================
def oracle_intelligence(query, net_worth):
    q = query.lower()
    if any(x in q for x in ["negocio", "trato", "deal", "ganar"]):
        return f"Estrategia de Victoria: Con un capital de ${net_worth:,.0f}, el movimiento óptimo es una adquisición agresiva en bienes raíces en Dubái. El apalancamiento es tu mejor arma. Haz el trato ahora."
    elif "seguridad" in q:
        return "Alerta: Se detectan vulnerabilidades en nodos secundarios. He activado el cifrado de grado militar. Estás protegido."
    elif "futuro" in q:
        return f"Proyección: En 5 años, si mantenemos el ROI del 12%, su patrimonio superará los ${net_worth*1.8:,.0f}. Dominio absoluto."
    return "Sistemas listos. ¿Cuál es el siguiente objetivo de conquista, Señor?"

# ==========================================
# 4. GESTIÓN DE ACCESO (SECURITY GATE)
# ==========================================
if 'access' not in st.session_state: st.session_state.access = False

if not st.session_state.access:
    st.markdown("<h1 class='main-header'>PASE TECH | THE GENESIS</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.write("### LOGIN TO COMMAND CENTER")
        key = st.text_input("SISTEMA DE IDENTIDAD (PASSWORD)", type="password")
        if st.button("AUTENTICAR"):
            if key == "bruno":
                st.session_state.access = True
                voice_oracle("Acceso verificado. Bienvenido al centro de mando, Señor.")
                st.rerun()
            else: st.error("ACCESO DENEGADO. AUTORIDADES NOTIFICADAS.")
else:
    # --- DASHBOARD PRINCIPAL ---
    st.sidebar.markdown("<h2 style='color:#d4af37'>SYSTEM STATUS</h2>", unsafe_allow_html=True)
    liquid_cash = st.sidebar.number_input("LIQUIDEZ (USD)", value=25000000, step=1000000)
    owned_m2 = st.sidebar.number_input("PROPIEDADES (m2)", value=1200)
    hq_loc = st.sidebar.selectbox("SEDE CENTRAL", list(DB.keys()))
    
    # Cálculo de Poder
    net_worth = liquid_cash + (owned_m2 * DB[hq_loc]["m2"])

    tabs = st.tabs(["🏛️ TREASURY", "🧠 ORACLE AI", "🤝 DEAL MAKER", "📊 MARKETS", "🛡️ SECURITY", "🛰️ AEROSPACE", "🧬 BIOTECH"])

    # --- TAB 1: TREASURY (EL IMPERIO) ---
    with tabs[0]:
        st.markdown("<h2 class='main-header'>GLOBAL TREASURY</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("NET WORTH ESTIMATED", f"${net_worth:,.2f}", "+15%")
        col2.metric("TAX SAVINGS (EST)", f"USD {net_worth * (DB[hq_loc]['Tax']/100):,.0f}")
        col3.metric("POWER INDEX", f"{DB[hq_loc]['Power']}/100")
        
        st.divider()
        st.subheader("Crecimiento Exponencial (Simulación de 10 Años)")
        projection = [net_worth * (1.12**i) for i in range(11)]
        st.area_chart(projection)
        st.latex(r"Empire\_Growth = \int_{0}^{t} Capital \cdot e^{r \cdot dt}")

    # --- TAB 2: ORACLE AI (VOZ DE MANDO) ---
    with tabs[1]:
        st.subheader("Neural Network Interface")
        if 'chat' not in st.session_state: st.session_state.chat = []
        for m in st.session_state.chat:
            with st.chat_message(m["role"]): st.write(m["content"])
        
        if p := st.chat_input("Hable con su imperio..."):
            st.session_state.chat.append({"role": "user", "content": p})
            with st.chat_message("user"): st.write(p)
            ans = oracle_intelligence(p, net_worth)
            st.session_state.chat.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.write(ans)
                voice_oracle(ans)

    # --- TAB 3: DEAL MAKER (EL ARTE DEL TRATO) ---
    with tabs[2]:
        st.subheader("High-Stakes Negotiation Module")
        deal_c1, deal_c2 = st.columns(2)
        with deal_c1:
            target = st.text_input("Nombre de la Adquisición (Ej: Sony, Microsoft)")
            amount = st.number_input("Valor de la Oferta (M)", value=100.0)
            if st.button("LANZAR OFERTA"):
                voice_oracle(f"Iniciando negociación con {target} por {amount} millones. Dominaremos el mercado.")
                st.success(f"Oferta enviada a la junta directiva de {target}.")
        with deal_c2:
            st.write("### Factores de Éxito")
            st.progress(85, text="Apalancamiento")
            st.progress(92, text="Influencia Política")

    # --- TAB 4: MARKETS ---
    with tabs[3]:
        st.subheader("Live Market Domination")
        m_cols = st.columns(4)
        for i, (k, v) in enumerate(MARKETS.items()):
            m_cols[i].metric(k, f"${v:,}", f"{random.uniform(-2, 5):.1f}%")
        st.line_chart(np.random.randn(20, 4))

    # --- TAB 5: SECURITY (BUNKER) ---
    with tabs[4]:
        st.subheader("Quantum Security & Vault")
        if st.button("GENERAR CÓDIGO DE ACCESO SATELITAL"):
            code = hashlib.sha512(str(time.time()).encode()).hexdigest().upper()[:32]
            st.code(code)
            voice_oracle("Nuevo código generado. Seguridad máxima activada.")
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800")

    # --- TAB 6: AEROSPACE ---
    with tabs[5]:
        st.subheader("Satellite Reconnaissance")
        st.write("Sincronizando con la red de satélites de Pase Tech...")
        st.map(pd.DataFrame({'lat': [34.0522, 47.3769, 25.2048], 'lon': [-118.2437, 8.5417, 55.2708]}))

    # --- TAB 7: BIOTECH ---
    with tabs[6]:
        st.subheader("Human Optimization Lab")
        st.metric("Capacidad Mental", "98%", "Optimal")
        st.metric("Stress Level", "12%", "Controlled")
        st.info("Protocolo de Longevidad: Activado. Suplementos optimizados.")

st.divider()
st.caption(f"PASE TECH GLOBAL | GENESIS & APOCALYPSE v20.0 | {datetime.now().year} | BUILT FOR THE 1%")


