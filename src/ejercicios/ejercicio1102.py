#leer dos cadenas ingresadas a mano 
cadena = input( "ingrese una cadena : ")
subcadena = input( "ingrese una subcadena: " )
#cantidad de veces que aparece en la subcadena la cadena principal
print ("cantidad de veces que aparece: ", subcadena.count(cadena) )
#concatenar las cadena, osea unir
print("concatenacion: ", cadena + subcadena.lower())

#leer la letra H en la cadena 
primera_letra = cadena[0].lower()
cantidad_letra = subcadena.lower().count(primera_letra)
print("la letra",primera_letra, "aparece", cantidad_letra, "veces en la cadena: ", subcadena)