import streamlit as st

# Inicialización de la lista para almacenar los números
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Título de la aplicación
st.title("Contador de Números en un Array")

# Ingreso del tamaño del array
tamaño = st.number_input("Ingrese el tamaño del array (número entero positivo):", min_value=1, step=1)

# Ingreso de los números
if tamaño > 0:
    st.write(f"Ingrese {tamaño} números:")
    for i in range(tamaño):
        numero = st.number_input(f"Número {i + 1}:", key=i)  # Uso de 'key' para que cada input tenga un identificador único
        st.session_state.numeros.append(numero)

# Botón para buscar el número en el array
buscar = st.number_input("Ingrese un número a buscar:", step=1.0)

if st.button("Buscar"):
    if st.session_state.numeros:
        # Contar cuántas veces aparece el número buscado en el array
        conteo = st.session_state.numeros.count(buscar)
        st.write(f"El número {buscar} se encontró {conteo} vez/veces en el array.")
    else:
        st.write("No se han ingresado números en el array.")
