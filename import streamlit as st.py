import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURACIÓN GENERAL Y ESTILO "TECH"
st.set_page_config(page_title="Pase Tech Global Solutions", layout="wide", initial_sidebar_state="collapsed", page_icon="🌐")

# Estilo Dark Mode y acentos de color profesionales
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #E0E0E0; }
    .stTabs [data-baseweb="tab"] { color: #4CAF50; font-weight: bold; font-size: 16px; } /* Verde para tabs */
    .stMetric { background-color: #1E1E1E; border: 1px solid #4CAF50; padding: 10px; border-radius: 8px; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; } /* Botones verdes */
    h1, h2, h3, h4, h5, h6 { color: #E0E0E0; }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO Y SLOGAN
st.title("🌐 PASE TECH GLOBAL SOLUTIONS")
st.subheader("Innovación y Datos para un Futuro Mejor")
st.caption(f"Última Actualización: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# 3. PANTALLA DE INICIO: QUIÉNES SOMOS
# Creamos una sesión para controlar qué pantalla se muestra
if 'show_intro' not in st.session_state:
    st.session_state.show_intro = True

if st.session_state.show_intro:
    st.write("---")
    st.header("💡 Quiénes Somos: Liderando la Innovación")
    col_intro1, col_intro2 = st.columns([1, 2])

    with col_intro1:
        st.image("https://images.unsplash.com/photo-1517048676732-c625af101037?auto=format&fit=crop&q=80&w=600", caption="Nuestro equipo visionario (imagen placeholder)")
        st.write("**Nuestra Misión:** Transformar ideas complejas en soluciones accesibles y eficientes. En Pase Tech, creemos en el poder de la tecnología para optimizar cada aspecto de la vida moderna, desde la inversión inmobiliaria hasta la exploración espacial.")
    
    with col_intro2:
        st.subheader("Nuestras Áreas de Experiencia")
        st.markdown("""
        - **Desarrollo de Software a Medida:** Creamos aplicaciones web y herramientas de análisis de datos.
        - **Consultoría Tecnológica:** Asesoramos a empresas y particulares en la optimización de sus procesos.
        - **Investigación y Desarrollo:** Exploramos nuevas fronteras en IA, Biotecnología y Automatización.
        """)
        st.write("Con un equipo joven y dinámico, estamos comprometidos con la excelencia y la vanguardia tecnológica.")
        if st.button("Explorar Nuestros Servicios"):
            st.session_state.show_intro = False
    st.write("---")
else: # Una vez que se cierra la intro, se muestra la navegación
    # 4. SISTEMA DE NAVEGACIÓN PRINCIPAL
    tabs = st.tabs([
        "🏡 INMUEBLES",
        "🛡️ CIBERSEGURIDAD",
        "🚗 MOVILIDAD AVANZADA",
        "🔬 BIOTECNOLOGÍA",
        "🚀 ESPACIO"
    ])

    # --- SECCIÓN 1: INMUEBLES ---
    with tabs[0]:
        st.header("Análisis de Mercado Inmobiliario")
        tipo_propiedad = st.selectbox("Tipo de Propiedad", ["Apartamento", "Casa", "Oficina", "Terreno"])
        barrio_inmueble = st.selectbox("Barrio de Interés", ["Pocitos", "Carrasco", "Cordón", "Centro", "Malvín"])
        
        col_inm1, col_inm2 = st.columns(2)
        with col_inm1:
            precio_base = {"Apartamento": 120000, "Casa": 250000, "Oficina": 180000, "Terreno": 90000}[tipo_propiedad]
            precio_ajustado = precio_base + (random.randint(-10000, 10000) if barrio_inmueble != "Carrasco" else 30000)
            
            st.metric(f"Valor Estimado ({barrio_inmueble})", f"USD {precio_ajustado:,.0f}")
            m2_estimado = precio_ajustado / random.randint(40, 150)
            st.metric("Precio por m²", f"USD {m2_estimado:.0f}")

        with col_inm2:
            st.subheader("Mapa Interactivo")
            st.map(pd.DataFrame({'lat': [-34.90 + random.random()/50], 'lon': [-56.16 + random.random()/50]}))
            if st.button("Ver Reporte Detallado"):
                st.info(f"Generando reporte para {tipo_propiedad} en {barrio_inmueble}...")

    # --- SECCIÓN 2: CIBERSEGURIDAD ---
    with tabs[1]:
        st.header("Pase Tech Cyber-Defense")
        sistema_a_escanear = st.text_input("Ingresar IP o URL para Escaneo de Seguridad:", "192.168.1.1")
        
        if st.button("Iniciar Escaneo de Vulnerabilidades"):
            with st.spinner('Escaneando el sistema...'):
                import time
                time.sleep(2) # Simula un escaneo
            
            vulnerabilidades = ["Puerto 80 Abierto", "Versión de Apache Antigua", "Credenciales Débiles"]
            if random.random() < 0.7: # Simula que a veces encuentra vulnerabilidades
                st.error("🚨 ¡Vulnerabilidades Encontradas! 🚨")
                for v in random.sample(vulnerabilidades, k=random.randint(1, len(vulnerabilidades))):
                    st.write(f"- {v}")
            else:
                st.success("✅ Escaneo Completo: No se encontraron vulnerabilidades críticas.")
            st.write("Nivel de Amenaza Global: **MODERADO**")

    # --- SECCIÓN 3: MOVILIDAD AVANZADA ---
    with tabs[2]:
        st.header("Pase Tech Motors: Diseña tu Vehículo")
        modelo_vehiculo = st.selectbox("Modelo Base", ["Urbano Compacto", "SUV Eléctrico", "Deportivo Híbrido", "Vehículo Autónomo"])
        color_vehiculo = st.color_picker("Elige el Color Principal", "#FF4B4B")
        potencia_motor = st.slider("Potencia del Motor (HP)", 100, 1000, 300)
        
        st.subheader("Tu Diseño Personalizado:")
        col_car1, col_car2 = st.columns(2)
        with col_car1:
            st.write(f"**Modelo:** {modelo_vehiculo}")
            st.write(f"**Color:** {color_vehiculo}")
            st.write(f"**Potencia:** {potencia_motor} HP")
            velocidad_max = (potencia_motor / 5) + random.randint(0, 50)
            st.metric("Velocidad Máxima Est.", f"{velocidad_max:.0f} km/h")
        with col_car2:
            # Aquí pondríamos una imagen del auto diseñado, por ahora una genérica
            st.image("https://images.unsplash.com/photo-1583121920703-a162232a5147?auto=format&fit=crop&q=80&w=400", caption=f"Prototipo {modelo_vehiculo} en color {color_vehiculo}")
            if st.button("Generar Planos 3D"):
                st.success("Planos 3D enviados a tu correo. ¡Tu vehículo futurista está listo!")

    # --- SECCIÓN 4: BIOTECNOLOGÍA ---
    with tabs[3]:
        st.header("Pase Tech Bio-Lab: Investigación Avanzada")
        tipo_investigacion = st.radio("Foco de Investigación:", ["Farmacología", "Secuenciación Genética", "Nutrición Personalizada"])
        
        if tipo_investigacion == "Farmacología":
            dosis = st.slider("Dosis del Compuesto (mg)", 1, 100, 25)
            eficacia = 50 + (dosis * 0.5) + random.randint(-5, 5)
            st.metric("Eficacia Potencial", f"{eficacia:.1f}%")
            if eficacia > 75: st.success("¡Resultados prometedores! Continuando fases de prueba.")
            else: st.info("Se requiere más investigación para optimizar la fórmula.")
            st.line_chart([random.uniform(0.1, 1.0) for _ in range(10)]) # Grafico de actividad
        
        elif tipo_investigacion == "Secuenciación Genética":
            secuencia_adn = st.text_area("Ingresar Secuencia de ADN (ej. ATGC...)", "ATGCGTAACTGG")
            if st.button("Analizar Secuencia"):
                st.write(f"Análisis de {len(secuencia_adn)} bases. Riesgo de mutación: {random.uniform(0.1, 5.0):.2f}%")
                st.bar_chart([random.random() for _ in range(5)])
        
        else: # Nutrición Personalizada
            calorias = st.number_input("Objetivo de Calorías Diarias", 1500, 3000, 2000)
            proteinas = calorias * 0.25 / 4 # Ejemplo: 25% calorías de proteína
            st.write(f"Recomendación para {calorias} kcal:")
            st.write(f"- Proteínas: {proteinas:.0f} g")
            st.write(f"- Carbohidratos: {(calorias * 0.55 / 4):.0f} g")
            st.write(f"- Grasas: {(calorias * 0.20 / 9):.0f} g")

    # --- SECCIÓN 5: ESPACIO ---
    with tabs[4]:
        st.header("Pase Tech Aerospace: Exploración Estelar")
        mision_espacial = st.selectbox("Seleccionar Misión", ["Orbital Terrestre", "Misión Lunar", "Exploración de Marte", "Observatorio de Exoplanetas"])
        
        col_esp1, col_esp2 = st.columns(2)
        with col_esp1:
            st.subheader("Estado de la Misión")
            combustible_restante = random.randint(50, 100)
            st.progress(combustible_restante, text=f"Combustible Restante: {combustible_restante}%")
            st.metric("Distancia Recorrida", f"{random.randint(100000, 5000000):,} km")
            if combustible_restante < 60:
                st.warning("⚠️ Nivel de combustible a monitorear.")
            
        with col_esp2:
            st.subheader("Actividad de Sensores")
            # Gráfico de actividad simulada
            actividad_sensores = [random.uniform(0.1, 1.0) for _ in range(20)]
            st.line_chart(actividad_sensores)
            if st.button("Enviar Comando a Satélite"):
                st.success("Comando 'Reconfigurar Órbita' enviado con éxito.")
            
        st.subheader("Próximos Lanzamientos (Global)")
        # Datos ficticios de lanzamientos futuros
        lanzamientos_futuros = {
            "Misión": ["Pase-Sat 2027", "Mars Cargo", "Lunar Outpost"],
            "Fecha": ["25/03/2027", "10/08/2027", "05/01/2028"],
            "Estado": ["Planificado", "En Desarrollo", "Concepto"]
        }
        st.table(pd.DataFrame(lanzamientos_futuros))

st.divider()
st.caption("Pase Tech Global Solutions © 2026 - Desarrollado en Montevideo.")

