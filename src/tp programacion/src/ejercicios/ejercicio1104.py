""" Este programa recibe una fecha escrita por el usuario en formato dd/mm/aaaa.
A partir de la cadena ingresada, obtiene el día, el mes y el año utilizando
índices y cortes de texto. Luego genera una versión abreviada de la fecha
y muestra cada uno de sus componentes por separado en pantalla.
"""
fecha = input("Ingrese una fecha (dd/mm/aaaa): ")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

anio_corto = fecha[8:10]
print("Formato:", anio_corto + "-" + mes + "-" + dia)

print("El día es:", dia)
print("El mes es:", mes)
print("El año es:", anio)
