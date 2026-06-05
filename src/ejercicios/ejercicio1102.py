cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print(f"Cantidad de veces que aparece: {cantidad}")

if cadena2:
    cadena2_modificada = cadena2[0].lower() + cadena2[1:]
else:
    cadena2_modificada = ""

concatenacion = cadena1 + cadena2_modificada
print(f"Concatenación: {concatenacion}")

primera_letra = cadena1[0]
cantidad_letra = cadena2.count(primera_letra)
print(f"La letra '{primera_letra}' aparece {cantidad_letra} veces en la cadena '{cadena2}'")