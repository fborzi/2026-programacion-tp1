cadena1 = input()
cadena2 = input()

letra1 = cadena1[0]

vecesLetra = cadena2.lower().count(letra1.lower())

print("Cantidad de veces que aparece:", cadena2.count(cadena1))
print("Concatenacion:", cadena1.lower() + cadena2.lower())

print("La letra '" + letra1 + "' aparece", vecesLetra, "veces en la cadena '" + cadena2 + "'")

