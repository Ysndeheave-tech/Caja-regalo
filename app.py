import streamlit as st
import random

# --- 1. CONFIGURACIÓN Y ESTILO ---
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
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONTENIDO CENTRADO ---
st.title("💖 Cajita de Sorpresas")
st.write("---") # Línea divisoria para que no se vea vacío
st.markdown("<p style='text-align: center;'>Presiona el botón para recibir algo especial hoy:</p>", unsafe_allow_html=True)

# --- 3. BOTÓN CENTRADO (usando columnas) ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    btn = st.button("¡Haz clic aquí!")

# --- 4. LÓGICA ---
if btn:
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
