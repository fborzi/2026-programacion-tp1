"""Ejercicio 1102 - Manipulación de cadenas"""

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print(f"Cantidad de veces que aparece: {cantidad}")

if cadena2:
    CADENA2_MODIFICADA = cadena2[0].lower() + cadena2[1:]
else:
    CADENA2_MODIFICADA = ""

concatenacion = cadena1 + CADENA2_MODIFICADA
print(f"Concatenación: {concatenacion}")

primera_letra = cadena1[0]
cantidad_letra = cadena2.count(primera_letra)
print(f"La letra '{primera_letra}' aparece {cantidad_letra} veces en la cadena '{cadena2}'")
