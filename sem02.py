import streamlit as st

# Inicialización de variables
puntos_contaminantes = []

# Título de la aplicación
st.title("Centro de Verificación de Automóviles")

# Explicación para el usuario
st.write("Ingrese los puntos contaminantes de los automóviles.")

# Bucle para ingresar datos de los automóviles
while True:
    # Ingreso de puntos contaminantes
    puntos = st.number_input("Ingrese los puntos contaminantes del automóvil:", step=1.0, min_value=0.0)
    
    # Agregar el dato a la lista
    puntos_contaminantes.append(puntos)
    
    # Preguntar si se desea agregar otro automóvil
    continuar = st.radio("¿Desea ingresar los datos de otro automóvil?", ("Sí", "No"))
    
    if continuar == "No":
        break

# Procesamiento de datos
if puntos_contaminantes:  # Verificar si hay datos ingresados
    promedio = sum(puntos_contaminantes) / len(puntos_contaminantes)
    max_contaminacion = max(puntos_contaminantes)
    min_contaminacion = min(puntos_contaminantes)

    # Mostrar resultados
    st.write(f"**Promedio de puntos contaminantes:** {promedio:.2f}")
    st.write(f"**Puntos contaminantes del automóvil que menos contaminó:** {min_contaminacion}")
    st.write(f"**Puntos contaminantes del automóvil que más contaminó:** {max_contaminacion}")
else:
    st.write("No se han ingresado datos válidos.")
