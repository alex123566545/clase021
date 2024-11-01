import streamlit as st

#Titulo de la aplicación 
st.title("Suma de los elementos de la serie Numerica")

# Explicación para el usuario

st.write ("Esta aplicacion calcula la suma de los primeros n elementos de la series numerica : 1, 5, 3, 7, 5, 9, 7,...")

# Campo de entrada para el numero de elementos

n = st.number_input("Ingrese el valor de n (debe ser un número entero positivo):", min_value=1,step=1)

# Funcion para calcular la suma de la serie

def calcular_suma(n):
    serie = []
    for i in range(n):
        if i % 2 == 0: # Indices pares {0,2,4,...}
           serie.append(1  + (i//2)*2) # 1,3,5,7,..
        else : #Indices impares (1,3,5,...)
            serie.append(5 + (i//2)*2) #5,7,9....

    return sum(serie)


#Boton para calcular la suma
if st.button("calcular suma"):
    if n>0: #Validación
       suma = calcular_suma(n)
       st.write(f"La suma de los primeros {n} elementos de la series es : {suma}")
    else:
        st.warning("Por favor, ingrese un número entero positivo")
