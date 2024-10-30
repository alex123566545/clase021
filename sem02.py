import streamlit as st

# Inicialización de la lista para almacenar los números
if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Título de la aplicación
st.title("Registro de Números")

# Explicación para el usuario
st.write("Ingrese números uno por uno y haga clic en 'Añadir número' para almacenarlos.")

# Campo de entrada para los números
numero = st.number_input("Ingrese un número:", step=1.0)

# Botón para añadir el número
if st.button("Añadir número"):
    st.session_state.numeros.append(numero)
    st.success(f"Número añadido: {numero}")

# Mostrar la lista de números ingresados
st.write("**Números ingresados:**")
st.write(st.session_state.numeros)

# Calcular y mostrar el porcentaje de pares e impares
if st.session_state.numeros:
    total_numeros = len(st.session_state.numeros)
    pares = sum(1 for n in st.session_state.numeros if n % 2 == 0)
    impares = total_numeros - pares

    porcentaje_pares = (pares / total_numeros) * 100
    porcentaje_impares = (impares / total_numeros) * 100

    # Mostrar resultados estadísticos
    st.write(f"**Total de números ingresados:** {total_numeros}")
    st.write(f"**Números pares:** {pares} ({porcentaje_pares:.2f}%)")
    st.write(f"**Números impares:** {impares} ({porcentaje_impares:.2f}%)")
else:
    st.write("No se han ingresado números.")
