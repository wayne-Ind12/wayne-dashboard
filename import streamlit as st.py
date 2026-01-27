import streamlit as st
import pandas as pd
import numpy as np  # <--- ESTA ES LA LÍNEA QUE FALTA
from datetime import datetime

# 1. CONFIGURACIÓN DE MARCA: PASE TECH
st.set_page_config(page_title="Pase Tech - Dashboard", layout="wide", page_icon="⚡")

# Estilo personalizado Pase Tech (Azul Eléctrico y Gris Oscuro)
st.markdown("""
    <style>
    .stApp { background-color: #050a30; color: #ffffff; }
    .stTabs [data-baseweb="tab"] { color: #7ec8e3; font-weight: bold; font-size: 18px; }
    .stMetric { background-color: #000c66; border: 1px solid #7ec8e3; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ PASE TECH")
st.caption(f"Inteligencia de Datos Aplicada | Montevideo, Uruguay | {datetime.now().strftime('%d/%m/%Y')}")

# 2. SISTEMA DE NAVEGACIÓN
pestanas = st.tabs(["🏘️ INMUEBLES", "🧪 BIOTECNOLOGÍA", "📈 FINANZAS", "🛰️ ESPACIO"])

# --- DIVISIÓN 1: INMUEBLES (Real Estate) ---
with pestanas[0]:
    st.header("Análisis Inmobiliario MVD")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        map_data = pd.DataFrame({
            'lat': [-34.9056, -34.9133, -34.8885, -34.8770],
            'lon': [-56.1367, -56.1555, -56.1620, -56.1850]
        })
        st.map(map_data)
        
    with col2:
        st.subheader("Calculadora de Inversión")
        precio = st.number_input("Precio Propiedad (USD)", value=130000)
        alquiler = st.number_input("Alquiler Mensual (UYU)", value=25000)
        roi = ((alquiler / 40) * 12 / precio) * 100
        st.metric("Rentabilidad Estimada", f"{roi:.2f}%")
        st.write("Promedio mercado MVD: **4.5% - 5.5%**")

# --- DIVISIÓN 2: BIOTECNOLOGÍA ---
with pestanas[1]:
    st.header("Pase Tech Bio-Lab")
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Analizador de Salud")
        edad = st.slider("Edad del Paciente", 1, 100, 25)
        glucosa = st.number_input("Nivel de Glucosa (mg/dL)", value=90)
        if glucosa > 100:
            st.warning("⚠️ Atención: Niveles elevados detectados.")
        else:
            st.success("✅ Niveles dentro del rango normal.")
            
    with c2:
        st.subheader("Crecimiento Molecular")
        dias = st.slider("Días de observación", 1, 30, 10)
        datos_bio = pd.DataFrame(np.random.cumsum(np.random.randn(dias, 1) + 0.5), columns=['Biomasa'])
        st.line_chart(datos_bio)

# --- DIVISIÓN 3: FINANZAS ---
with pestanas[2]:
    st.header("Monitor de Mercados Pase Tech")
    m1, m2, m3 = st.columns(3)
    m1.metric("NASDAQ", "15,620.50", "+2.1%")
    m2.metric("Ethereum (ETH)", "2,250.40", "-1.4%")
    m3.metric("Dólar/Peso UYU", "39.50", "0.0%")
    
    st.subheader("Proyección de Cartera")
    fin_data = pd.DataFrame(np.random.randn(20, 2), columns=['Tecnológicas', 'Energía'])
    st.area_chart(fin_data)

# --- DIVISIÓN 4: ESPACIO (Aerospace) ---
with pestanas[3]:
    st.header("Exploración Espacial & Satélites")
    
    col_sp1, col_sp2 = st.columns(2)
    
    with col_sp1:
        st.subheader("Simulación de Despegue")
        combustible = st.progress(75, text="Combustible Nivel 1")
        oxigeno = st.progress(90, text="Soporte Vital")
        
        # Simulación de trayectoria
        t = np.linspace(0, 10, 50)
        altitud = t**2 # Ecuación simple de parábola
        df_vuelo = pd.DataFrame({'Altitud (km)': altitud})
        st.line_chart(df_vuelo)

    with col_sp2:
        st.subheader("Próximos Lanzamientos (Global)")
        lanzamientos = {
            "Misión": ["SpaceX Starlink", "Blue Origin NS-25", "NASA Artemis II"],
            "Fecha": ["Febrero 2026", "Marzo 2026", "Septiembre 2026"],
            "Estado": ["Confirmado", "En revisión", "Planificado"]
        }
        st.table(pd.DataFrame(lanzamientos))

st.divider()
st.caption("Pase Tech © 2026 - Montevideo, Uruguay. Soluciones de Software de Próxima Generación.")

