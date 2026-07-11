import streamlit as st
import random
from PIL import Image

# --- CONFIGURACIÓN ESTÉTICA ---
st.set_page_config(page_title="Cajita Rockstar", page_icon="⚡")

st.markdown("""
    <style>
    /* Fondo oscuro */
    .stApp { background-color: #0A0A0A; }
    
    /* Eliminar bordes y fondos de los contenedores automáticos */
    .stMarkdown, .stButton, .stVideo, .stImage {
        background-color: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    
    h1 { 
        color: #FFFFFF; 
        font-family: 'Impact', sans-serif; 
        text-transform: uppercase;
        text-align: center;
        text-shadow: 4px 4px #FF00FF;
        margin-top: 20px;
    }
    
    /* Botón Rockstar Centrado */
    div.stButton > button {
        background-color: #FF00FF;
        color: #000;
        border: 4px solid #FFF;
        padding: 20px 40px;
        font-size: 24px;
        font-weight: 900;
        text-transform: uppercase;
        display: block;
        margin: 0 auto; /* Esto centra el botón */
    }
    </style>
    """, unsafe_allow_html=True)

# --- TÍTULO Y VIDEO ---
st.title("⚡ CAJITA DE PODER ⚡")
st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL")

# --- GALERÍA ---
col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    pass

# --- BOTÓN ---
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("¡PRESIONA Y RECLAMA!"):
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
    st.success(random.choice(mensajes))
