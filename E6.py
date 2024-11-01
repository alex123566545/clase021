import streamlit as st

#Inicialización de variables de sesión para la suma y el conteo de numeros

if 'puntos_contaminantes' not in st.session_state:
    st.session_state.puntos_contaminantes = []

# Titulo de la aplicación 

st.title("Centro de verificación de automoviles")

# Campo de entrada para los puntos contaminantes
puntos = st.number_input("Ingrese los puntos contaminates del automovil:", step=1.0, min_value=0.0)

#Boton para añadir  los puntos contaminantes 

if st.button("Anadir Automovil"):
    if puntos > 0: # Aseguramos que se añada solo si el punto es mayor a cero
       st.session_state.puntos_contaminantes.append(puntos)
       st.session_state(f"Número añadido:{puntos}" )
    else:
        st.warning("Por favor, ingrese un número positivo")
# Boton para calcular y mostrar resultados

if st.button("Calcular resultados"):
    if st.session_state.puntos_contaminantes: #Verificar si hay  datos ingresados
        promedio= sum(st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        max_contaminacion = max(st.session_state.puntos_contaminantes)
        min_contaminacion = min(st.session_state.puntos_contaminantes)

        #Mostrar resultados

        st.write(f"**Promedio de puntos contaminantes:** {promedio:.2f}")
        st.write(f"**Puntos contaminantes del automovil que menos contaminos** {min_contaminacion}")
        st.write(f"**Puntos contaminantes del automovil que mas contamino** {max_contaminacion}")
    else:
        st.write("No se han ingresado datos validos")

# Mostrar lista de automoviles ingresados

st.write("**Puntos contaminantes ingresados**")
st.write(st.session_state.puntos_contaminantes)