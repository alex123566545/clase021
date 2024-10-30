import streamlit as st

def calcular_multiplos(x):
    multiplos = [i for i in range(0,101) if i % x == 0]
    cantidad = len(multiplos)
    sumatoria = sum(multiplos)
    return multiplos, cantidad, sumatoria

st.title("Multiplos de un número entre 0  y  100")
x = st.number_input("Ingresa el valor de X : ", min_value=1, step = 1)

multiplos, cantidad, sumatoria = calcular_multiplos(x)
st.write(f"Array de multiplos de {x} entre 0 y 100: {multiplos}")
st.write(f"Cantidad de datos almacenados: {cantidad}")
st.write(f"Sumatoria de los datos del array :{sumatoria}")

