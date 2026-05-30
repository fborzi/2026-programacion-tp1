"""
En este codigo vamos a realizar la actividad correspondiente al TP n°1 ejercicio 1104 en lenguaje Python desde VS code:
esto consta de ingresar una cadena de caracteres en formato de fecha e iremos trabajando sobre ella,
imprimiremos el tipo de formato 'aa-mm-dd',
entonces dividiremos la cadena imprimiendo el dia, el año y el mes correspomdiente
"""
fecha = input("Ingrese fecha establecida en formato 'dd/mm/aaaa'")
formato = fecha[8:] + "-" + fecha[3:5]+"-"+fecha[0:2]
print("Formato: ", formato)
print("El día es: ", fecha[0:2])
print("El mes es: ", fecha[3:5])
print("El año es: ", fecha[6:])
