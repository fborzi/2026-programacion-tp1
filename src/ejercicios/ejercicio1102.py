# Este programa evalua 2 cadenas de caracteres y trabaja a partir de ellas
# Utiliza diferentes metodos para contar y Convertir en minusculas o mayusculas.

cadena1 = input()
cadena2 = input()


letra1 = cadena1[0]

aparece = cadena2.lower().count(letra1.lower())

print("Cantidad de veces que aparece:", cadena1.count(cadena2))


concatenacion = cadena1.lower() + cadena2.lower()
print("Concatenación:", concatenacion)

print(f"La letra '{letra1}' aparece {aparece} veces en la cadena '{cadena2}'")

