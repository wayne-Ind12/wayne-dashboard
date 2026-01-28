import streamlit as st
import pandas as pd
import random
import time
import hashlib
from datetime import datetime

# 1. ARQUITECTURA VISUAL (ESTILO CORPORATIVO/TECH)
st.set_page_config(page_title="PASE TECH | GLOBAL OPS", layout="wide", page_icon="⚡")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;500&display=swap');
    .stApp { background-color: #05080a; color: #d1d5db; font-family: 'JetBrains Mono', monospace; }
    .stMetric { border-left: 3px solid #58a6ff; background-color: #0d1117; padding: 20px; border-radius: 4px; }
    .stButton>button { width: 100%; border-radius: 2px; background-color: #1f2937; color: #58a6ff; border: 1px solid #30363d; transition: 0.3s; }
    .stButton>button:hover { background-color: #58a6ff; color: #000; border: 1px solid #58a6ff; }
    .stTabs [data-baseweb="tab"] { color: #8b949e; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #58a6ff; }
    .stChatMessage { border-bottom: 1px solid #30363d; background: transparent; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA CORE (INTELIGENCIA DE MERCADO)
DB_GLOBAL = {
    "Uruguay": {"m2": 2850, "Costo": 1250, "Tax": 9, "Risk": "Low", "Visa": "Mercosur"},
    "Suiza": {"m2": 15800, "Costo": 4900, "Tax": 5, "Risk": "Minimal", "Visa": "Permiso B"},
    "EAU": {"m2": 7900, "Costo": 3100, "Tax": 0, "Risk": "Medium", "Visa": "Golden"},
    "USA": {"m2": 8500, "Costo": 3800, "Tax": 5, "Risk": "Low", "Visa": "H1-B / EB-5"},
    "Singapur": {"m2": 18000, "Costo": 4200, "Tax": 2, "Risk": "Minimal", "Visa": "Employment Pass"}
}

STOCKS = {
    "PASE TECH (PT)": 450.25, "GOLD (XAU)": 2420.10, "BITCOIN (BTC)": 65400.00, "APPLE (AAPL)": 192.45
}

# 3. FUNCIONES DE ELITE (IA Y SEGURIDAD)
def ia_logic(query):
    q = query.lower()
    if "mejor" in q and ("inversión" in q or "lugar" in q):
        best = min(DB_GLOBAL, key=lambda x: DB_GLOBAL[x]['Tax'])
        return f"📍 **Análisis Pase AI:** El destino óptimo para eficiencia fiscal es **{best}** (0% Impuestos). Para refugio de capital, **Suiza** mantiene el grado de inversión AAA."
    elif "mercado" in q or "precio" in q:
        return f"📈 **Análisis Pase AI:** El Oro está en máximos históricos. Bitcoin muestra consolidación. Se recomienda diversificar un 20% en activos PT."
    elif "seguridad" in q:
        return "🛡️ **Protocolo:** Implementando rotación de llaves asimétricas. La red está bajo monitoreo constante."
    return "💡 **Sugerencia:** Prueba preguntarme sobre 'mejor inversión' o solicita un 'reporte financiero'."

def get_tactical_report():
    report = f"PASE TECH - TACTICAL REPORT\n{'='*30}\n"
    report += f"FECHA: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    report += f"ESTADO DE ACTIVOS:\n"
    for k, v in STOCKS.items():
        report += f"- {k}: ${v:,.2f}\n"
    report += f"\nRECOMENDACIÓN: Acumular Activos en Zonas Low-Tax.\n{'='*30}"
    return report

# 4. SISTEMA DE AUTENTICACIÓN
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.title("⚡ PASE TECH | SECURE LOGIN")
    with st.container():
        col_l1, col_l2, col_l3 = st.columns([1,2,1])
        with col_l2:
            key = st.text_input("ENTER ACCESS KEY", type="password")
            if st.button("VERIFY IDENTITY"):
                if key == "vale": # CLAVE DE COMANDO
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("INVALID KEY.")
else:
    # --- DASHBOARD PRINCIPAL ---
    st.sidebar.title("PASE TECH OPS")
    st.sidebar.write(f"USER: **BRUNO**")
    st.sidebar.write(f"SYSTEM: **ACTIVE**")
    if st.sidebar.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    tabs = st.tabs(["🧠 CORE AI", "💹 MARKET HUB", "🔒 VAULT", "🏢 REAL ESTATE", "🛰️ TACTICAL"])

    # --- TAB 1: CORE AI ---
    with tabs[0]:
        st.subheader("Neural Network Interface")
        if 'chat' not in st.session_state: st.session_state.chat = []
        for m in st.session_state.chat:
            with st.chat_message(m["role"]): st.write(m["content"])
        
        if p := st.chat_input("Enter strategic command..."):
            st.session_state.chat.append({"role": "user", "content": p})
            with st.chat_message("user"): st.write(p)
            ans = ia_logic(p)
            st.session_state.chat.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"): st.write(ans)

    # --- TAB 2: MARKET HUB (EXCLUSIVO) ---
    with tabs[1]:
        st.subheader("Live Asset Monitoring")
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        for i, (asset, price) in enumerate(STOCKS.items()):
            change = random.uniform(-2, 2)
            cols = [m_col1, m_col2, m_col3, m_col4]
            cols[i].metric(asset, f"${price:,.2f}", f"{change:.2f}%")
        
        st.write("### Market Performance (Last 24h)")
        st.area_chart([random.randint(100, 200) for _ in range(20)])

    # --- TAB 3: THE VAULT ---
    with tabs[2]:
        st.subheader("Cybersecurity & Encryption")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.write("Generador de Llaves de Acceso")
            if st.button("GENERATE RSA KEY"):
                key_gen = "".join(random.choices("ABCDEF0123456789", k=32))
                st.code(key_gen, language='text')
                st.toast("New key generated.")
        with v_col2:
            st.write("Digital Identity Hash")
            raw_data = st.text_input("Input Data to Hash")
            if raw_data:
                st.code(hashlib.sha256(raw_data.encode()).hexdigest())

    # --- TAB 4: REAL ESTATE PRO ---
    with tabs[3]:
        st.subheader("Global Portfolio Management")
        p_sel = st.selectbox("Market Selection", list(DB_GLOBAL.keys()))
        m2 = st.number_input("Target Area (m²)", 50, 10000, 150)
        
        # Cálculo de ROI Simplificado
        data = DB_GLOBAL[p_sel]
        costo_total = (data['m2'] * m2) * (1 + data['Tax']/100)
        
        st.metric("Total Investment Value", f"USD {costo_total:,.0f}")
        
        st.write(f"**Risk Level:** {data['Risk']} | **Visa Path:** {data['Visa']}")
        
        # ROI Formula: $ROI = \frac{Ingresos - Costos}{Costos} \times 100$
        st.write("Fórmula de Rentabilidad Aplicada:")
        st.latex(r"ROI = \frac{Net\_Revenue}{Total\_Investment} \times 100")

    # --- TAB 5: TACTICAL & REPORTS ---
    with tabs[4]:
        st.subheader("Operational Intelligence")
        st.write("Generación de Reportes de Inteligencia para Socios.")
        
        report_content = get_tactical_report()
        st.download_button(
            label="📄 EXPORT TACTICAL REPORT (TXT)",
            data=report_content,
            file_name=f"PASE_TECH_REPORT_{datetime.now().strftime('%Y%H%M')}.txt",
            mime="text/plain"
        )
        
        st.write("---")
        st.write("Satellite Link Status")
        st.progress(92, text="Signal Strength (Encrypted)")
        st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&q=80&w=800")

st.divider()
st.caption(f"PASE TECH GLOBAL SOLUTIONS | V13.0 | 2026 | BUILT FOR THE FUTURE.")
