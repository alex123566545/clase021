import streamlit as st

# Inicialización de variables en el estado de la sesión
if 'usuarios' not in st.session_state:
    st.session_state['usuarios'] = []

# Función para agregar un usuario
def agregar_usuario(nombre):
    st.session_state['usuarios'].append(nombre)
    st.success(f"Usuario {nombre} agregado.")

# Función para mostrar usuarios
def mostrar_usuarios():
    if st.session_state['usuarios']:
        st.write("Lista de usuarios:")
        for usuario in st.session_state['usuarios']:
            st.write(f"- {usuario}")
    else:
        st.warning("No hay usuarios registrados.")

# Menú Principal
st.title("Gestión de Usuarios")

opcion = st.selectbox("Selecciona una opción", ["Agregar Usuario", "Mostrar Usuarios"])

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
