import streamlit as st
import conversiones  # Importa tu archivo conversiones.py
import fahr_celsius  # Importa tu archivo fahr_celsius.py
import mainconv  # Importa tu archivo mainconv.py

# Título de la aplicación
st.title("Conversor de Escalas Termométricas")

# Entrada de temperatura
temperatura = st.number_input("Introduce la temperatura:")

# Selección de escala de origen
escala_origen = st.selectbox("Selecciona la escala de origen:", ("Celsius", "Fahrenheit", "Kelvin"))

# Selección de escala de destino
escala_destino = st.selectbox("Selecciona la escala de destino:", ("Celsius", "Fahrenheit", "Kelvin"))

# Conversión de temperatura usando las funciones de tus archivos
if st.button("Convertir"):
    if escala_origen == "Celsius" and escala_destino == "Fahrenheit":
        resultado = fahr_celsius.celsius_a_fahrenheit(temperatura)
        st.write(f"{temperatura}° Celsius son {resultado}° Fahrenheit")
    elif escala_origen == "Celsius" and escala_destino == "Kelvin":
        resultado = conversiones.celsius_a_kelvin(temperatura)
        st.write(f"{temperatura}° Celsius son {resultado} Kelvin")
    elif escala_origen == "Fahrenheit" and escala_destino == "Celsius":
        resultado = fahr_celsius.fahrenheit_a_celsius(temperatura)
        st.write(f"{temperatura}° Fahrenheit son {resultado}° Celsius")
    elif escala_origen == "Fahrenheit" and escala_destino == "Kelvin":
        resultado = conversiones.fahrenheit_a_kelvin(temperatura)
        st.write(f"{temperatura}° Fahrenheit son {resultado} Kelvin")
    elif escala_origen == "Kelvin" and escala_destino == "Celsius":
        resultado = conversiones.kelvin_a_celsius(temperatura)
        st.write(f"{temperatura} Kelvin son {resultado}° Celsius")
    elif escala_origen == "Kelvin" and escala_destino == "Fahrenheit":
        resultado = conversiones.kelvin_a_fahrenheit(temperatura)
        st.write(f"{temperatura} Kelvin son {resultado}° Fahrenheit")
    else:
        st.write("Selecciona una escala de origen y destino válida")
