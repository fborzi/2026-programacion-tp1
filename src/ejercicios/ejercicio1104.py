"""Ejercicio 1104."""

fecha = input()

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

print("formato:", anio[2:4] + "-" + mes + "-" + dia)
print("el dia es:", dia)
print("el mes es:", mes)
print("el año es:", anio)
