import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN DE MARCA
st.set_page_config(page_title="Pase Tech Omni-Suite", layout="wide", page_icon="🛡️")

# Estilo "Bat-Tech" (Gris Carbono y Azul Neón)
st.markdown("""
    <style>
    .stApp { background-color: #0a0b10; color: #ffffff; }
    .stTabs [data-baseweb="tab"] { color: #00d4ff; font-weight: bold; }
    .stSelectbox label, .stSlider label { color: #00d4ff !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ PASE TECH: OMNI-SUITE")
st.write(f"Nivel de Acceso: **Administrador** | {datetime.now().strftime('%H:%M:%S')}")

# 2. DIVISIONES INSPIRADAS EN LAS INDUSTRIAS WAYNE
tabs = st.tabs([
    "🏢 URBAN & REAL ESTATE", 
    "🦇 TACTICAL & DEFENSE", 
    "🏎️ ADVANCED MOBILITY", 
    "🧬 MEDICAL & BIO", 
    "🛰️ SATELLITE NETWORK"
])

# --- SECCIÓN 1: URBAN & REAL ESTATE ---
with tabs[0]:
    st.header("Análisis Urbano de Montevideo")
    opcion_barrio = st.selectbox("Seleccionar Sector para Análisis:", ["Pocitos", "Carrasco", "Cordón", "Centro", "Malvín"])
    
    col1, col2 = st.columns(2)
    with col1:
        # Precios ficticios por barrio
        precios = {"Pocitos": 3100, "Carrasco": 3500, "Cordón": 2100, "Centro": 2000, "Malvín": 2800}
        st.metric(f"Precio Promedio en {opcion_barrio}", f"USD {precios[opcion_barrio]}/m²")
        st.write("Estado del mercado: **Alta Demanda**")
    with col2:
        st.subheader("Mapa de Vigilancia de Inmuebles")
        st.map(pd.DataFrame({'lat': [-34.90], 'lon': [-56.16]}))

# --- SECCIÓN 2: TACTICAL & DEFENSE ---
with tabs[1]:
    st.header("División de Seguridad y Defensa")
    tipo_seguridad = st.radio("Módulo de Escaneo:", ["Ciberseguridad", "Perímetro Físico", "Drones"])
    
    if tipo_seguridad == "Ciberseguridad":
        st.code("SCANNING NETWORK... [PASS] \nFIREWALL: ACTIVE \nINTRUSIONS: 0", language="bash")
        st.progress(100)
    elif tipo_seguridad == "Perímetro Físico":
        st.warning("Sensor detectado en Sector 4. Activando cámaras...")
        st.image("https://images.unsplash.com/photo-1557597774-9d2739f85a94?auto=format&fit=crop&q=80&w=400", caption="Vista de Cámara Térmica")
    else:
        st.info("Desplegando Drones de Reconocimiento...")
        st.bar_chart([10, 25, 40, 30, 45])

# --- SECCIÓN 3: ADVANCED MOBILITY ---
with tabs[2]:
    st.header("Pase Tech Motors: Prototipos")
    vehiculo = st.select_slider("Potencia del Motor (HP)", options=[500, 1000, 1500, 2000])
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Velocidad Máxima Est.", f"{vehiculo / 5} km/h")
        st.metric("Autonomía Eléctrica", "600 km")
    with c2:
        st.subheader("Curva de Aceleración")
        aceleracion = [0, 50, 120, 240, vehiculo/5]
        st.line_chart(aceleracion)

# --- SECCIÓN 4: MEDICAL & BIO ---
with tabs[3]:
    st.header("Pase Tech Bio-Lab")
    paciente = st.text_input("ID del Paciente", "B. Wayne")
    analisis = st.selectbox("Tipo de Análisis:", ["Toxicología", "Ritmo Cardíaco", "Genética"])
    
    if analisis == "Ritmo Cardíaco":
        st.write(f"Analizando a {paciente}...")
        pulso = [70, 72, 75, 80, 74, 70, 68]
        st.line_chart(pulso)
        st.success("Ritmo estable bajo estrés.")
    else:
        st.info("Cargando base de datos molecular...")
        st.write("Pureza de la muestra: 98.4%")

# --- SECCIÓN 5: SATELLITE NETWORK ---
with tabs[4]:
    st.header("Red Satelital Global")
    satelite = st.selectbox("Seleccionar Satélite:", ["Pase-1 (Latam)", "Pase-2 (Global)", "Pase-3 (Deep Space)"])
    
    st.write(f"Señal del {satelite}: **Fuerte**")
    # Gráfico de interferencia
    interferencia = [random.random() for _ in range(15)]
    st.area_chart(interferencia)
    
    st.table(pd.DataFrame({
        "Misión": ["Relevamiento Climático", "GPS Privado", "Enlace Cuántico"],
        "Estado": ["Operativo", "Operativo", "En Pruebas"]
    }))

st.divider()
st.caption("Pase Tech Omni-Suite © 2026 - Control Total de Datos")



