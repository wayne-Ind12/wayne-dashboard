import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Wayne Industries", layout="wide")

st.title("🛡️ Wayne Industries - Suite MVD")

# 2. TABS (Navegación)
tab1, tab2, tab3 = st.tabs(["🏢 REAL ESTATE", "🧬 BIOTECH", "💰 FINANZAS"])

# --- TAB 1: INMOBILIARIA ---
with tab1:
    st.header("Radar de Montevideo")
    
    # Datos simples
    df_mvd = pd.DataFrame({
        'Barrio': ['Pocitos', 'Centro', 'Aguada', 'Prado'],
        'Precio_m2': [3150, 2050, 1850, 1750]
    }).set_index('Barrio') # Seteamos el índice para el gráfico
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Mapa de Operaciones")
        # Mapa nativo (Solo necesita lat y lon)
        map_data = pd.DataFrame({
            'lat': [-34.9056, -34.8885, -34.8770, -34.8870],
            'lon': [-56.1367, -56.1620, -56.1850, -56.2020]
        })
        st.map(map_data)
        
    with col2:
        st.write("Ranking de Precios (USD/m2)")
        st.bar_chart(df_mvd)

# --- TAB 2: BIOTECH ---
with tab2:
    st.header("Laboratorio de Biotecnología")
    st.write("Simulación de Crecimiento Celular")
    
    # Generamos datos matemáticos simples con Numpy
    chart_data = pd.DataFrame(
        np.random.randn(20, 1),
        columns=['Crecimiento']
    )
    st.line_chart(chart_data)
    st.success("Sistemas Biométricos Online")

# --- TAB 3: FINANZAS ---
with tab3:
    st.header("División Finanzas")
    st.metric("Acciones Wayne Corp", "150.25 USD", "+5.4%")
    
    # Un gráfico de área nativo
    finance_data = pd.DataFrame(
        np.random.randn(15, 2),
        columns=['Acciones', 'Bonos']
    )
    st.area_chart(finance_data)

st.divider()
st.caption("Wayne Industries - Versión Lite (Sin Dependencias Externas)")
