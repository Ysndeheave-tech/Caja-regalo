import streamlit as st
import random
from PIL import Image

# --- CONFIGURACIÓN CORRECTA ---
st.set_page_config(page_title="Cajita Rockstar", page_icon="⚡")

st.markdown("""
    <style>
    /* Fondo oscuro */
    .stApp { background-color: #0A0A0A !important; }
    
    /* Eliminar fondos automáticos y bordes */
    div[data-testid="stVerticalBlock"] {
        background-color: transparent !important;
    }
    
    h1 { 
        color: #FFFFFF !important; 
        font-family: 'Impact', sans-serif; 
        text-align: center;
        text-shadow: 4px 4px #FF00FF;
    }
    
    /* Centrado absoluto del botón */
    div.stButton {
        display: flex;
        justify-content: center;
    }
    
    button {
        background-color: #FF00FF !important;
        color: #000 !important;
        border: 4px solid #FFF !important;
        padding: 20px 40px !important;
        font-size: 24px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        cursor: crosshair !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.title("⚡ CAJITA DE PODER ⚡")

st.video("https://youtu.be/G-H7OS_Mrc8?si=9RKpL")

col1, col2, col3 = st.columns(3)
try:
    with col1: st.image(Image.open("Picture1.jpg"), use_container_width=True)
    with col2: st.image(Image.open("Picture2.jpg"), use_container_width=True)
    with col3: st.image(Image.open("Picture3.jpg"), use_container_width=True)
except:
    pass

# --- BOTÓN CENTRADO ---
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
    st.success(random.choice(mensajes))
