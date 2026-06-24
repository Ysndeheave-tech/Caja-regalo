import streamlit as st
import random
from PIL import Image

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Para mi amiguita", page_icon="💖")

st.markdown("""
    <style>
    .stApp { background-color: #FCE4EC; }
    h1 { color: #880E4F; text-align: center; }
    .stButton>button {
        background-color: #E91E63;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 18px;
        margin: auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONTENIDO ---
st.title("💖 Cajita de Sorpresas")

# AQUÍ CAMBIA EL NOMBRE DEL ARCHIVO SI ES DIFERENTE
try:
    img = Image.open("mi_foto.jpg") 
    st.image(img, use_container_width=True)
except:
    st.warning("¡Sube tu foto a GitHub con el nombre 'mi_foto.jpg' para que se vea!")

st.write("---")
st.markdown("<p style='text-align: center;'>Presiona el botón para recibir algo especial hoy:</p>", unsafe_allow_html=True)

# --- 3. BOTÓN ---
if st.button("¡Haz clic aquí!"):
    mensajes = [
        "¡Eres una persona increíble!",
    "Tu sonrisa alegra el día de cualquiera.",
    "Gracias por ser mi amiga.",
    "Eres única, nunca lo olvides.",
    "No te rindas, los hombres tienen que seguir pelandotela",
    "Te amo mi loca",
    "Por vos me hago lesbiana",
    "Estoy siempre para vos",
    "Sos el amor de mi vida",
    "Te extraño todos los días",
    "No hay nada que una lloradita juntas no arregle",
    "Gracias por existir",
    "Sos mi otra mitad",
    "Te quiero mucho",
    "Sos la salsa de mis tacos",
    "Amo compartir neurona contigo",
    "Conocerte es de las mejores cosas que me pasaron",
    "Sos mi persona favorita"
    "Te mereces solo lo mejor",
    "Eres de lo más importante que tengo",
    ]
    st.balloons()
    st.success(random.choice(mensajes))

# --- 4. MÚSICA ---
st.write("---")
st.markdown("<h3 style='text-align: center;'>Nuestra canción 🎵</h3>", unsafe_allow_html=True)
# AQUÍ CAMBIA EL LINK POR TU CANCIÓN
st.video("TU_LINK_DE_YOUTUBE_AQUI")
