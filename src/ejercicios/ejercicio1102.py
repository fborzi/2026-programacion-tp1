"""
En este codigo vamos a realizar la actividad correspondiente al TP n°1 ejercicio 1102 en lenguaje Python desde VS code:
esto consta de ingresar dos cadena de caracteres, guardarla cada cadena y luego empezar a trabajar sobre ellas.
contaremos la longitud de la cadena e imprimiremos el resultado,
buscaremos cuantas veces aparece la cadena1 en la cadena2 e imprimiremos en resultado,
concatenaremos las dos cadenas haciendo que la segunda empiece con minuscula independientemente de como haya sido
cargada,por ultimo buscaremos y contaremos la cantidad de veces que aparece la primera letra de cadena1 en la cadena2 e 
imprimiremos el resultado
"""
cadena1 = input("Ingrese cadena 1 de caracteres: ")
cadena2 = input("Ingrese cadena 2 de caracteres: ")
print("Cantidad de veces que aparece: ", cadena2.count(cadena1))
print("Concatenacion:",cadena1, cadena2[0].lower()+ cadena2[1::])
print("la letra '", cadena1[0], "' aparece", cadena2.lower().count(cadena1[0].lower()), " veces en la cadena ",cadena2)
