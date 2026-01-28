import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN DE MARCA Y ESTILO
st.set_page_config(page_title="Pase Tech Global", layout="wide", page_icon="🧠")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 2px solid #58a6ff; padding: 15px; border-radius: 12px; }
    .stTabs [data-baseweb="tab"] { color: #58a6ff; font-weight: bold; font-size: 16px; }
    .stChatFloatingInputContainer { background-color: #0d1117; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MAESTRA
DB_GLOBAL = {
    "Uruguay": {"Montevideo": 2800, "Punta del Este": 3500, "Costo_Vida": 1200, "Visa": "Mercosur", "Impuesto": 0.09},
    "EEUU": {"Miami": 6500, "Nueva York": 12000, "Costo_Vida": 3500, "Visa": "H1-B / F1", "Impuesto": 0.05},
    "España": {"Madrid": 4800, "Barcelona": 4200, "Costo_Vida": 1800, "Visa": "Nómada Digital", "Impuesto": 0.10},
    "Japón": {"Tokio": 9500, "Osaka": 6000, "Costo_Vida": 2500, "Visa": "Highly Skilled", "Impuesto": 0.08},
    "Suiza": {"Zúrich": 15000, "Ginebra": 14000, "Costo_Vida": 4500, "Visa": "Permiso B", "Impuesto": 0.05}
}

# 3. LÓGICA DE INTELIGENCIA ARTIFICIAL (PASE AI)
def procesar_ia(query):
    query = query.lower()
    if "inmueble" in query or "invertir" in query:
        return "Pase AI: Actualmente, Madrid y Montevideo ofrecen la mejor relación costo-beneficio para inversores de Pase Tech."
    elif "viajar" in query or "vivir" in query:
        return "Pase AI: Basado en tu perfil, el Global Planner puede calcular si tu presupuesto es apto para el destino seleccionado."
    elif "seguridad" in query or "traje" in query:
        return "Pase AI: Los sistemas tácticos están operativos. Puedes enviar comandos desde la pestaña CYBER & HARDWARE."
    else:
        return "Análisis Pase AI: Procesando datos... ¿Podrías ser más específico con tu requerimiento estratégico?"

# 4. SISTEMA DE NAVEGACIÓN
if 'intro' not in st.session_state: st.session_state.intro = True
if 'messages' not in st.session_state: st.session_state.messages = []

if st.session_state.intro:
    st.title("🌐 PASE TECH: GLOBAL SOLUTIONS")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Quiénes Somos")
        st.write("""
        Somos una central de inteligencia dedicada a la optimización de recursos globales. 
        Desde inversiones inmobiliarias internacionales hasta soporte táctico con IA.
        
        **Nuestra Misión:** Proveer herramientas útiles que garanticen rentabilidad y seguridad.
        """)
        if st.button("ACCEDER AL SISTEMA"):
            st.session_state.intro = False
            st.rerun()
    with col2:
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=500")

else:
    tabs = st.tabs(["🧠 PASE AI", "🌍 GLOBAL PLANNER", "🏢 INMUEBLES", "🛡️ CYBER & HARDWARE", "🧬 BIO/AERO"])

    # --- TAB: PASE AI ---
    with tabs[0]:
        st.header("Núcleo de Inteligencia Artificial")
        for m in st.session_state.messages:
            with st.chat_message(m["role"]): st.markdown(m["content"])
        
        if p := st.chat_input("Consulta al sistema..."):
            st.session_state.messages.append({"role": "user", "content": p})
            with st.chat_message("user"): st.markdown(p)
            r = procesar_ia(p)
            st.session_state.messages.append({"role": "assistant", "content": r})
            with st.chat_message("assistant"): st.markdown(r)

    # --- TAB: GLOBAL PLANNER ---
    with tabs[1]:
        st.header("💎 VIP Global Planner")
        c1, c2 = st.columns(2)
        with c1:
            dest = st.selectbox("Destino", list(DB_GLOBAL.keys()))
            prof = st.selectbox("Profesión", ["Estudiante", "Programador", "Médico", "Inversionista"])
            presupuesto = st.number_input("Presupuesto Mensual (USD)", value=2000)
        with c2:
            costo = DB_GLOBAL[dest]["Costo_Vida"]
            st.write(f"### Análisis para {dest}")
            st.write(f"- Visa sugerida: {DB_GLOBAL[dest]['Visa']}")
            if presupuesto >= costo: st.success(f"✅ Viable. Sobrante: USD {presupuesto-costo}")
            else: st.error(f"⚠️ Insuficiente. Faltan: USD {costo-presupuesto}")

    # --- TAB: INMUEBLES ---
    with tabs[2]:
        st.header("Inversión Inmobiliaria")
        pais = st.selectbox("País", list(DB_GLOBAL.keys()), key="p_inv")
        ciudad = st.selectbox("Ciudad", [k for k in DB_GLOBAL[pais].keys() if k not in ["Costo_Vida", "Visa", "Impuesto"]])
        metros = st.slider("Metros Cuadrados", 20, 200, 60)
        
        base = DB_GLOBAL[pais][ciudad] * metros
        gastos = base * DB_GLOBAL[pais]["Impuesto"]
        st.metric("Inversión Total", f"USD {base + gastos:,.0f}")
        st.write(f"Gastos de cierre en {pais}: USD {gastos:,.0f}")

    # --- TAB: CYBER & HARDWARE ---
    with tabs[3]:
        st.header("🛡️ Tactical Command")
        if st.button("🔔 ENVIAR ALERTA AL DISPOSITIVO"):
            st.toast("Notificación enviada al traje/gadget", icon="⚡")
            st.info("Comando sincronizado con hardware Pase Tech.")
        st.progress(random.randint(70, 99), text="Integridad de la Red")

    # --- TAB: BIO/AERO ---
    with tabs[4]:
        st.header("Bio-Metrics & Aerospace")
        st.line_chart([random.randint(60, 100) for _ in range(10)])
        st.write("Sincronización satelital: **Activa**")

st.divider()
st.caption(f"Pase Tech Global v8.0 | {datetime.now().year} | Montevideo, Uruguay")
