cadena1 = input("ingrese la primera cadena: ")
cadena2 = input("ingrese la segunda cadena: ")

print("cantidad de veces que aparece:", cadena2.count(cadena1))

concatenacion = cadena1.lower() + cadena2.lower()
print("Concatenacion:", concatenacion)

letra = cadena1[1]
cantidad = cadena2.count(letra)

print ("la letra", letra, "aparece", cantidad, "veces en la cadena")