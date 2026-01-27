import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Wayne Real Estate", layout="wide")

st.title("🦇 Wayne Real Estate - Radar Montevideo")

# --- DATOS DEL MAPA ---
# Coordenadas aproximadas de barrios en Montevideo
data_barrios = pd.DataFrame({
    'lat': [-34.9056, -34.9133, -34.8885, -34.8770, -34.8870],
    'lon': [-56.1367, -56.1555, -56.1620, -56.1850, -56.2020],
    'barrio': ['Pocitos', 'Punta Carretas', 'Centro', 'Aguada', 'Prado'],
    'precio_m2': [3200, 3500, 2100, 1900, 1800]
})

st.markdown("### 📍 Mapa de Valor por Metro Cuadrado")
st.write("Explora las zonas de mayor rentabilidad:")

# Mostramos el mapa
st.map(data_barrios)

# --- CALCULADORA AVANZADA ---
st.sidebar.header("Calculadora de Inversión")
barrio_sel = st.sidebar.selectbox("Selecciona Zona", data_barrios['barrio'])
precio_total = st.sidebar.number_input("Precio Inmueble (USD)", value=120000)
m2_total = st.sidebar.number_input("Metros Cuadrados", value=45)

# Lógica de comparación
p_m2_actual = precio_total / m2_total
promedio_zona = data_barrios[data_barrios['barrio'] == barrio_sel]['precio_m2'].values[0]

st.markdown(f"## Análisis para {barrio_sel}")
col1, col2 = st.columns(2)

with col1:
    st.metric("Precio m² actual", f"USD {p_m2_actual:,.0f}")
with col2:
    diferencia = p_m2_actual - promedio_zona
    st.metric("Vs. Promedio Zona", f"{diferencia:,.0f} USD", delta=-diferencia)

if p_m2_actual < promedio_zona:
    st.success("✅ ¡Oportunidad detectada! El precio está por debajo del promedio del barrio.")
else:
    st.error("⚠️ El precio está por encima del promedio. ¡Negocia con el vendedor!")

# --- TABLA DE DATOS ---
with st.expander("Ver tabla de referencia de precios"):
    st.table(data_barrios)
