import streamlit as st
import random
from PIL import Image

# --- CONFIGURACIÓN ESTÉTICA MAXIMALISTA ---
st.set_page_config(page_title="Nuestra Vibra Lila", page_icon="💜")

st.markdown("""
    <style>
    /* Fondo vibrante lila */
    .stApp { 
        background: radial-gradient(circle, #E1BEE7 0%, #7B1FA2 100%); 
    }
    
    /* Tarjetas con bordes súper redondeados y sombras pesadas */
    .css-1r6slb0, .stMarkdown { 
        background-color: rgba(255, 255, 255, 0.9); 
        padding: 30px; 
        border-radius: 40px; 
        border: 4px solid #4A148C;
        box-shadow: 15px 15px 0px #4A148C;
        margin-bottom: 20px;
    }
    
    h1 { 
        color: #4A148C; 
        text-align: center; 
        font-family: 'Impact', sans-serif; 
        font-size: 3.5rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Botón maximalista */
    .stButton>button { 
        background-color: #FF00FF; 
        color: white; 
        border-radius: 50px; 
        width: 100%; 
        padding: 20px; 
        font-size: 24px; 
        border: 4px solid #000;
        box-shadow: 8px 8px 0px #000;
        font-weight: 900;
    }
    .stButton>button:hover { background-color: #CC00CC; transform: translate(-2px, -2px); }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.title("✨ CAJITA DE PODER ✨")

# MÚSICA CON MARCO
st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL")

st.markdown("<br>", unsafe_allow_html=True)

# --- GALERÍA ESTILO POLAROID ---
col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    st.error("¡Recuerda revisar que las fotos estén en la carpeta principal!")

st.markdown("<br>", unsafe_allow_html=True)

# --- BOTÓN ---
_, c_boton, _ = st.columns([1, 2, 1])
with c_boton:
    btn = st.button("¡PRESIONA Y BRILLA!")

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
