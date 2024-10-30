import streamlit as st
import math

# Función para calcular el área de una circunferencia
def calcular_area(radio):
    return math.pi * radio ** 2

# Función para calcular el perímetro de una circunferencia
def calcular_perimetro(radio):
    return 2 * math.pi * radio

# Título de la aplicación
st.title("Cálculo de Área y Perímetro de una Circunferencia")

# Solicitar al usuario que ingrese el radio
radio = st.number_input("Ingrese el radio de la circunferencia:", min_value=0.0, step=0.1)

# Botón para realizar el cálculo
if st.button("Calcular"):
    if radio > 0:
        # Calcular área y perímetro
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)
        
        # Mostrar resultados
        st.write(f"**Área de la circunferencia:** {area:.2f}")
        st.write(f"**Perímetro de la circunferencia:** {perimetro:.2f}")
    else:
        st.error("Por favor, ingrese un radio mayor a 0.")
