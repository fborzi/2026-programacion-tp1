"Este modulo lee una cadena de texto y muestra su longitud, si contiene la subcadena 'la', la cadena en mayúsculas y la cantidad de vocales en minúscula que tiene."

cadena = input("ingrese una cadena de texto: ")

print("La longitud de la cadena es:", len(cadena))

if "la" in cadena.lower():
    print("Contiene 'la': Si")
else:
    print("No contiene 'la': No")

print("Cadena en mayúsculas:", cadena.upper())

vocales = 0

for letra in cadena.lower():
    if letra in "aeiou":
        vocales = vocales + 1
print("Vocales en minúsculas:", vocales)
