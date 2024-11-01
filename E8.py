import streamlit as st

#Inicialización de la lista para almacenar los numeros

if 'numeros' not in st.session_state:
    st.session_state.numeros = []

import streamlit as st

# Inicialización de la lista para almacenar los números
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Título de la aplicación
st.title("Contador de Números en un Array")

# Ingreso del tamaño del array
tamaño = st.number_input("Ingrese el tamaño del array (número entero positivo):", min_value=1, step=1)

# Limpiar la lista si el tamaño cambia
if len(st.session_state.numeros) != tamaño:
    st.session_state.numeros = [None] * tamaño  # Crear una lista del tamaño especificado, inicialmente vacía

# Ingreso de los números solo si el tamaño es mayor que cero
if tamaño > 0:
    st.write(f"Ingrese {tamaño} números:")
    
    # Ingresar cada número con un campo individual
    for i in range(tamaño):
        numero = st.number_input(f"Número {i + 1}:", key=f'numero_{i}')
        st.session_state.numeros[i] = numero  # Asignar cada número a la posición correspondiente en la lista

# Campo para ingresar el número a buscar
buscar = st.number_input("Ingrese un número a buscar:", step=1.0)

# Botón para buscar el número en el array
if st.button("Buscar"):
    # Contar cuántas veces aparece el número buscado en el array, excluyendo posiciones vacías
    conteo = st.session_state.numeros.count(buscar)
    st.write(f"El número {buscar} se encontró {conteo} vez/veces en el array") if conteo > 0 else st.write("El número no se encuentra en el array")
