"""Ejercicio 1104 - Formato de fecha"""

fecha = input()

primera_barra = fecha.index('/')
segunda_barra = fecha.index('/', primera_barra + 1)

dia = fecha[:primera_barra]
mes = fecha[primera_barra + 1:segunda_barra]
anio = fecha[segunda_barra + 1:]

anio_corto = anio[2:]

print(f"Formato: {anio_corto}-{mes}-{dia}")
print(f"El dia es: {dia}")
print(f"El mes es: {mes}")
print(f"El año es: {anio}")