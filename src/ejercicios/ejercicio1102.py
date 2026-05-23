a = (input("Introduzca una cadena de caracteres: "))
b = (input("Introduzca una nueva cadena de caracteres: "))
cantidaddeveces = b.count(a)

print("la cantidad de veces que aparece es ", cantidaddeveces)
print(a, " ", b.lower())

primeraletra = b[0]
cantidad2 = a.count(primeraletra)

print("La letra ", primeraletra, " aparece ",
      cantidad2, " veces en la cadena ", a)
