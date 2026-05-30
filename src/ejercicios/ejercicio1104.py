"""
En el ejercicio 1104, vamos a ingresar una dos digitos para el dia, dos digitos para el mes y cuatro digitos para el 
año. Luego cambiaremos la forma de verlo en la pantalla, donde quedara primero los cuatro digitos del año, los dos 
del mes y los dos del dia.
"""
fecha = input()

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

print(dia)
print(mes)
print(anio)
print(anio[2:4] + "-" + mes + "-" + dia)