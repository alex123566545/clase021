import streamlit as st

#Inicialización de la lista para almacenar los puntos

if 'numeros' not in st.session_state:
    st.session_state.numeros = []

#Titulo de la aplicación
st.title("Registro de numeros")

#Explicación para el usuario

st.write("Ingrese números uno por uno y haga clic en Añadir numero para almacenarlos")

#Campo de entrada para los numeros

numero = st.number_input("Ingrese un número:", step=1.0)

#Boton para añadir el numero

if st.button("Añadir numero"):
    st.session_state.numeros.append(numero)
    st.success(f"Numero añadido:{numero}")

#Mostrar la lista de numeros ingresados

st.write("**Numeros ingresados**")
st.write(st.session_state.numeros)

#Calcular y mostrar el porcentaje de pares e impares

if st.session_state.numeros:
    total_numeros = len(st.session_state.numeros)
    pares = sum(1 for n in st.session_state.numeros if n % 2 == 0)
    impares = total_numeros - pares


    porcentaje_pares = (pares/total_numeros)*100
    porcentaje_impares= (impares/total_numeros)*100

    #MOSTRAR RESULTADOS ESTADISTIICOS
    st.write(f"**Total de numeros ingresados:** {total_numeros}")
    st.write(f"**Numeros pares: ** {pares} ({porcentaje_pares:.2f}%)")
    st.write(f"**Numeros impares:** {impares}({porcentaje_impares:.2f}%)")
else:
    st.write("No se han ingresado numeros")