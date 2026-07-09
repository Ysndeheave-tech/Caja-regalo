import streamlit as st
import random
from PIL import Image

# --- CONFIGURACIÓN ESTÉTICA ---
st.set_page_config(page_title="Nuestros Recuerdos", page_icon="💖")
st.markdown("""
    <style>
    /* Degradado suave para evitar el diseño plano */
    .stApp { 
        background: linear-gradient(135deg, #FCE4EC 0%, #FFFFFF 100%); 
    }
    h1 { color: #880E4F; text-align: center; font-family: 'Georgia', serif; }
    
    /* Botón con estilo moderno */
    .stButton>button { 
        background-color: #E91E63; 
        color: white; 
        border-radius: 50px; 
        padding: 10px 25px; 
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("💖 Nuestra Cajita de Recuerdos")

# --- MÚSICA ---
# Usamos un contenedor para centrar el video
c_video1, c_video2, c_video3 = st.columns([1, 4, 1])
with c_video2:
    st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL") 

st.write("---")

# --- GALERÍA DE 3 FOTOS ---
col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    st.error("Revisa que Picture1.jpg, Picture2.jpg y Picture3.jpg estén en la raíz de tu GitHub.")

st.write("---")

# --- MENSAJE SORPRESA (Botón Centrado) ---
# Creamos 5 columnas para que el botón en la 3ra quede perfecto
_, c_boton, _ = st.columns([2, 1, 2])
with c_boton:
    btn = st.button("¡Presiona para una sorpresa!")

if btn:
    mensajes = [
        "¡Eres una persona increíble!", "Tu sonrisa alegra el día de cualquiera.",
        "Gracias por ser mi amiga.", "Eres única, nunca lo olvides.",
        "No te rindas, los hombres tienen que seguir pelandotela", "Te amo mi loca",
        "Por vos me hago lesbiana", "Estoy siempre para vos",
        "Sos el amor de mi vida", "Te extraño todos los días",
        "No hay nada que una lloradita juntas no arregle", "Gracias por existir",
        "Sos mi otra mitad", "Te quiero mucho", "Sos la salsa de mis tacos",
        "Amo compartir neurona contigo", "Conocerte es de las mejores cosas que me pasaron",
        "Sos mi persona favorita", "Te mereces solo lo mejor",
        "Eres de lo más importante que tengo"
    ]
    st.balloons()
    st.success(random.choice(mensajes))
