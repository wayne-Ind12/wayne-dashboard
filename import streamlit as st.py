import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURACIÓN Y ESTILO
st.set_page_config(page_title="Wayne Capital MVD", layout="wide")

# CSS para que los botones y la interfaz se vean más "App"
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #1f77b4; color: white; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #1a1c23; border-radius: 10px; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. SISTEMA DE NAVEGACIÓN (Botones Superiores)
st.title("🦇 Wayne Intelligence Suite")
pestana_inicio, pestana_radar, pestana_vip = st.tabs(["🏠 INICIO", "📍 RADAR PÚBLICO", "💎 ZONA INVERSOR (PRO)"])

# 3. CONTENIDO: PESTAÑA INICIO
with pestana_inicio:
    st.header("Bienvenido al Radar Inmobiliario de Montevideo")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        ### ¿Por qué usar nuestra tecnología?
        Encontrar una oportunidad en Uruguay es difícil. Nuestra herramienta analiza:
        * **Precio real por m2** en los principales barrios.
        * **Comparativa automática** contra el promedio de la zona.
        * **Cálculo de ROI** (Rentabilidad de alquiler).
        """)
    with col2:
        st.info("### 🎁 Oferta de Lanzamiento: USD 1.00")
        st.write("Obtén tu código de acceso VIP y desbloquea el análisis de rentabilidad.")
        st.link_button("ADQUIRIR CÓDIGO VIP", "https://link-de-tu-mercado-pago.com")

# 4. CONTENIDO: PESTAÑA RADAR (Público)
with pestana_radar:
    st.subheader("📍 Mapa de Valores en Tiempo Real")
    data_mvd = pd.DataFrame({
        'lat': [-34.9056, -34.9133, -34.8885, -34.8770],
        'lon': [-56.1367, -56.1555, -56.1620, -56.1850],
        'barrio': ['Pocitos', 'Punta Carretas', 'Centro', 'Aguada'],
        'precio_m2_ref': [3150, 3400, 2050, 1850]
    })
    st.map(data_mvd)
    st.write("Este mapa muestra las zonas que estamos monitoreando actualmente.")

# 5. CONTENIDO: PESTAÑA VIP (Bloqueada)
with pestana_vip:
    # Verificación de Código
    codigo_acceso = st.text_input("Introduce tu código de 1 dólar para desbloquear:", type="password")
    
    if codigo_acceso == "WAYNE2026":
        st.success("🛰️ CONEXIÓN ESTABLECIDA - MODO INVERSOR ACTIVO")
        
        # --- CALCULADORA PRO ---
        st.header("💎 Calculadora de Rentabilidad Pro")
        c1, c2 = st.columns(2)
        with c1:
            b_precio = st.number_input("Precio Propiedad (USD)", value=120000)
            b_barrio = st.selectbox("Barrio de la Propiedad", data_mvd['barrio'])
        with c2:
            b_m2 = st.number_input("Metros de la Propiedad", value=50)
            alquiler_est = st.number_input("Alquiler Mensual Esperado ($U)", value=28000)
        
        # Cálculos Pro
        roi = ((alquiler_est / 40) * 12 / b_precio) * 100
        m2_calc = b_precio / b_m2
        
        st.divider()
        m1, m2 = st.columns(2)
        m1.metric("Rentabilidad Anual (ROI)", f"{roi:.2f} %")
        m2.metric("Precio por m2", f"USD {m2_calc:,.0f}")
        
        if roi > 6:
            st.balloons()
            st.success("🔥 ¡OPORTUNIDAD DE ORO! Esta rentabilidad es superior al promedio.")
    else:
        st.warning("🔒 Esta sección es exclusiva para suscriptores.")
        st.image("https://images.unsplash.com/photo-1554224155-169641357599?auto=format&fit=crop&q=80&w=500", caption="Análisis avanzado bloqueado")

st.caption("Wayne Capital - Montevideo v4.0")

