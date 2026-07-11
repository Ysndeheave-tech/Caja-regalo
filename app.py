import streamlit as st
import random
from PIL import Image

# --- ESTILO ROCKSTAR / BRUTALISTA ---
st.set_page_config(page_title="Cajita Rockstar", page_icon="⚡")

st.markdown("""
    <style>
    /* Fondo oscuro profundo */
    .stApp { background-color: #0A0A0A; }
    
    /* Estilo de los bloques de contenido */
    .stMarkdown, .stButton, .stVideo {
        background-color: #1A1A1A;
        border: 3px solid #FF00FF; /* Contraste neón */
        padding: 20px;
        margin: 10px 0;
        border-radius: 0; /* Bordes rectos para un look brutalista */
    }
    
    h1 { 
        color: #FFFFFF; 
        font-family: 'Impact', sans-serif; 
        text-transform: uppercase;
        letter-spacing: -1px;
        text-shadow: 4px 4px #FF00FF;
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
        cursor: crosshair; /* Un detalle final rockstar */
    }
    </style>
    """, unsafe_allow_html=True)

# --- FONDO DE EMOJIS REPARTIDOS ---
# Esto llena todo el fondo con emojis a baja opacidad en lugar de puntos
st.markdown("""
    <div style='position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; 
                pointer-events: none; font-size: 35px; opacity: 0.1; line-height: 1.5;'>
        ⚡💀🎸🔥🤘⚡💀🎸🔥🤘⚡💀🎸🔥🤘⚡💀🎸🔥🤘⚡💀🎸🔥🤘⚡💀🎸🔥🤘⚡💀🎸🔥🤘⚡💀🎸🔥🤘
    </div>
""", unsafe_allow_html=True)

# --- CABECERA (Solo el título, sin los cuadros raros) ---
st.title("⚡ CAJITA DE PODER ⚡")

# --- MÚSICA ---
st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL")

# --- GALERÍA ---
col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    pass

# --- BOTÓN CENTRADO ---
_, c_boton, _ = st.columns([1, 2, 1])
with c_boton:
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
