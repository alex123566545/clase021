import streamlit as st

#Inicialización de la lista para almacenar los numeros

if 'numeros' not in st.session_state:
    st.session_state.numeros = []

#Titulo de la aplicación
st.title("Encontrar el mayor de un array")

#Ingreso del tamaño del array

tamaño = st.number_input("Ingrese el tamaño del array (numero entero positivo):", min_value=1,step=1)

#Ingreso de los numeros

if tamaño > 0:
    st.write(f"Ingrese {tamaño} numeros")
    for i in range(tamaño):
        numero = st.number_input(f"Numero {i + 1}:", key=i) 
        st.session_state.numeros.append(numero)

#Boton para determinar el numero mayor

if st.button('Encontrar Mayor'):
    if st.session_state.numeros:
        mayor= max(st.session_state.numeros) 
        st.write(f"El numero mayor ingresado es : {mayor}")
    else:
        st.write("No se han ingresado numeros en el array")