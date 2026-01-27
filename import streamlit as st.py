import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# 1. CONFIGURACIÓN DE MARCA
st.set_page_config(page_title="Wayne Industries MVD", layout="wide", page_icon="🦇")

# Estilo Negro y Verde (Estilo Terminal Wayne)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e0e0e0; }
    .stTabs [data-baseweb="tab"] { color: #00ff00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Wayne Industries - Global Dashboard")
st.caption(f"Acceso Autorizado - Montevideo Division | {datetime.now().strftime('%d/%m/%Y')}")

# 2. NAVEGACIÓN POR DIVISIONES
tab_mvd, tab_biotech, tab_finance = st.tabs([
    "🏢 REAL ESTATE (MVD)", 
    "🧬 BIOTECHNOLOGY", 
    "💰 WEALTH MANAGEMENT"
])

# --- DIVISIÓN 1: REAL ESTATE (Con Gráficos Mejorados) ---
with tab_mvd:
    st.header("Análisis Geográfico de Montevideo")
    
    data_mvd = pd.DataFrame({
        'Barrio': ['Pocitos', 'Punta Carretas', 'Centro', 'Aguada', 'Prado', 'Buceo'],
        'lat': [-34.9056, -34.9133, -34.8885, -34.8770, -34.8870, -34.9100],
        'lon': [-56.1367, -56.1555, -56.1620, -56.1850, -56.2020, -56.1150],
        'Precio_m2': [3150, 3400, 2050, 1850, 1750, 2800]
    })

    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Mapa interactivo
        st.map(data_mvd)
    
    with col2:
        # Gráfico de Barras Moderno
        fig_bar = px.bar(data_mvd, x='Barrio', y='Precio_m2', 
                         color='Precio_m2', title="Ranking de Precios (USD/m²)",
                         color_continuous_scale='Greens')
        fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig_bar, use_container_width=True)

# --- DIVISIÓN 2: BIOTECHNOLOGY (Simulador de Laboratorio) ---
with tab_biotech:
    st.header("Wayne Biotech Lab - Análisis de Células")
    
    col_bio1, col_bio2 = st.columns(2)
    
    with col_bio1:
        st.subheader("Simulador de Crecimiento Bacteriano")
        horas = st.slider("Tiempo de cultivo (Horas)", 1, 48, 24)
        tasa = st.slider("Tasa de crecimiento", 0.1, 1.0, 0.3)
        
        # Fórmula matemática real: N = N0 * e^(rt)
        tiempo = list(range(horas))
        poblacion = [100 * (2.71 ** (tasa * t)) for t in tiempo]
        
        fig_bio = px.line(x=tiempo, y=poblacion, title="Progreso de Cultivo Celular",
                          labels={'x':'Tiempo (h)', 'y':'N° de Células'})
        fig_bio.update_traces(line_color='#00ff00')
        st.plotly_chart(fig_bio, use_container_width=True)
        
    with col_bio2:
        st.subheader("Estado de Reactores")
        st.write("Análisis de pureza de compuestos:")
        st.progress(85, text="Pureza del Suero Wayne-X: 85%")
        st.progress(40, text="Estabilidad de Isótopos: 40%")

# --- DIVISIÓN 3: WEALTH MANAGEMENT (Cripto y Activos) ---
with tab_finance:
    st.header("Terminal de Inteligencia Financiera")
    
    st.write("Escaneando mercados globales...")
    
    # Simulamos un gráfico de velas (Candlestick) de una acción de Wayne
    fig_fin = go.Figure(data=[go.Candlestick(x=['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
                open=[100, 110, 105, 115],
                high=[112, 118, 110, 120],
                low=[95, 108, 100, 112],
                close=[110, 105, 115, 118])])
    
    fig_fin.update_layout(title="Acciones de Wayne Enterprises (WYN)", template="plotly_dark")
    st.plotly_chart(fig_fin, use_container_width=True)

st.divider()
st.caption("Propiedad de Industrias Wayne. Uso exclusivo para personal autorizado.")
