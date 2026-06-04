"""
Programa para formatear fechas según la salida esperada.
"""

fecha = input()

print(f"Formato: {fecha[8:10]}-{fecha[3:5]}-{fecha[0:2]}")
print(f"El día es: {fecha[0:2]}")
print(f"El mes es: {fecha[3:5]}")
print(f"El año es: {fecha[6:10]}")
