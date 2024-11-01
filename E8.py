import streamlit as st

# Inicialización de la lista para almacenar los números
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Título de la aplicación
st.title("Contador de Números en un Array")

# Ingreso del tamaño del array
tamaño = st.number_input("Ingrese el tamaño del array (número entero positivo):", min_value=1, step=1)

# Evita duplicar entradas al presionar "Buscar" varias veces
if 'array_lleno' not in st.session_state:
    st.session_state.array_lleno = False

# Ingreso de los números solo si el tamaño es mayor que cero y el array no está lleno
if tamaño > 0 and not st.session_state.array_lleno:
    st.write(f"Ingrese {tamaño} números:")
    
    # Limpiar la lista si el tamaño cambia
    if len(st.session_state.numeros) != tamaño:
        st.session_state.numeros = []
    
    # Recorrer el rango de tamaño ingresado para obtener los números
    for i in range(tamaño):
        numero = st.number_input(f"Número {i + 1}:", key=f'numero_{i}')  # Uso de 'key' para que cada input tenga un identificador único
        if len(st.session_state.numeros) < tamaño:
            st.session_state.numeros.append(numero)

    # Confirmar que el array está completo
    if len(st.session_state.numeros) == tamaño:
        st.session_state.array_lleno = True

# Campo para ingresar el número a buscar
buscar = st.number_input("Ingrese un número a buscar:", step=1.0)

# Botón para buscar el número en el array
if st.button("Buscar"):
    if st.session_state.numeros:
        # Contar cuántas veces aparece el número buscado en el array
        conteo = st.session_state.numeros.count(buscar)
        st.write(f"El número {buscar} se encontró {conteo} vez/veces en el array")
    else:
        st.write("No se han ingresado números en el array")
