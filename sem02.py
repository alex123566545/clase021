import streamlit as st

# Inicialización de variables para la suma y el contador de números
suma = 0
contador = 0

# Título de la aplicación
st.title("Calculadora de Suma y Media de Números")

# Explicación para el usuario
st.write("Introduce números uno a uno. Para terminar, introduce el número 0.")

# Crear un espacio de almacenamiento en la sesión
if 'suma' not in st.session_state:
    st.session_state.suma = 0
    st.session_state.contador = 0

# Campo de entrada para el número
numero = st.number_input("Introduce un número:", step=1.0)

# Botón para agregar el número
if st.button("Añadir número"):
    if numero != 0:
        # Acumular suma y contar el número de entradas
        st.session_state.suma += numero
        st.session_state.contador += 1
        st.success(f"Número añadido: {numero}")
    else:
        # Cálculo y muestra de la suma y la media
        if st.session_state.contador > 0:
            media = st.session_state.suma / st.session_state.contador
            st.write(f"La suma de los números es: {st.session_state.suma}")
            st.write(f"La media de los números es: {media:.2f}")
        else:
            st.write("No se han ingresado números válidos.")
        
        # Reiniciar la sesión
        st.session_state.suma = 0
        st.session_state.contador = 0

# Mostrar la suma y el conteo en tiempo real
st.write(f"Suma acumulada: {st.session_state.suma}")
st.write(f"Números ingresados: {st.session_state.contador}")
