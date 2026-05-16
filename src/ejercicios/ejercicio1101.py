"""
En este codigo vamos a realizar la actividad correspondiente al TP n°1 ejercicio 1101 en lenguaje Python desde VS code:
esto consta de ingresar una cadena de caracteres, guardarla en una variable luego vamos a trabajar sobre la misma.
contaremos la longitud de la cadena e imprimiremos el resultado,
buscaremos la sigla "la" e inprimiremos si fue encontrada o no,
imprimiremos la cadena convertida a MAYUSCULA,
por ultimo buscaremos y contaremos la cantidad de vocales en minuscula e imprimiremos el total
"""
s = input("Ingrese cadena de caracteres: ")
print("Cadena ingresada: ", s)
print("la longitud de la cadena es: ", len(s))
if "la" in s:
    print ("sigla ´la´ fue encontrada: Si ")
else:  
    print("sigla ´la´ fue encontrada: No ")
print(s.upper()) 
vocal_total = ( s.count("a") + s.count("e") +  s.count("i") +  s.count("o") +  s.count("u"))
print("el total de vocales en minusculas utilizadas son:", vocal_total)
