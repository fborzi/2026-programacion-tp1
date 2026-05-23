cadena1 = input("ingrese la primera cadena: ")
cadena2 = input("ingrese la segunda cadena: ")

cantidad = cadena1.count(cadena2)
print("cantidad de veces que aparece:", cantidad)

cadena2 = cadena2[0].lower() + cadena2 [1:]

nueva = cadena1 + " " + cadena2
print("concatenacion:" , nueva)

letra = cadena1[0]

cantidad_letra = nueva.count(letra)
print("la letra", letra, "aparece", cantidad_letra,
      "veces en la cadena", cadena2)