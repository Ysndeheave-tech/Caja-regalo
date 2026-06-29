import streamlit as st
import random
from PIL import Image

# --- CONFIGURACIÓN ESTÉTICA ---
st.set_page_config(page_title="Nuestros Recuerdos", page_icon="💖")
st.markdown("""
    <style>
    .stApp { background-color: #FCE4EC; }
    h1 { color: #880E4F; text-align: center; }
    .stButton>button { background-color: #E91E63; color: white; border-radius: 20px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("💖 Nuestra Cajita de Recuerdos")

# --- MÚSICA ---
# Cambia el link de abajo por el de tu canción favorita en YouTube
st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL") 

st.write("---")

# --- GALERÍA DE 3 FOTOS ---
# Dividimos la pantalla en 3 columnas iguales
col1, col2, col3 = st.columns(3)

with col1:
    st.image(Image.open("Picture.jpg"), use_container_width=True)
with col2:
    st.image(Image.open("Picture2.jpg"), use_container_width=True)
with col3:
    st.image(Image.open("Picture3.jpg"), use_container_width=True)

st.write("---")

# --- MENSAJE SORPRESA ---
if st.button("¡Presiona para una sorpresa!"):
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
    "Eres de lo más importante que tengo"
    ]
    st.balloons()
    st.success(random.choice(mensajes))
