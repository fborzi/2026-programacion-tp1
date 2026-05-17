"""
Este programa analiza una cadena de caracteres ingresada
por el usuario.

El programa:
1) Muestra la cadena ingresada.
2) Informa su longitud.
3) Verifica si contiene la palabra "la".
4) Convierte el texto a mayúsculas.
5) Cuenta cuántas vocales minúsculas tiene.
"""
cadena = input()

print("La longitud de la cadena es", len(cadena))

print("¿La cadena contiene 'la'?:", "la" in cadena.lower())

print("La cadena en mayúsculas es", cadena.upper())

contador = 0

for letra in cadena.lower():
    if letra in "aeiou":
        contador += 1

print("La cantidad de vocales es", contador)