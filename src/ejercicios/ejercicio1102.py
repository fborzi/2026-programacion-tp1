"""1102"""


texto1 = input("ingrese la primera cadena: ")
texto2 = input("ingrese la segunda cadena: ")

cantidad = texto2.count(texto1)
print("Cantidad de veces que aparece:", cantidad)

concatenacion = texto1.lower() + texto2.lower()
print("Concatenación:", concatenacion)

primera_letra = texto1[0].lower()
veces = texto2.lower().count(primera_letra)

print(f"La letra {texto1[0]} aparece {veces} veces en la cadena {texto2}")
