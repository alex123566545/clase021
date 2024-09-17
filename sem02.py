import streamlit as st

#Inicialización de variables 
usuarios = []

#Función para agregar un usuario
def agregar_usuario(nombre):
    usuarios.append(nombre)
    st.success(f"Usuario {nombre} agregado.")

#Función para mostrar usuarios
def mostrar_usuarios():
    if usuarios:
        st.write("Lista de usuarios:")
        for usuarios in usuario:
            st.white(f"- {usuario}")
    else:
        st.warning("No hay usuarios registrados.")

#Menú Principal
st.title("Gestión de Usuarios")

opcion = st.selectbox("Selecciona una opción", ["Agregar Usuario", "Mostrar Usuario"])

if opcion == "Agregar Usuario":
    nombre = st.text_input("Nombre del usuario")
    if st.button("Agregar"):
        if nombre:
            agregar_usuario(nombre)
        else:
            st.error("El nombre no puede estar vacío")

elif opcion == "Mostrar Usuarios":
    if st.button("Mostrar usuarios"):
        mostrar_usuarios()