cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print("Cantidad de veces que aparece:", cantidad)

cadena2 = cadena2[0].lower() + cadena2[1:]
nueva_cadena = cadena1 + " " + cadena2
print("Concatenación:", nueva_cadena)

primera_letra = cadena1[0].lower()
veces = cadena2.lower().count(primera_letra)
print("La letra", primera_letra, "aparece", veces, "veces en la cadena", cadena2)
