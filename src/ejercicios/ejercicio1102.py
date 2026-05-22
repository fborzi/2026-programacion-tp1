cadena1= input("Ingrese una cadena de caracteres: ")
cadena2= input("Ingrese otra cadena: ")
letra1= cadena1[0]
print("Cantidad de veces que aparece: ", cadena2.count(cadena1))
print(cadena1 + cadena2.casefold())
print("La letra ", letra1, "aparece ", cadena2.count(letra1), "veces en la cadena ", cadena2  )