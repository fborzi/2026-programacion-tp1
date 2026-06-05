""" este ejercicio busca procesar una fecha ingresada como cadena de caracteres y extraer sus distintas partes 
-utilizando posiciones e índices."""

fecha = input("Ingrese una fecha (dd/mm/aaaa): ")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

anio_corto = fecha[8:10]
print("Formato:", anio_corto + "-" + mes + "-" + dia)

print("El día es:", dia)
print("El mes es:", mes)
print("El año es:", anio)
print("El año es:", anio)