import streamlit as st
import random

# --- 1. CONFIGURACIÓN DE ESTILOS (Colores) ---
st.markdown("""
    <style>
    /* Color de fondo de toda la página */
    .stApp {
        background-color: #FCE4EC;
    }
    /* Estilo para los textos */
    h1 {
        color: #4A148C;
        text-align: center;
    }
    /* Estilo del botón */
    div.stButton > button {
        background-color: #E91E63;
        color: white;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EL PROGRAMA ---
st.title("💖 Cajita de Sorpresas")
st.write("Presiona el botón para recibir algo especial hoy:")

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

if st.button("¡Haz clic aquí!"):
    sorpresa = random.choice(mensajes)
    st.balloons() 
    st.success(sorpresa)
