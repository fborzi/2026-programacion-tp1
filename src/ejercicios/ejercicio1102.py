cadena1 = input("ingrese la primera cadena: ")
cadena2 = input("ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print("cantidad de veces que aparece:", cantidad)

cadena2_min = cadena2[0].lower() + cadena2[1:]
concatenacion = cadena1.lower() + cadena2_min
print("concatenacion: ", concatenacion)

primera_letra = cadena1[0]
cantidad_letra = cadena2.count(primera_letra)
print("la letra", "'" + primera_letra + "'", "aparece", cantidad_letra, "veces en la cadena", "'" + cadena2 + "'")