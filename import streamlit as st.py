import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. CONFIGURACIÓN E IMAGEN DE MARCA
st.set_page_config(page_title="Wayne Capital - Premium", layout="wide", page_icon="💰")

# Sistema de "Llave de Pago"
CODIGO_REAL = "WAYNE2026" # Este es el código que tú vendes por 1 USD

st.title("🛡️ Wayne Intelligence Suite: Edición Inversor")

# 2. DATOS DE REFERENCIA
data_mvd = pd.DataFrame({
    'lat': [-34.9056, -34.9133, -34.8885, -34.8770, -34.8870, -34.9100],
    'lon': [-56.1367, -56.1555, -56.1620, -56.1850, -56.2020, -56.1150],
    'barrio': ['Pocitos', 'Punta Carretas', 'Centro', 'Aguada', 'Prado', 'Buceo'],
    'precio_m2_ref': [3150, 3400, 2050, 1850, 1750, 2800]
})

# 3. BARRA LATERAL - CONTROL DE ACCESO
st.sidebar.header("🔑 Acceso Premium")
user_code = st.sidebar.text_input("Introduce tu Código VIP", type="password")
es_premium = (user_code == CODIGO_REAL)

if not es_premium:
    st.sidebar.warning("⚠️ Funciones Pro Bloqueadas")
    st.sidebar.info("Para obtener tu código por 1 USD, envía un mensaje al desarrollador.")
else:
    st.sidebar.success("✅ Acceso VIP Activo")

# 4. ENTRADA DE DATOS
st.sidebar.divider()
st.sidebar.header("📥 Datos de la Propiedad")
with st.sidebar.form("nueva_casa"):
    b_barrio = st.selectbox("Barrio", data_mvd['barrio'])
    b_precio = st.number_input("Precio Venta (USD)", min_value=10000, value=115000)
    b_m2 = st.number_input("Metros Cuadrados", min_value=10, value=45)
    submit = st.form_submit_button("ANALIZAR")

# 5. LÓGICA DE CÁLCULO
m2_calculado = b_precio / b_m2
ref_zona = data_mvd[data_mvd['barrio'] == b_barrio]['precio_m2_ref'].values[0]
dif_porcentaje = ((m2_calculado - ref_zona) / ref_zona) * 100

# 6. INTERFAZ PÚBLICA (Lo que todos ven)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 Mapa de Mercado")
    st.map(data_mvd)

with col2:
    st.subheader("📊 Análisis Básico")
    st.metric("Precio m²", f"USD {m2_calculado:,.0f}")
    if m2_calculado < ref_zona:
        st.write("✨ **Estado:** Posible Oportunidad")
    else:
        st.write("✨ **Estado:** Precio de Mercado")

# 7. SECCIÓN PREMIUM (Solo con el código)
st.divider()
if es_premium:
    st.header("💎 PANEL EXCLUSIVO PARA INVERSORES")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("💰 Calculadora de Alquiler (ROI)")
        alquiler_estimado = st.number_input("Alquiler mensual estimado ($U)", value=25000)
        ganancia_anual_usd = (alquiler_estimado / 40) * 12
        roi = (ganancia_anual_usd / b_precio) * 100
        st.metric("Rentabilidad Anual (ROI)", f"{roi:.2f} %")
    
    with c2:
        st.subheader("📉 Comparativa Detallada")
        st.metric("Diferencia vs Barrio", f"{dif_porcentaje:.1f}%", delta=f"{dif_porcentaje:.1f}%", delta_color="inverse")
        if roi > 6: st.balloons()

    # Historial y Descarga solo para VIP
    st.subheader("📁 Tu Historial de Exportación")
    if 'historial' not in st.session_state: st.session_state.historial = []
    if submit:
        st.session_state.historial.append({"Fecha": datetime.now().strftime("%H:%M"), "Barrio": b_barrio, "ROI": f"{roi:.1f}%"})
    
    st.table(st.session_state.historial)
else:
    st.markdown("""
    ### 🔒 Contenido Bloqueado
    Compra tu acceso para desbloquear:
    * **Calculadora de ROI** (Saber cuánto vas a ganar por mes).
    * **Análisis de Oportunidad** detallado.
    * **Descarga de Reportes** en Excel.
    """)


