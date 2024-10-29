import streamlit as st

def validate_data(marca, modelo, kilometraje):
    """Valida los datos ingresados para el automóvil."""
    if not marca or not modelo:
        return "La marca y el modelo no deben estar vacíos."
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            return "El kilometraje no puede ser menor que 0."
    except ValueError:
        return "El kilometraje debe ser un número válido."
    return None

def main():
    st.title("Registro de Automóvil")
    st.write("Ingrese los datos del automóvil a continuación:")

    #Registro por el usuario
    marca = st.text_input("Marca del automóvil")
    modelo = st.text_input("Modelo del automóvil")
    kilometraje = st.text_input("Kilometraje del automóvil")

    if st.button("Registrar"):
        #validación de los datos
        error = validate_data(marca, modelo, kilometraje)
        if error:
            st.error(error)
        else:
            st.success("Automóvil registrado exitosamente.")
            st.write("**Marca:**",marca)
            st.write("**Modelo:**",modelo)
            st.write("**Kilometraje:**", kilometraje)

if __name__ == "__main__":
    main()