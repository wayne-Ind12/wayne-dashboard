import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN Y ESTILO PROFESIONAL
st.set_page_config(page_title="Pase Tech Global", layout="wide", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .stTabs [data-baseweb="tab"] { color: #58a6ff; font-size: 18px; }
    .stButton>button { background-color: #238636; color: white; width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 2. LÓGICA DE NAVEGACIÓN
if 'intro_done' not in st.session_state:
    st.session_state.intro_done = False

# --- PANTALLA INICIAL: QUIÉNES SOMOS ---
if not st.session_state.intro_done:
    st.title("⚡ PASE TECH GLOBAL SOLUTIONS")
    col_a, col_b = st.columns(2)
    with col_a:
        st.header("Liderando la Transformación Digital")
        st.write("""
        En **Pase Tech**, no creamos simples aplicaciones; construimos herramientas de toma de decisiones. 
        Nuestra suite integra análisis inmobiliario real, seguridad perimetral, 
        monitoreo bio-médico y logística aeroespacial.
        
        **Nuestra promesa:** Convertir datos complejos en rentabilidad y seguridad para nuestros clientes.
        """)
        if st.button("ACCEDER AL DASHBOARD PROFESIONAL"):
            st.session_state.intro_done = True
    with col_b:
        st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=500", caption="Análisis de Datos en Tiempo Real")

else:
    # --- DASHBOARD PRINCIPAL ---
    st.title("🛡️ Terminal de Gestión Pase Tech")
    tabs = st.tabs(["🏗️ INMUEBLES PRO", "🔐 CIBERSEGURIDAD", "🏎️ MOVILIDAD", "🧬 BIOTECH", "🛰️ AGRO-ESPACIO"])

    # 1. INMUEBLES: CALCULADORA DE INVERSIÓN REAL (URUGUAY)
    with tabs[0]:
        st.header("Calculadora de Inversión Inmobiliaria")
        col1, col2 = st.columns([1, 1])
        with col1:
            precio = st.number_input("Precio de Venta (USD)", value=150000, step=5000)
            alquiler_estimado = st.number_input("Alquiler mensual esperado (UYU)", value=30000, step=1000)
            tipo_compra = st.selectbox("Tipo de Propiedad", ["Usada", "Obra Nueva / Promovida"])
            
        with col2:
            # Lógica de costos reales en Uruguay
            comision_inmo = precio * 0.0366  # 3% + IVA
            itp_impuesto = precio * 0.02     # Impuesto a la transferencia
            escritura_gastos = precio * 0.03 # Escribano y timbres
            
            total_gastos = comision_inmo + itp_impuesto + escritura_gastos
            if tipo_compra == "Obra Nueva / Promovida":
                total_gastos += precio * 0.04 # Gastos de ocupación
            
            inversion_total = precio + total_gastos
            rentabilidad = ((alquiler_estimado / 40) * 12 / inversion_total) * 100
            
            st.metric("Inversión Total Necesaria", f"USD {inversion_total:,.0f}")
            st.metric("Rentabilidad Anual (ROI)", f"{rentabilidad:.2f}%")
            st.write(f"Gastos de cierre: USD {total_gastos:,.0f}")

    # 2. CIBERSEGURIDAD: AUDITORÍA DE RIESGOS
    with tabs[1]:
        st.header("Auditoría de Seguridad Digital")
        st.write("Evalúa el nivel de protección de tu infraestructura.")
        empresa = st.text_input("Nombre de la Organización / Red")
        check1 = st.checkbox("¿Tiene autenticación de dos factores (2FA) en todos los accesos?")
        check2 = st.checkbox("¿Los respaldos (backups) se realizan semanalmente y fuera de la red?")
        check3 = st.checkbox("¿El software de los servidores está actualizado a la última versión?")
        
        nivel_riesgo = 100
        if check1: nivel_riesgo -= 30
        if check2: nivel_riesgo -= 40
        if check3: nivel_riesgo -= 30
        
        st.subheader(f"Nivel de Riesgo para {empresa}")
        if nivel_riesgo > 50:
            st.error(f"RIESGO CRÍTICO: {nivel_riesgo}%")
            st.write("⚠️ Se recomienda intervención inmediata en sus protocolos de acceso.")
        else:
            st.success(f"RIESGO BAJO: {nivel_riesgo}%")
            st.write("✅ Sus sistemas cumplen con los estándares básicos de Pase Tech.")

    # 3. MOVILIDAD: DISEÑADOR DE FLOTAS LOGÍSTICAS
    with tabs[2]:
        st.header("Pase Tech Mobility: Configuración de Vehículos")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            modelo = st.selectbox("Vehículo Base", ["Dron de Reparto", "Camioneta Eléctrica", "Blindado Ejecutivo"])
            color = st.color_picker("Color Corporativo", "#1f77b4")
            blindaje = st.select_slider("Nivel de Protección", options=["Nivel 1 (Ligero)", "Nivel 2 (Reforzado)", "Nivel 3 (Militar)"])
        with col_m2:
            st.write(f"### Especificaciones de {modelo}")
            st.write(f"- Color HEX: {color}")
            st.write(f"- Blindaje: {blindaje}")
            peso_extra = {"Nivel 1 (Ligero)": 50, "Nivel 2 (Reforzado)": 200, "Nivel 3 (Militar)": 600}
            st.metric("Peso Adicional de Seguridad", f"{peso_extra[blindaje]} kg")
            st.button("ENVIAR A PRODUCCIÓN")

    # 4. BIOTECH: DIAGNÓSTICO DE RENDIMIENTO
    with tabs[3]:
        st.header("Bio-Lab: Análisis de Salud Preventiva")
        st.write("Calculadora de parámetros vitales para seguros de vida y salud.")
        c_bio1, c_bio2 = st.columns(2)
        with c_bio1:
            edad = st.number_input("Edad", 1, 120, 30)
            glucosa = st.number_input("Glucosa en ayunas (mg/dL)", 50, 250, 90)
        with c_bio2:
            presion = st.slider("Presión Sistólica (Máxima)", 80, 200, 120)
            
        if glucosa > 126 or presion > 140:
            st.warning("🚨 Alerta de Salud: Parámetros fuera de rango normal detectados.")
        else:
            st.success("✨ Parámetros estables. Reporte de salud óptimo.")
        
        # Historial de tendencia
        st.line_chart([random.randint(70, 130) for _ in range(15)])

    # 5. AGRO-ESPACIO: MONITOREO SATELITAL
    with tabs[4]:
        st.header("División Aeroespacial y Agro-Tec")
        st.write("Utilidad: Monitoreo de cultivos mediante índices de vegetación satelital.")
        lote = st.text_input("Identificación de Lote / Campo", "Sector Norte - UY")
        indice_ndvi = st.slider("Índice de Vegetación (NDVI)", 0.0, 1.0, 0.6)
        
        if indice_ndvi < 0.4:
            st.error("⚠️ Estrés Hídrico detectado en el lote. Se sugiere riego inmediato.")
        else:
            st.success("🌾 Cultivo saludable. Densidad de biomasa óptima.")
        
        st.write("Próximos Pasajes Satelitales:")
        st.table(pd.DataFrame({
            "Satélite": ["Pase-SAT 1", "Sentinel-2", "Landsat-9"],
            "Horario": ["14:20", "03:45", "18:10"],
            "Resolución": ["Alta", "Media", "Media"]
        }))

st.divider()
st.caption("Pase Tech Global Solutions © 2026 - Herramientas de Precisión.")

