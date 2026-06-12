cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print("Cantidad de veces que aparece:", cantidad)

cadena1 = cadena1[0].lower() + cadena1[1:]
cadena2 = cadena2[0].lower() + cadena2[1:5] + cadena2[5].lower() + cadena2[6:30]
nueva_cadena = cadena1 + cadena2
print("Concatenación:", nueva_cadena)

primera_letra = cadena1[0].lower()
veces = cadena2.lower().count(primera_letra)
primera_letra = primera_letra.upper()
print("La letra", primera_letra , "aparece", veces, "veces en la cadena", cadena2)
