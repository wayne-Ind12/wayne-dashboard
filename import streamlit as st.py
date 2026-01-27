import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. CONFIGURACIÓN DE LA NAVE MISTERIOSA
st.set_page_config(page_title="Wayne Capital - MVD Radar", layout="wide", page_icon="🦇")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #00ff00; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Wayne Intelligence Suite: Montevideo")
st.write(f"Sincronizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# 2. BASE DE DATOS DE REFERENCIA (Barrios de Montevideo)
# Estos datos son los que usará el mapa y el comparador
data_mvd = pd.DataFrame({
    'lat': [-34.9056, -34.9133, -34.8885, -34.8770, -34.8870, -34.9100],
    'lon': [-56.1367, -56.1555, -56.1620, -56.1850, -56.2020, -56.1150],
    'barrio': ['Pocitos', 'Punta Carretas', 'Centro', 'Aguada', 'Prado', 'Buceo'],
    'precio_m2_ref': [3150, 3400, 2050, 1850, 1750, 2800]
})

# 3. BARRA LATERAL (CEREBRO DEL NEGOCIO)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/be/Batman_Logo.png", width=100)
st.sidebar.header("📥 Registro de Oportunidad")

with st.sidebar.form("nueva_casa"):
    b_barrio = st.selectbox("Barrio", data_mvd['barrio'])
    b_precio = st.number_input("Precio Venta (USD)", min_value=10000, value=115000)
    b_m2 = st.number_input("Metros Cuadrados", min_value=10, value=45)
    submit = st.form_submit_button("REGISTRAR EN HISTORIAL")

# 4. CUERPO PRINCIPAL - MAPA Y MÉTRICAS
col_map, col_info = st.columns([2, 1])

with col_map:
    st.subheader("📍 Mapa de Calor: Valor m²")
    st.map(data_mvd)

with col_info:
    st.subheader("📊 Análisis de Valor")
    m2_calculado = b_precio / b_m2
    ref_zona = data_mvd[data_mvd['barrio'] == b_barrio]['precio_m2_ref'].values[0]
    dif_porcentaje = ((m2_calculado - ref_zona) / ref_zona) * 100

    st.metric("Tu m²", f"USD {m2_calculado:,.0f}")
    st.metric("Promedio Zona", f"USD {ref_zona:,.0f}", delta=f"{dif_porcentaje:.1f}%", delta_color="inverse")

    if m2_calculado < ref_zona:
        st.success("💎 ¡Ganga Detectada! Por debajo del mercado.")
    else:
        st.warning("⚖️ Precio de mercado o superior.")

# 5. BASE DE DATOS Y DESCARGA
st.divider()
st.subheader("📁 Historial de Caza (Base de Datos)")

# Lógica para mantener los datos en la sesión actual
if 'historial' not in st.session_state:
    st.session_state.historial = []

if submit:
    nuevo_registro = {
        "Fecha": datetime.now().strftime("%H:%M:%S"),
        "Barrio": b_barrio,
        "Precio": b_precio,
        "m2": b_m2,
        "USD/m2": round(m2_calculado, 2),
        "Estado": "Oportunidad" if m2_calculado < ref_zona else "Normal"
    }
    st.session_state.historial.append(nuevo_registro)

if st.session_state.historial:
    df_h = pd.DataFrame(st.session_state.historial)
    st.dataframe(df_h, use_container_width=True)
    
    # Exportación a Excel/CSV
    csv_data = df_h.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 DESCARGAR BASE DE DATOS (CSV)",
        data=csv_data,
        file_name=f"reporte_wayne_{datetime.now().strftime('%d_%m')}.csv",
        mime="text/csv"
    )
else:
    st.info("Aún no has registrado propiedades en esta sesión.")

st.caption("Wayne Capital Uruguay - Sistema de Inteligencia Inmobiliaria")

