import streamlit as st
import math

def calcular_area(radio):
    return math.pi * radio ** 2

def calcular_perimetro(radio):
    return 2 * math.pi * radio

st.title("Calculo de Area y Perimetro de una circunferencia")

radio = st.number_input("Ingrese el radio de la circunferencia", min_value= 0.0, step = 0.1)

if st.button("calcular"):
    if radio > 0:
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)

        st.write(f"**Area de la circunferencia:** {area:.2f}")
        st.write(f"**Perimetro de la circunferencia:** {perimetro:.2f}")
    else:
        st.error("Ingrese un readio mayor a ")