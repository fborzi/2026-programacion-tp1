"""Ejercicio 1101 - Análisis de una cadena."""
cadena = input("Ingrese una cadena: ")
print("La longitud de la cadena es:", len(cadena))
if "la" in cadena:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la': No")
print("Cadena en mayúsculas:", cadena.upper())
vocales = "aeiou"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
print("Vocales en minúsculas:", contador)