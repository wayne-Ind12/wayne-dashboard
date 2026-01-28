import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN Y ESTILO
st.set_page_config(page_title="Pase Tech Global", layout="wide", page_icon="🌐")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 2px solid #58a6ff; padding: 15px; border-radius: 12px; }
    .stTabs [data-baseweb="tab"] { color: #58a6ff; font-weight: bold; font-size: 18px; }
    .stSelectbox label, .stSlider label { color: #58a6ff !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MAESTRA (Países, Ciudades, Costo Vida, Inmuebles)
DB_GLOBAL = {
    "Uruguay": {"Montevideo": 2800, "Punta del Este": 3500, "Costo_Vida": 1200, "Visa": "Residencia Mercosur"},
    "EEUU": {"Miami": 6500, "Nueva York": 12000, "Los Angeles": 8000, "Costo_Vida": 3500, "Visa": "F1/H1-B/EB-5"},
    "España": {"Madrid": 4800, "Barcelona": 4200, "Valencia": 3000, "Costo_Vida": 1800, "Visa": "Nómada Digital/Arraigo"},
    "Brasil": {"San Pablo": 2100, "Rio de Janeiro": 1900, "Florianópolis": 1600, "Costo_Vida": 900, "Visa": "Residencia Mercosur"},
    "Japón": {"Tokio": 9000, "Osaka": 6000, "Kioto": 5500, "Costo_Vida": 2500, "Visa": "Working Holiday/Highly Skilled"},
    "Italia": {"Roma": 5000, "Milán": 7000, "Nápoles": 2800, "Costo_Vida": 2000, "Visa": "Ciudadanía/Elective Residence"}
}

# 3. NAVEGACIÓN PRINCIPAL
if 'intro_done' not in st.session_state:
    st.session_state.intro_done = False

if not st.session_state.intro_done:
    st.title("🌐 PASE TECH GLOBAL SOLUTIONS")
    st.subheader("Inteligencia Estratégica para un Mundo sin Fronteras")
    if st.button("INICIAR SESIÓN EN EL SISTEMA"):
        st.session_state.intro_done = True
else:
    tabs = st.tabs(["🏗️ INMUEBLES", "💎 VIP PLANNER", "🔐 CIBERSEGURIDAD", "🧬 BIOTECH", "🚀 ESPACIO"])

    # --- TAB 1: INMUEBLES INTERNACIONALES ---
    with tabs[0]:
        st.header("Análisis Inmobiliario Internacional")
        col_i1, col_i2 = st.columns(2)
        with col_i1:
            p_sel = st.selectbox("País de Inversión", list(DB_GLOBAL.keys()))
            c_sel = st.selectbox("Ciudad", list(DB_GLOBAL[p_sel].keys())[:-2])
            metros = st.number_input("Metros Cuadrados", 20, 1000, 60)
        with col_i2:
            base = DB_GLOBAL[p_sel][c_sel] * metros
            impuestos = base * 0.08 # Promedio global
            st.metric(f"Inversión Total en {c_sel}", f"USD {base + impuestos:,.0f}")
            st.info(f"Impuestos estimados en {p_sel}: USD {impuestos:,.0f}")

    # --- TAB 2: VIP GLOBAL PLANNER (ULTRA PERSONALIZADO) ---
    with tabs[1]:
        st.header("💎 VIP Global Migration & Career Planner")
        c1, c2 = st.columns([1, 1])
        with c1:
            dest = st.selectbox("Destino de Relocalización", list(DB_GLOBAL.keys()))
            profesion = st.selectbox("Tu Profesión / Ocupación", ["Estudiante", "Programador/IT", "Médico", "Inversionista", "Chef/Hostelería"])
            idioma = st.select_slider("Nivel de Idioma Local", options=["Nulo", "Básico", "Intermedio", "Avanzado/Nativo"])
        
        with c2:
            st.subheader("Reporte de Viabilidad")
            costo = DB_GLOBAL[dest]["Costo_Vida"]
            visa_tipo = DB_GLOBAL[dest]["Visa"]
            
            # Lógica personalizada
            if profesion == "Programador/IT":
                sueldo_est = costo * 2.5
                st.success(f"📈 Alta Demanda: Sueldo estimado USD {sueldo_est:,.0f}")
            elif profesion == "Estudiante":
                st.info(f"🎓 Costo de vida reducido estimado: USD {costo * 0.8:,.0f}")
            
            st.write(f"🛂 **Trámite Sugerido:** {visa_tipo}")
            st.write(f"🏠 **Dificultad de Alojamiento:** {'Alta' if costo > 2500 else 'Media/Baja'}")
            
            if idioma == "Nulo" and dest in ["Japón", "EEUU", "Italia"]:
                st.warning("⚠️ El idioma será una barrera crítica inicial.")

    # --- TAB 3: CIBERSEGURIDAD (Nuevas Opciones) ---
    with tabs[2]:
        st.header("Blindaje Digital Pase Tech")
        op_ciber = st.radio("Herramienta:", ["Generador de Llaves", "Auditoría de Red", "Recuperación de Datos"])
        if op_ciber == "Generador de Llaves":
            longitud = st.slider("Longitud", 12, 64, 24)
            st.code("".join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789!@#$%^&*", k=longitud)))
        else:
            st.write("Módulo en ejecución... Protegiendo puertos activos.")

    # --- TAB 4: BIOTECH (Nuevas Opciones) ---
    with tabs[3]:
        st.header("Pase Tech Bio-Analytics")
        modo_bio = st.selectbox("Módulo:", ["Análisis de Sangre", "Optimización Deportiva", "Estudio del Sueño"])
        if modo_bio == "Optimización Deportiva":
            deporte = st.text_input("Deporte", "Fútbol")
            horas = st.number_input("Horas de entrenamiento/semana", 1, 40, 10)
            st.metric("Recuperación Necesaria", f"{(horas * 1.5):.1f} horas/semana")
        else:
            st.info("Conecte un dispositivo wearable para ver datos en tiempo real.")

    # --- TAB 5: ESPACIO (Nuevas Opciones) ---
    with tabs[4]:
        st.header("Pase Tech Aerospace & SAT")
        servicio_esp = st.selectbox("Servicio Satelital:", ["Internet Global", "Fotos HD del Suelo", "Minería de Asteroides (Beta)"])
        
        if servicio_esp == "Fotos HD del Suelo":
            lat = st.number_input("Latitud", value=-34.90)
            lon = st.number_input("Longitud", value=-56.16)
            st.button("Capturar Imagen Satelital")
            st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&q=80&w=600", caption="Vista orbital procesada")
        elif servicio_esp == "Internet Global":
            st.metric("Latencia Estimada", "22ms")
            st.progress(85, text="Cobertura en tu zona")

st.divider()
st.caption("Pase Tech Suite v6.0 | Global & Aero Intelligence | 2026")

