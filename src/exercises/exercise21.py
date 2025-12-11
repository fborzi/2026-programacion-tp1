""" Alguna cosita con cadenas """
cadena1 = input("Ingrese un texto: ").lower()
cadena2 = input("Ingrese otro texto: ").lower()

print("La cantidad de veces que aparece la cadena 2 en la cadena 1 es:", cadena2.count(cadena1))

print("La cadenas unidas es:", cadena1 + cadena2)

primera_letra = cadena1[0]
print("La letra", primera_letra, "aparece", cadena2.count(primera_letra), "veces en la primera cadena.")
