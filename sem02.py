import streamlit as st

#INICIALIZACIÓN DE LAS VARIABLES PARA LA SUMA Y EL CONTADOR DE NUMEROS
sum = 0
contador = 0

# Titulo de la aplicación

st.title("Calculadora de suma y media de numeros");

#Explicación para el usuario
st.write("Introduce numeros uno a uno.Para Terminar, introduce el número 0")


#Crear un espacio de almacenamiento

if 'suma' not in st.session_state:
  st.session_state.suma = 0
  st.session_state.contador =0

  # Campo de entrada para el número

numero = st.number_input("Introduce un número:" , step= 1.0)

#Botón para agregar el numero

if st.button("Añadir número"):
  if numero !=0:
    #Acumular suma y contar el numero de entradas
    st.session_state.suma +=numero
    st.session_state.contador +=1
    st.success(f"Numero anadido: {numero}")
  else:
    if st.session_state.contador >0:
      media = st.session_state.suma / st.session_state.contador
      st.write(f"La suma de los numeros es: {st.session_state.suma}")
      st.write(f"La media de los numeros es : {media:.2f}")
    else:
      st.write("No se ha ingresado numeros validos")
      
      #Reiniciar la sesion

      st.session_state.suma =0
      st.session_state.contador=0

 #Mostrar la suma y el conteo en tiempo real

 st.write(f"Suma acumulada : {st.session_state.suma}")
 st.write(f"Numeros ingresados : {st.session_state.contador}")     




