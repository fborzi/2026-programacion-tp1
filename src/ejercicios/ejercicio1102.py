cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

print("Cantidad de veces que aparece:", cadena2.count(cadena1))

print("Concatenacion:", cadena1 + cadena2.lower())

letra = cadena1[0]

print("La letra", letra, "aparece", cadena2.count(letra), "veces en la cadena", cadena2)
