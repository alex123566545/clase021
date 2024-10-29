import streamlit as st

# Función para calcular múltiplos de X entre 0 y 100
def calcular_multiplos(x):
    # Generar lista de múltiplos de x entre 0 y 100
    multiplos = [i for i in range(0, 101) if i % x == 0]
    # Calcular cantidad y sumatoria
    cantidad = len(multiplos)
    sumatoria = sum(multiplos)
    return multiplos, cantidad, sumatoria

# Interfaz de Streamlit
st.title("Múltiplos de un número entre 0 y 100")

# Input para que el usuario ingrese el valor de X
x = st.number_input("Ingresa el valor de X:", min_value=1, step=1)

# Botón para calcular
if st.button("Calcular"):
    multiplos, cantidad, sumatoria = calcular_multiplos(x)
    st.write(f"Array de múltiplos de {x} entre 0 y 100: {multiplos}")
    st.write(f"Cantidad de datos almacenados: {cantidad}")
    st.write(f"Sumatoria de los datos del array: {sumatoria}")


if __name__ == "__main__":
    main()