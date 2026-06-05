"""Ejercicio 1102 - Operaciones con dos cadenas."""
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
print("Cantidad de veces que aparece:", cadena2.count(cadena1))
concatenacion = cadena1.lower() + cadena2[0].lower() + cadena2[1:]
print("Concatenación:", concatenacion)
primera_letra = cadena1[0]
cantidad = cadena2.count(primera_letra)
print("La letra '" + primera_letra + "' aparece", cantidad,
      "veces en la cadena '" + cadena2 + "'")