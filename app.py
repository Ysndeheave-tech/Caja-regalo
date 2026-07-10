import streamlit as st
import random
from PIL import Image

# --- CONFIGURACIÓN ESTÉTICA MAXIMALISTA ---
st.set_page_config(page_title="Nuestra Cajita de Poder", page_icon="💜")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #E1BEE7 0%, #4A148C 100%); }
    .stMarkdown, .stButton {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 40px;
        border: 6px solid #FF00FF;
        box-shadow: 12px 12px 0px #000;
        margin-bottom: 20px;
    }
    h1 { color: #FF00FF; text-align: center; font-family: 'Impact'; text-shadow: 4px 4px #000; }
    .stButton>button { 
        background-color: #4A148C; color: white; border-radius: 50px; 
        width: 100%; padding: 25px; font-size: 26px; font-weight: 900;
        border: 4px solid #FF00FF; box-shadow: 6px 6px 0px #FF00FF;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ CAJITA DE PODER Y AMOR ✨")
st.markdown("<h2 style='text-align: center; color: white;'>💜 📸 🎵 🌸 🎀 🦄 💖</h2>", unsafe_allow_html=True)

# MÚSICA
st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL")

# GALERÍA DE FOTOS
st.markdown("### 🖼️ NUESTROS MOMENTOS")
col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    st.error("¡Recuerda subir tus 3 fotos!")

# BOTÓN CON TODOS LOS MENSAJES
if st.button("¡PRESIONA PARA LA MAGIA! 💖"):
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
        "Sos mi persona favorita",
        "Te mereces solo lo mejor",
        "Eres de lo más importante que tengo"
    ]
    st.balloons()
    st.success(random.choice(mensajes))

# FOOTER LLENADOR
st.markdown("<h1 style='font-size: 60px;'>🌟✨💜🌈🎀🦄💖🌸⚡</h1>", unsafe_allow_html=True)
