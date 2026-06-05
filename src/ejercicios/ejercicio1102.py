"""Este ejericio se trata de ingresar dos cadenas y realizar diferentes operaciones 
con ellas, como contar cuantas veces aparece una cadena dentro de la otra,concatenar las cadenas, etc."""

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cantidad = cadena2.count(cadena1)
print("Cantidad de veces que aparece:", cantidad)

concatenacion = cadena1.lower() + cadena2.lower()
print("Concatenación:", concatenacion)

letra = cadena1[0].lower()
cantidad_letra = cadena2.lower().count(letra)

print("La letra '", letra, "' aparece", cantidad_letra,
      "veces en la cadena '", concatenacion, "'")
