import streamlit as st

# Inicialización de variables en el estado de la sesión
st.title("Ejercicios basicos con bucles") 

st.subheader("Ejercicio 1: imprimir hola mundo 9 veces")
if st.button("Ejecutar E1"):
    for i in range(10):
        st.write("hola mundo")