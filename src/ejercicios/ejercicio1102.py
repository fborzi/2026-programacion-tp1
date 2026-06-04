"""Este ejericio se trata de ingresar dos cadenas y realizar diferentes operaciones 
con ellas, como contar cuantas veces aparece una cadena dentro de la otra,concatenar las cadenas, etc."""

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")



cantidad = cadena2.count(cadena1)
print("Cantidad de veces que aparece:", cantidad)



cadena2_minuscula = cadena2[0].lower() + cadena2[1:]
concatenacion = cadena1 + cadena2_minuscula
print("Concatenación:", concatenacion)

letra = cadena1[0]
concatenacion=cadena1+cadena2
cantidad_letra =concatenacion.count(letra)


print("La letra '",letra,"' aparece",cantidad_letra,"veces en la cadena '",concatenacion,"'")