import streamlit as st
import pandas as pd
import random
import time
import hashlib
from datetime import datetime

# 1. ARQUITECTURA VISUAL ELITE
st.set_page_config(page_title="PASE TECH | EMPIRE OS", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    .stApp { background-color: #010203; color: #a0aec0; }
    .stMetric { background: linear-gradient(135deg, #0d1117 0%, #05080a 100%); border: 1px solid #1e293b; padding: 20px; border-radius: 10px; }
    [data-testid="stMetricValue"] { color: #60a5fa; font-family: 'JetBrains Mono', monospace; }
    .stTabs [data-baseweb="tab"] { font-weight: 700; color: #64748b; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #60a5fa; border-bottom-color: #60a5fa; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA MASTER (Sincronizada)
DB_GLOBAL = {
    "Suiza": {"m2": 15800, "Tax": 5, "Costo": 4900},
    "EAU": {"m2": 7900, "Tax": 0, "Costo": 3100},
    "Uruguay": {"m2": 2850, "Tax": 9, "Costo": 1250},
    "Singapur": {"m2": 18500, "Tax": 2, "Costo": 4200}
}

MARKET_DATA = {
    "BTC": 66200.0, "GOLD": 2350.0, "MSFT": 420.0, "SONY": 94.0
}

# 3. NÚCLEO FINANCIERO (Fórmulas)
def calcular_patrimonio(activos, propiedades_m2, pais_inmueble):
    # Valor mercado activos
    val_mercado = sum(activos.values())
    # Valor propiedades: (m2 * precio_zona)
    val_inmuebles = propiedades_m2 * DB_GLOBAL[pais_inmueble]["m2"]
    return val_mercado + val_inmuebles

# 4. SISTEMA DE CONTROL
if 'auth_empire' not in st.session_state: st.session_state.auth_empire = False

if not st.session_state.auth_empire:
    st.title("🛡️ PASE TECH | ENCRYPTED GATEWAY")
    with st.container():
        col_c, col_pass, col_r = st.columns([1,2,1])
        with col_pass:
            access_code = st.text_input("IDENTIFICATION REQUIRED", type="password")
            if st.button("EXECUTE AUTHENTICATION"):
                if access_code == "vale":
                    st.session_state.auth_empire = True
                    st.success("Welcome, Director.")
                    st.rerun()
                else: st.error("ACCESS DENIED: LOGGING ATTEMPT.")
else:
    # --- DASHBOARD CORPORATIVO ---
    st.title("💎 PASE TECH: GLOBAL EMPIRE")
    
    tabs = st.tabs(["🏛️ TREASURY", "🧠 CFO AI", "📈 MARKETS", "🏢 REAL ESTATE", "📦 LOGISTICS", "⚖️ LEGAL", "🛡️ VAULT"])

    # --- TAB 1: TREASURY (LA BILLETERA VIRTUAL) ---
    with tabs[0]:
        st.header("Executive Financial Summary")
        
        # Simulación de posesiones
        m2_prop = st.sidebar.number_input("Tus Propiedades (m² totales)", 0, 10000, 250)
        pais_p = st.sidebar.selectbox("Ubicación de Sede", list(DB_GLOBAL.keys()))
        
        total_net = calcular_patrimonio(MARKET_DATA, m2_prop, pais_p)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("ESTIMATED NET WORTH", f"USD {total_net:,.2f}")
        c2.metric("LIQUID ASSETS", f"USD {sum(MARKET_DATA.values()):,.2f}")
        c3.metric("TAX EFFICIENCY", f"{100 - DB_GLOBAL[pais_p]['Tax']}%", "Stable")
        
        st.write("### Composición del Imperio")
        st.progress(min(int((sum(MARKET_DATA.values()) / total_net) * 100), 100), text="Liquidez vs Activos Fijos")
        
        # Fórmula Matemática en LaTeX
        st.latex(r"Total\_Wealth = \sum_{i=1}^{n} (Asset_i \times Price_i) + (Area \times Price_{m2})")

    # --- TAB 2: CFO AI (INTELIGENCIA FINANCIERA) ---
    with tabs[1]:
        st.header("Chief Financial Officer AI")
        if 'chat_emp' not in st.session_state: st.session_state.chat_emp = []
        for m in st.session_state.chat_emp:
            with st.chat_message(m["role"]): st.write(m["content"])
        
        if p := st.chat_input("Consulta financiera o estratégica..."):
            st.session_state.chat_emp.append({"role": "user", "content": p})
            with st.chat_message("user"): st.write(p)
            
            # Lógica de respuesta mejorada
            if "patrimonio" in p.lower() or "cuanto tengo" in p.lower():
                r = f"Señor, su patrimonio actual es de USD {total_net:,.2f}. El 60% está concentrado en bienes raíces en {pais_p}."
            elif "riesgo" in p.lower():
                r = "Análisis: El riesgo es moderado. Sugiero mover un 10% de liquidez a ORO para cobertura ante inflación."
            else:
                r = "Procesando... Sugiero revisar la pestaña de MARKETS para optimizar sus entradas en activos tecnológicos."
                
            st.session_state.chat_emp.append({"role": "assistant", "content": r})
            with st.chat_message("assistant"): st.write(r)

    # --- TAB 3: MARKETS ---
    with tabs[2]:
        st.header("Real-Time Market Tracking")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("BTC/USD", f"${MARKET_DATA['BTC']:,}", "+2.4%")
        m2.metric("GOLD/OZ", f"${MARKET_DATA['GOLD']:,}", "-0.5%")
        m3.metric("MSFT (Microsoft)", f"${MARKET_DATA['MSFT']}", "+1.2%")
        m4.metric("SONY (Sony Corp)", f"${MARKET_DATA['SONY']}", "-0.8%")
        st.line_chart([random.randint(400, 500) for _ in range(20)])

    # --- TAB 4: REAL ESTATE ---
    with tabs[3]:
        st.header("Property & HQ Portfolio")
        st.table(pd.DataFrame(DB_GLOBAL).T)

    # --- TAB 5: LOGISTICS ---
    with tabs[4]:
        st.header("Global Supply Chain")
        st.info("Cargamento de 'Hardware Cuántico' llegando a Puerto de Montevideo en 48hs.")
        st.progress(85, text="Transito: 85%")

    # --- TAB 6: LEGAL ---
    with tabs[5]:
        st.header("Legal Compliance & Contracts")
        if st.button("GENERAR NDA CORPORATIVO"):
            st.code("NON-DISCLOSURE AGREEMENT (NDA)\nBETWEEN: PASE TECH CORP & [CONFIDENTIAL]\nTERMS: CLASS A ENFORCEMENT", language="text")

    # --- TAB 7: VAULT ---
    with tabs[6]:
        st.header("Ultra-Secure Vault")
        st.write("Generador de claves para acceso a servidores centrales.")
        if st.button("GENERATE MILITARY GRADE KEY"):
            key = hashlib.sha256(str(time.time()).encode()).hexdigest().upper()[:24]
            st.code(key, language="text")

st.divider()
st.caption(f"PASE TECH GLOBAL EMPIRE | Versión 15.0 | {datetime.now().year} | Designed for the Elite.")

