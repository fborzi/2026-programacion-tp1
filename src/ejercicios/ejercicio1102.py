
cadena = input("ingrese una cadena: ")
subcadena = input("ingrese una subcadena: " )

print("cantidad de veces que aparece: ", subcadena.count(cadena) )

print("concatenacion:", cadena.lower()+ subcadena.lower())
 
primera_letra = cadena[0].lower()
cantidad_letra = subcadena.lower().count(primera_letra)
print("la letra",primera_letra, "aparece", cantidad_letra, "veces en la cadena", subcadena)