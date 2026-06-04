"""
Programa para evaluar y manipular cadenas de caracteres.
"""

cadena1 = input()
cadena2 = input()


letra1 = cadena1[0]

aparece = cadena2.lower().count(letra1.lower())

print("Cantidad de veces que aparece:", cadena2.count(cadena1))


concatenacion = (cadena1+ cadena2).lower()
print("Concatenación:", concatenacion)

print(f"La letra '{letra1}' aparece {aparece} veces en la cadena '{cadena2}'")

