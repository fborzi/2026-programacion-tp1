"""
En el ejercicio 1104, vamos a ingresar una dos digitos para el dia, dos digitos para el mes y cuatro digitos para el 
año. Luego cambiaremos la forma de verlo en la pantalla, donde quedara primero los cuatro digitos del año, los dos 
del mes y los dos del dia.
"""
fecha = input("Ingrese dd/mm/aaaa: ")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]
anio_dos = fecha[8:10]

print("Formato: ", anio_dos + "-" + mes + "-" + dia)
print("El día es: ", dia)
print("El mes es: ", mes)
print("El año es: ", anio)
