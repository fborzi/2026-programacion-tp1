# Este programa evalua 2 cadenas de caracteres y trabaja a partir de ellas
# Utiliza diferentes metodos para contar y Convertir en minusculas o mayusculas.

cadena1 = input()
cadena2 = input()

print("Cantidad de veces que aparece:", cadena2.count(cadena1))
print("Concatenacion:", cadena1.lower() + cadena2.lower())
letra1 = cadena1[0].lower()
print("La letra", cadena1[0], "aparece", cadena2.lower().count(letra1), "veces en la cadena", cadena2)
