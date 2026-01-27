import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Wayne Capital", page_icon="🦇")

st.title("🛡️ Wayne Intelligence Suite")
st.subheader("Uruguay Real Estate & Market Monitor")

# --- SECCIÓN 1: MONITOR DE MERCADO ---
st.markdown("### 📊 Monitor de Referencia (BTC)")
if st.button('Escanear Mercado'):
    try:
        res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        precio = float(res.json()['price'])
        st.metric("Bitcoin Price", f"USD {precio:,.2f}")
    except:
        st.error("Error al conectar con el satélite.")

# --- SECCIÓN 2: CALCULADORA DE INVERSIÓN ---
st.markdown("### 🏠 Analizador Inmobiliario")
col1, col2 = st.columns(2)

with col1:
    barrio = st.selectbox("Barrio", ["Pocitos", "Centro", "Carrasco", "Cordón", "Prado"])
    precio_casa = st.number_input("Precio Total (USD)", value=120000)

with col2:
    metros = st.number_input("Metros Cuadrados (m2)", value=50)

if st.button('Calcular Rentabilidad'):
    precio_m2 = precio_casa / metros
    st.write(f"El precio por m2 es: **USD {precio_m2:,.2f}**")
    
    # Lógica simple de comparación
    if precio_m2 < 2000:
        st.success("🔥 ¡POSIBLE GANGA! Muy por debajo del promedio.")
    else:
        st.warning("⚖️ Precio dentro del rango normal o elevado.")

st.sidebar.info("Este dashboard corre en la nube de Google a través de Streamlit.")