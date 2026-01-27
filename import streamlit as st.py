import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la App
st.title("🦇 Wayne Real Estate - Base de Datos")

# --- ENTRADA DE DATOS ---
with st.form("registro_propiedad"):
    st.write("Registrar nueva oportunidad detectada")
    f_barrio = st.selectbox("Barrio", ["Pocitos", "Centro", "Carrasco", "Cordón", "Prado"])
    f_precio = st.number_input("Precio (USD)", value=100000)
    f_m2 = st.number_input("Metros", value=40)
    
    boton_guardar = st.form_submit_button("Guardar en la Nube")

# --- LÓGICA DE GUARDADO ---
if boton_guardar:
    # Creamos la nueva fila
    nueva_fila = {
        "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Barrio": f_barrio,
        "Precio": f_precio,
        "m2": f_m2,
        "Resultado": f_precio / f_m2
    }
    
    # Aquí es donde ocurre la magia:
    # Por ahora lo guardamos en el 'estado' de la sesión para probar
    if 'db' not in st.session_state:
        st.session_state.db = []
    
    st.session_state.db.append(nueva_fila)
    st.success("✅ ¡Dato guardado localmente! Conectando con Google...")

# --- MOSTRAR LOS DATOS ACUMULADOS ---
if 'db' in st.session_state:
    st.write("### 📁 Tu Base de Datos Histórica")
    df_visual = pd.DataFrame(st.session_state.db)
    st.dataframe(df_visual)
    
    # Botón para descargar a Excel real
    csv = df_visual.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar Excel (.csv)", csv, "datos_wayne.csv", "text/csv")

st.info("💡 Siguiente paso: Configurar 'Secrets' en Streamlit para el guardado automático en Google Sheets.")
