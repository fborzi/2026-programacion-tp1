cadena1 = input("ingrese la primera cadena: ")
cadena2 = input("ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print(f"cantidad de veces que aparece: {cantidad}")

if cadena2:
    cadena2_modificada = cadena2[0].lower() + cadena2[1:]
else:
    cadena2_modificada = ""

concatenacion = cadena1 + cadena2_modificada
print(f"concatenacion: {concatenacion}")

primera_letra = cadena1[0]
cantidad_letra = cadena2.count(primera_letra)
print(f"la letra '{primera_letra}' aparece {cantidad_letra} veces en la cadena '{cadena2}'")