import streamlit as st

#Inicialización de la lista para almacenar los numeros

if 'numeros' not in st.session_state:
    st.session_state.numeros = []

# Titulo de la aplicacion
    
    st.title("Contador de Números en un array")

#Ingreso del tamaño del array

tamaño = st.number_input("Ingrese el tamaño del array(numero entero positivo):", min_value=1,step=1)

#Ingreso de los numero

if tamaño > 0:
    st.write(f"Ingrese {tamaño} numeros:")
    for i in range(tamaño):
        numero= st.number_input(f"Numero{i+1}:", key=i) #Uso de 'Key' para que cada input tenga un identidicador unico
        st.session_state.numeros.append(numero)

buscar = st.number_input("Ingrese un numero a buscar:", step=1.0)

if st.button("Buscar"):
    if st.session_state.numeros:
        #Contar cuantas veces aparece el numero buscado en el array
        conteo= st.session_state.numeros.count(buscar)
        st.write(f"El numero {buscar} se encontro {conteo} vez/veces en el array")
    else:
        st.write("No se han ingresado numeros en el array")