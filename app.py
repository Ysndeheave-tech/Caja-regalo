import streamlit as st
import random
from PIL import Image

# --- ESTILO ROCKSTAR / BRUTALISTA ---
st.set_page_config(page_title="Cajita Rockstar", page_icon="⚡")

st.markdown("""
    <style>
    /* Fondo oscuro y profundo */
    .stApp { background: #0A0A0A; }
    
    /* Eliminar espacios en blanco y bordes suaves */
    [data-testid="stVerticalBlock"] { gap: 0rem; }
    
    .stMarkdown, .stButton, .stVideo {
        background-color: #1A1A1A;
        border: 3px solid #FF00FF; /* Contraste neón */
        padding: 20px;
        margin: 5px;
    }
    
    h1 { 
        color: #FFFFFF; 
        font-family: 'Impact', sans-serif; 
        text-transform: uppercase;
        letter-spacing: -2px;
        text-shadow: 5px 5px #FF00FF;
    }
    
    .stButton>button { 
        background-color: #FF00FF; 
        color: #000; 
        border: none;
        width: 100%; 
        padding: 25px; 
        font-size: 24px; 
        font-weight: 900;
        text-transform: uppercase;
        cursor: crosshair;
    }
    
    /* Quitar espacios de los contenedores */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("⚡ CAJITA DE PODER ⚡")

# --- MÚSICA (Sin adornos) ---
st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL")

# --- GALERÍA (Más compacta) ---
col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    pass

# --- BOTÓN ---
if st.button("¡PRESIONA Y RECLAMA!"):
    mensajes = [
        "Eres una persona increíble.", "Tu vibra es única.",
        "Gracias por ser mi cómplice.", "El mundo no está listo para nosotras.",
        "No te rindas, que se jodan todos", "Te amo, loca",
        "Sos la verdadera protagonista", "Siempre firme para vos",
        "Sos el amor de mi vida", "Te extraño cada día",
        "A llorar juntas, que es más rock", "Gracias por existir",
        "Sos mi otra mitad", "Te quiero mucho", "Sos la salsa de mis tacos",
        "Amo compartir neurona contigo", "Conocerte fue un golpe de suerte",
        "Sos mi persona favorita", "Te mereces lo mejor",
        "Eres lo más importante"
    ]
    st.success(random.choice(mensajes))
