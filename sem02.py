import streamlit as st

# Inicialización de la lista para almacenar los números
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Título de la aplicación
st.title("Encontrar el Mayor de un Array")

# Ingreso del tamaño del array
tamaño = st.number_input("Ingrese el tamaño del array (número entero positivo):", min_value=1, step=1)

# Ingreso de los números
if tamaño > 0:
    st.write(f"Ingrese {tamaño} números:")
    for i in range(tamaño):
        numero = st.number_input(f"Número {i + 1}:", key=i)  # Uso de 'key' para que cada input tenga un identificador único
        st.session_state.numeros.append(numero)

# Botón para determinar el número mayor
if st.button("Encontrar Mayor"):
    if st.session_state.numeros:
        mayor = max(st.session_state.numeros)  # Encuentra el número mayor
        st.write(f"El número mayor ingresado es: {mayor}")
    else:
        st.write("No se han ingresado números en el array.")
