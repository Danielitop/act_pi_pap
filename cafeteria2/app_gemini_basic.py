import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="Tutor de Inglés con Gemini", layout="centered")
st.title("💬 atencion al cliente cafeteria")
st.markdown("Hola, soy tu asistente personal de café. ¡Cuéntame qué se te antoja hoy y te ayudaré a encontrar la bebida y el postre perfectos de nuestro menú!")

# # Interfaz de usuario
# prompt = st.text_input("¿Qué quieres aprender o practicar hoy?", placeholder="Ej. Explica el uso del 'Present Perfect' o Traduce 'perro' al inglés.")
# # prompt = st.chat_input("¿Qué quieres aprender o practicar hoy?")
# enviar = st.button("Obtener Ayuda")

prompt = st.chat_input("busquemos tus gustos")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

    # Lógica del tutor de inglés
    def generar_respuesta_tutor(pregunta):
        if not pregunta:
            return "Por favor, escribe una pregunta o tema para empezar."
        
        # Añadimos un "prompt de sistema" para guiar a Gemini
        prompt_con_contexto = f"Eres un asistente de servicio al cliente amable y experto en el menú de nuestra cafetería. Tu misión es ayudar al cliente a encontrar la bebida y postre perfectos. Comienza con un saludo, pregunta qué se le antoja y haz preguntas clave para entender sus gustos (dulce, amargo, frío, caliente, café, té). Basado en sus respuestas, sugiere productos específicos del menú con una breve descripción y pregunta si alguna opción le atrae. Finaliza la conversación de manera cordial. Tu tono debe ser siempre servicial y positivo.'{pregunta}'"
        
        try:
            # Aquí debes poner tu clave de API de Gemini
            client = genai.Client(api_key="AIzaSyD5rCZPweRBmiLgfbhqyfN4VB6YZa-Sv4Q") 
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=prompt_con_contexto
            )
            return response.text
        except Exception as e:
            return f"Lo siento, ocurrió un error: {str(e)}. Por favor, inténtalo de nuevo más tarde."

    # Lógica principal de la aplicación
    if prompt:
        with st.spinner("Buscando la mejor respuesta para la cafeteria..."):
            respuesta = generar_respuesta_tutor(prompt)
        st.subheader("Respuesta de tu Tutor:")
        st.info(respuesta)
    else:
        st.info("Escribe tu pregunta de la cafeteria y haz clic en 'Obtener Ayuda'.")