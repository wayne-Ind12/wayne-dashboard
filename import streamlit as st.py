import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN Y ESTILO PASE TECH
st.set_page_config(page_title="Pase Tech Global", layout="wide", page_icon="🌎")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .stTabs [data-baseweb="tab"] { color: #58a6ff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS GLOBAL (Simulada para Pase Tech)
DB_GLOBAL = {
    "Uruguay": {"Montevideo": 2800, "Punta del Este": 3500, "Gastos": 0.09},
    "Argentina": {"Buenos Aires": 2200, "Córdoba": 1400, "Gastos": 0.07},
    "EEUU": {"Miami": 6500, "Nueva York": 12000, "Madrid": 4500, "Gastos": 0.05},
    "España": {"Madrid": 4800, "Barcelona": 4200, "Gastos": 0.10}
}

# 3. NAVEGACIÓN
if 'intro_done' not in st.session_state:
    st.session_state.intro_done = False

if not st.session_state.intro_done:
    st.title("🌎 PASE TECH GLOBAL SOLUTIONS")
    st.header("Tu Pasaporte a la Inversión y el Futuro")
    if st.button("ENTRAR AL TERMINAL GLOBAL"):
        st.session_state.intro_done = True
else:
    tabs = st.tabs(["🏗️ INMUEBLES GLOBALES", "💎 VIP: PLANNER", "🔐 CIBER", "🧬 BIO", "🚀 ESPACIO"])

    # --- SECCIÓN 1: INMUEBLES INTERNACIONALES ---
    with tabs[0]:
        st.header("Radar de Inversión Internacional")
        col_p1, col_p2 = st.columns(2)
        
        with col_p1:
            pais = st.selectbox("Seleccione País", list(DB_GLOBAL.keys()))
            ciudad = st.selectbox("Seleccione Ciudad", list(DB_GLOBAL[pais].keys())[:-1])
            m2_deseados = st.number_input("Metros Cuadrados", value=50)
            
        with col_p2:
            precio_m2 = DB_GLOBAL[pais][ciudad]
            subtotal = precio_m2 * m2_deseados
            gastos_ley = subtotal * DB_GLOBAL[pais]["Gastos"]
            total = subtotal + gastos_ley
            
            st.metric(f"Inversión en {ciudad}", f"USD {total:,.0f}")
            st.write(f"Precio promedio m²: USD {precio_m2}")
            st.write(f"Gastos legales estimados ({pais}): USD {gastos_ley:,.0f}")

    # --- SECCIÓN 2: VIP GLOBAL PLANNER (Nueva función solicitada) ---
    with tabs[1]:
        st.header("💎 VIP: Planificador de Relocalización")
        st.write("Configura tu perfil para analizar viabilidad en el extranjero.")
        
        c_vip1, c_vip2 = st.columns(2)
        with c_vip1:
            destino = st.selectbox("Destino de Interés", ["Miami, EEUU", "Madrid, España", "Nueva York, EEUU"])
            perfil = st.radio("Tu Perfil:", ["Estudiante", "Profesional IT", "Inversor / Negocios"])
            presupuesto = st.number_input("Presupuesto Mensual Disponible (USD)", value=2000)

        with c_vip2:
            st.subheader("Análisis de Viabilidad")
            # Lógica de utilidad real
            if destino == "Miami, EEUU":
                costo_vida = 3000 if perfil != "Estudiante" else 1800
                st.write(f"🏠 **Alojamiento:** Disponibilidad Media (Estudios desde $1,500)")
                if perfil == "Estudiante":
                    st.success("🎓 Becas disponibles en UM y FIU. Visa F-1 requerida.")
                elif perfil == "Profesional IT":
                    st.info("💼 Alta demanda en 'The Magic City'. Sueldos promedio: $6,000/mes.")
            
            elif destino == "Madrid, España":
                costo_vida = 1500
                st.write("🏠 **Alojamiento:** Muy alta demanda (Barrios económicos: Vallecas, Usera)")
                st.success("🇪🇸 Idioma compatible. Facilidad para visas de nómada digital.")

            # Resumen Financiero
            if presupuesto >= costo_vida:
                st.success(f"✅ Presupuesto apto para {destino}. Balance estimado: +{presupuesto - costo_vida} USD")
            else:
                st.error(f"⚠️ Presupuesto ajustado. Te faltan USD {costo_vida - presupuesto} para vivir cómodo.")

    # --- EL RESTO DE SECCIONES (Siguen igual para mantener utilidad) ---
    with tabs[2]: st.header("🔐 Ciberseguridad"); st.write("Módulo operativo.")
    with tabs[3]: st.header("🧬 Biotecnología"); st.write("Laboratorio en línea.")
    with tabs[4]: st.header("🚀 Aeroespacial"); st.write("Telemetría activa.")

st.divider()
st.caption("Pase Tech Suite v5.0 - Global Intelligence System")
