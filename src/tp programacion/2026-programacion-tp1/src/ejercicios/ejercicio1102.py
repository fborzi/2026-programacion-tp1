# Operaciones con dos cadenas

# Leer cadenas desde teclado
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

# a) Cantidad de veces que aparece la primera cadena en la segunda
cantidad = cadena2.count(cadena1)

print("Cantidad de veces que aparece:", cantidad)

# b) Concatenar ambas cadenas
# La segunda cadena debe comenzar en minúscula
concatenacion = cadena1.lower() + cadena2.lower()

print("Concatenación:", concatenacion)

# c) Contar cuántas veces aparece la primera letra
# de la primera cadena en la segunda cadena

primera_letra = cadena1[0]

cantidad_letra = cadena2.count(primera_letra)

print("La letra '" + primera_letra + "' aparece",
      cantidad_letra,
      "veces en la cadena '" + cadena2 + "'")