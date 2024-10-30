import streamlit as st

# Título de la aplicación
st.title("Suma de Elementos de la Serie Numérica")

# Explicación para el usuario
st.write("Esta aplicación calcula la suma de los primeros n elementos de la serie numérica: 1, 5, 3, 7, 5, 9, 7, ...")

# Campo de entrada para el número de elementos
n = st.number_input("Ingrese el valor de n (debe ser un número entero positivo):", min_value=1, step=1)

# Función para calcular la suma de la serie
def calcular_suma(n):
    serie = []
    for i in range(n):
        if i % 2 == 0:  # Índices pares (0, 2, 4, ...)
            serie.append(1 + (i // 2) * 2)  # 1, 3, 5, 7, ...
        else:  # Índices impares (1, 3, 5, ...)
            serie.append(5 + (i // 2) * 2)  # 5, 7, 9, ...
    return sum(serie)

# Botón para calcular la suma
if st.button("Calcular suma"):
    if n > 0:  # Validación
        suma = calcular_suma(n)
        st.write(f"La suma de los primeros {n} elementos de la serie es: {suma}")
    else:
        st.warning("Por favor, ingrese un número entero positivo.")
