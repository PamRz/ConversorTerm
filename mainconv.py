from conversiones import celsius_fahr,fahr_celsius
from conversiones import celsius_fahr, fahr_celsius
from conversiones import celsius_kelvin, kelvin_celsius

# Ahora puedes usar ambas funciones
resulCel_fah = celsius_fahr(30)
resulFah_cel = fahr_celsius(86)
resulCel_kel = celsius_kelvin (120)
resulKel_cel = kelvin_celsius(400)
print("ResultadoenFah :", resulCel_fah)
print("ResultadoenCel :", resulFah_cel)
print("ResultadoenKel :", resulCel_kel)
print("ResultadoenCel :", resulKel_cel)

from conversiones import celsius_fahr, fahr_celsius, celsius_kelvin, kelvin_celsius

# Prueba la función celsius_fahr
grados_celsius = 30
grados_fahrenheit = celsius_fahr(grados_celsius)
print(f"{grados_celsius} grados Celsius son equivalentes a {grados_fahrenheit} grados Fahrenheit")

# Prueba la función fahr_celsius
grados_fahrenheit = 86
grados_celsius = fahr_celsius(grados_fahrenheit)
print(f"{grados_fahrenheit} grados Fahrenheit son equivalentes a {grados_celsius} grados Celsius")

#Prueba la funcion celsius_kelvin
grados_celsius = 120
grados_kelvin = celsius_kelvin(grados_celsius)
print(f"{grados_celsius} grados Celsius son equivalentes a {grados_kelvin} grados kelvin")

#Prueba la funcion kelvin_celsius

grados_kelvin = 400
grados_celsius = kelvin_celsius(grados_kelvin)
print(f"{grados_kelvin} grados kelvin son equivalentes a {grados_celsius} grados Celsius")
from conversiones import celsius_fahr, fahr_celsius, celsius_kelvin, kelvin_celsius

