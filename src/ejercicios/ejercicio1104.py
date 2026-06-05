"""Ejercicio 1104 - Procesamiento de fechas."""
fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
barra1 = fecha.index("/")
barra2 = fecha.index("/", barra1 + 1)
dia = fecha[:barra1]
mes = fecha[barra1 + 1:barra2]
anio = fecha[barra2 + 1:]
aa = anio[2:]
print("Formato:", aa + "-" + mes + "-" + dia)
print("El día es:", dia)
print("El mes es:", mes)
print("El año es:", anio)
