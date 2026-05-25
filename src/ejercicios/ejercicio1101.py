"""
Este programa analiza una cadena de caracteres ingresada
por el usuario.

El programa:
Muestra la cadena ingresada.
Informa su longitud.
Verifica si contiene la palabra "la".
Convierte el texto a mayúsculas.
Cuenta cuántas vocales minúsculas tiene.
"""
cadena = input()

print("La longitud de la cadena es", len(cadena))

print("¿La cadena contiene 'la'?:", "la" in cadena.lower())

print("La cadena en mayúsculas es:", cadena.upper())

contador = 0

for letra in cadena.lower():
    if letra in "aeiou":
        contador += 1

print("La cantidad de vocales es", contador)
