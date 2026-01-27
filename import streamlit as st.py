import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN PASE TECH
st.set_page_config(page_title="Pase Tech - Dashboard", layout="wide", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #050a30; color: #ffffff; }
    .stTabs [data-baseweb="tab"] { color: #7ec8e3; font-weight: bold; font-size: 18px; }
    .stMetric { background-color: #000c66; border: 1px solid #7ec8e3; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ PASE TECH")
st.caption(f"Inteligencia de Datos | Montevideo | {datetime.now().strftime('%d/%m/%Y')}")

# 2. DIVISIONES
pestanas = st.tabs(["🏘️ INMUEBLES", "🧪 BIOTECH", "📈 FINANZAS", "🛰️ ESPACIO"])

# --- INMUEBLES ---
with pestanas[0]:
    st.header("Radar Inmobiliario")
    col1, col2 = st.columns([2, 1])
    with col1:
        # Mapa con datos fijos (Pocitos y Centro)
        st.map(pd.DataFrame({
            'lat': [-34.9056, -34.8885],
            'lon': [-56.1367, -56.1620]
        }))
    with col2:
        st.subheader("Simulador ROI")
        p = st.number_input("Precio (USD)", value=130000)
        a = st.number_input("Alquiler (UYU)", value=25000)
        st.metric("Rendimiento", f"{((a/40)*12/p)*100:.2f}%")

# --- BIOTECH (Sin usar Numpy para evitar errores) ---
with pestanas[1]:
    st.header("Pase Tech Bio-Lab")
    st.subheader("Análisis de Crecimiento")
    dias = st.slider("Días de observación", 5, 30, 15)
    
    # Creamos datos aleatorios usando solo Python básico
    datos_simples = [random.uniform(10, 20) + i for i in range(dias)]
    df_bio = pd.DataFrame(datos_simples, columns=['Biomasa'])
    st.line_chart(df_bio)

# --- FINANZAS ---
with pestanas[2]:
    st.header("Monitor de Mercados")
    m1, m2 = st.columns(2)
    m1.metric("NASDAQ", "15,620.50", "+2.1%")
    m2.metric("Dólar/Peso UYU", "39.50", "0.0%")
    
    # Gráfico simple
    st.area_chart(pd.DataFrame([random.random() for _ in range(10)], columns=['Tendencia']))

# --- ESPACIO ---
with pestanas[3]:
    st.header("Aerospace Division")
    st.write("Próximos Lanzamientos 2026")
    st.table(pd.DataFrame({
        "Misión": ["Starlink MVD", "Artemis II", "Mars Probe"],
        "Fecha": ["Febrero 2026", "Septiembre 2026", "Noviembre 2026"]
    }))

st.divider()
st.caption("Pase Tech Suite v1.2 - Edición Estable")


