texto1 = input("ingrese la primera cadena: ")
texto2 = input("ingrese la segunda cadena: ")
cantidad = texto2.count(texto1)
print("cantidad de veces que aparece", cantidad)
concatenancion = texto1.lower() + texto2.lower()
print("concatenación:", concatenancion)
primera_letra = texto1[0]
veces = texto2.count(primera_letra)
print("la letra", primera_letra, "aparece", veces, "veces en la cadena", texto2)