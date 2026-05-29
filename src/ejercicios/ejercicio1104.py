"""
En el ejercicio 1104, vamos a ingresar una dos digitos para el dia, dos digitos para el mes y cuatro digitos para el 
año. Luego cambiaremos la forma de verlo en la pantalla, donde quedara primero los cuatro digitos del año, los dos 
del mes y los dos del dia.
"""

fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
dia = fecha [0:2]
mes = fecha [3:5]
anio = fecha [6:10]
aa = anio[2:4]

print("El día es: ", dia)
print("El mes es: ", mes)
print("El año es: ", anio)
print("Formato: ", aa + "-" + mes + "-" + dia)