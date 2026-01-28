import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# 1. CONFIGURACIÓN DE PANTALLA Y ESTILO PROFESIONAL
st.set_page_config(page_title="Pase Tech Omni-Intelligence", layout="wide", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #c9d1d9; }
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #58a6ff; font-family: 'Courier New'; }
    .stTabs [data-baseweb="tab"] { padding: 10px; font-weight: bold; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; border: 1px solid #1f2937; background-color: #0d1117; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MAESTRA (EL "SABER" DE LA IA)
DB_GLOBAL = {
    "Uruguay": {"Ciudad": "Montevideo", "m2": 2800, "Costo_Vida": 1200, "Visa": "Residencia Mercosur", "Impuesto": 9},
    "EEUU": {"Ciudad": "Miami", "m2": 8000, "Costo_Vida": 3500, "Visa": "Visa H1-B / O-1", "Impuesto": 5},
    "España": {"Ciudad": "Madrid", "m2": 4800, "Costo_Vida": 1800, "Visa": "Nómada Digital", "Impuesto": 10},
    "Reino Unido": {"Ciudad": "Londres", "m2": 11000, "Costo_Vida": 3200, "Visa": "Skilled Worker", "Impuesto": 12},
    "EAU": {"Ciudad": "Dubái", "m2": 7500, "Costo_Vida": 2800, "Visa": "Golden Visa", "Impuesto": 0},
    "Australia": {"Ciudad": "Sídney", "m2": 8500, "Costo_Vida": 3000, "Visa": "Skilled Nominated", "Impuesto": 6},
    "Corea del Sur": {"Ciudad": "Seúl", "m2": 9000, "Costo_Vida": 2100, "Visa": "Visa E-7", "Impuesto": 7},
    "Suiza": {"Ciudad": "Zúrich", "m2": 15000, "Costo_Vida": 4500, "Visa": "Permiso B/L", "Impuesto": 5}
}

# 3. MOTOR DE IA AVANZADO (LÓGICA DE RAZONAMIENTO)
def procesar_ia_pro(query):
    q = query.lower()
    
    # Razonamiento sobre Inversión (Compara toda la DB)
    if any(p in q for p in ["mejor", "invertir", "donde", "inversión", "comprar"]):
        pais_barato = min(DB_GLOBAL, key=lambda x: DB_GLOBAL[x]['m2'])
        pais_sin_imp = "EAU (Dubái)"
        return (f"🧠 **Análisis de Mercado Pase AI:**\n\n"
                f"Si buscas el m² más accesible, **{pais_barato}** es el líder actual. "
                f"Sin embargo, para maximizar rentabilidad neta, **{pais_sin_imp}** es imbatible por su 0% de impuestos.\n\n"
                f"¿Quieres que comparemos el retorno de inversión (ROI) entre dos destinos específicos?")

    # Razonamiento sobre Vida/Trabajo/Estudio
    elif any(p in q for p in ["vivir", "viajar", "trabajar", "estudiar", "emigrar"]):
        mejor_vida = "España" if "estudiar" in q or "vivir" in q else "EEUU"
        return (f"🌍 **Consultoría de Relocalización:**\n\n"
                f"Para un perfil técnico, **{mejor_vida}** ofrece los mejores ecosistemas. "
                f"Si eres estudiante, recomiendo **España** por la facilidad de visa. "
                f"En la pestaña 'GLOBAL PLANNER' he cargado los costos de vida exactos para que compares.")

    # Razonamiento sobre Seguridad/Hack/Traje
    elif any(p in q for p in ["seguridad", "hacker", "proteger", "traje", "gadget"]):
        return (f"🛡️ **Protocolo Táctico Pase Tech:**\n\n"
                "He verificado los sistemas. Recomiendo implementar 'Cifrado Cuántico' y auditar los nodos de red. "
                "Si estás diseñando tu traje táctico, el módulo de 'Control Táctico' tiene el botón de alerta activo.")

    # Saludos y Personalidad Humana
    elif any(p in q for p in ["hola", "quien sos", "ayuda", "buen"]):
        return ("¡Hola! Soy el núcleo de inteligencia **Pase AI**. ⚡\n\n"
                "A diferencia de una IA común, yo tengo acceso directo a la base de datos financiera de Pase Tech. "
                "Puedo decirte dónde invertir, cuánto cuesta vivir en el extranjero o proteger tus sistemas. ¿Qué misión tenemos hoy?")

    else:
        return ("🤔 **Pase AI - Procesamiento:**\n\n"
                f"He analizado tu consulta sobre '{query}'. Mis sensores globales sugieren que esto impacta en tu rentabilidad. "
                "¿Podrías darme más detalles o elegir una de mis especialidades (Inmuebles, Seguridad o Viajes)?")

# 4. INTERFAZ Y NAVEGACIÓN
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("⚡ PASE TECH GLOBAL SOLUTIONS")

tabs = st.tabs(["🧠 PASE AI", "🌍 GLOBAL PLANNER", "🏢 INMUEBLES", "🛡️ TACTICAL", "🧬 BIOTECH", "🛰️ ESPACIO"])

# --- TAB 1: PASE AI ---
with tabs[0]:
    st.subheader("Centro de Inteligencia Pro")
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if p := st.chat_input("Escribe tu consulta al sistema..."):
        st.session_state.messages.append({"role": "user", "content": p})
        with st.chat_message("user"): st.markdown(p)
        
        with st.spinner("IA Pensando..."):
            time.sleep(1) # Simula procesamiento
            r = procesar_ia_pro(p)
            st.session_state.messages.append({"role": "assistant", "content": r})
            with st.chat_message("assistant"): st.markdown(r)

# --- TAB 2: GLOBAL PLANNER ---
with tabs[1]:
    st.subheader("💎 Planificador de Relocalización")
    c1, c2 = st.columns(2)
    with c1:
        pais_dest = st.selectbox("País Destino", list(DB_GLOBAL.keys()))
        profesion = st.selectbox("Ocupación", ["Estudiante", "Programador IT", "Inversor Senior", "Médico"])
    with c2:
        info = DB_GLOBAL[pais_dest]
        st.metric(f"Costo Mensual en {info['Ciudad']}", f"USD {info['Costo_Vida']:,}")
        st.info(f"Requisito de Visa: {info['Visa']}")

# --- TAB 3: INMUEBLES ---
with tabs[2]:
    st.subheader("Inversión Inmobiliaria Global")
    col_i = st.columns(2)
    with col_i[0]:
        p_sel = st.selectbox("País de Inversión", list(DB_GLOBAL.keys()), key="inv_p")
        m2_input = st.slider("Metros Cuadrados", 30, 500, 80)
    with col_i[1]:
        precio_m2 = DB_GLOBAL[p_sel]["m2"]
        subtotal = precio_m2 * m2_input
        impuesto_final = subtotal * (DB_GLOBAL[p_sel]["Impuesto"] / 100)
        st.metric(f"Inversión Total en {p_sel}", f"USD {subtotal + impuesto_final:,.0f}")
        st.write(f"Precio Base: USD {subtotal:,.0f} | Impuestos ({DB_GLOBAL[p_sel]['Impuesto']}%): USD {impuesto_final:,.0f}")

# --- TAB 4: TACTICAL ---
with tabs[3]:
    st.subheader("Centro de Mando Táctico")
    if st.button("🔔 ACTIVAR PROTOCOLO DE ALERTA"):
        st.toast("ALERTA ENVIADA AL DISPOSITIVO VINCULADO", icon="🛡️")
    st.progress(98, text="Integridad del Blindaje")

# --- TAB 5: BIOTECH ---
with tabs[4]:
    st.subheader("🧬 Análisis Bio-Médico")
    bpm = st.slider("Ritmo Cardíaco (Sensores del Traje)", 50, 180, 75)
    if bpm > 130: st.error("⚠️ Estrés elevado detectado.")
    else: st.success("✅ Signos vitales estables.")
    st.line_chart([random.randint(70, 90) for _ in range(20)])

# --- TAB 6: ESPACIO ---
with tabs[5]:
    st.subheader("🛰️ Monitoreo Satelital")
    st.write("Ubicación actual del satélite Pase-SAT: **Órbita sobre Montevideo**")
    st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&q=80&w=600")
    if st.button("📡 DESCARGAR DATOS TELEMÉTRICOS"):
        st.download_button("Descargar Reporte", "Datos de órbita: Estables. Energía: 94%.", "reporte.txt")

st.divider()
st.caption(f"Pase Tech Global v11.0 | {datetime.now().strftime('%d/%m/%Y')} | Sistema Inteligente de Operaciones")

