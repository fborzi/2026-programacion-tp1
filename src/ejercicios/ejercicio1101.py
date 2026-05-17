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

print(len(cadena))

print("la" in cadena.lower())

print(cadena.upper())

contador = 0

for letra in cadena.lower():
    if letra in "aeiou":
        contador += 1

print(contador)