import streamlit as st

# Inicialización de variables de sesión para la suma y el conteo de números
if 'puntos_contaminantes' not in st.session_state:
    st.session_state.puntos_contaminantes = []

# Título de la aplicación
st.title("Centro de Verificación de Automóviles")

# Explicación para el usuario
st.write("Ingrese los puntos contaminantes de los automóviles.")

# Campo de entrada para los puntos contaminantes
puntos = st.number_input("Ingrese los puntos contaminantes del automóvil:", step=1.0, min_value=0.0)

# Botón para añadir los puntos contaminantes
if st.button("Añadir automóvil"):
    if puntos > 0:  # Aseguramos que se añada solo si el punto es mayor a cero
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Número añadido: {puntos}")
    else:
        st.warning("Por favor, ingrese un número positivo.")

# Botón para calcular y mostrar resultados
if st.button("Calcular resultados"):
    if st.session_state.puntos_contaminantes:  # Verificar si hay datos ingresados
        promedio = sum(st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        max_contaminacion = max(st.session_state.puntos_contaminantes)
        min_contaminacion = min(st.session_state.puntos_contaminantes)

        # Mostrar resultados
        st.write(f"**Promedio de puntos contaminantes:** {promedio:.2f}")
        st.write(f"**Puntos contaminantes del automóvil que menos contaminó:** {min_contaminacion}")
        st.write(f"**Puntos contaminantes del automóvil que más contaminó:** {max_contaminacion}")
    else:
        st.write("No se han ingresado datos válidos.")

# Mostrar lista de automóviles ingresados
st.write("**Puntos contaminantes ingresados:**")
st.write(st.session_state.puntos_contaminantes)
