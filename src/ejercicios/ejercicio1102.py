
"""ingreso la cadena, una subcadena, te dice cuantas veces aparece la cadena en la subcadena, 
concatena las cadenas osea las une formando una cadena nueva y te dice cuantas veces aparece la primera letra
en la subcadena"""
cadena = input("ingrese una cadena: ")
subcadena = input("ingrese una subcadena: " )

print("cantidad de veces que aparece: ", subcadena.count(cadena) )

print("concatenacion:", cadena.lower()+ subcadena.lower())
 
primera_letra = cadena[0].lower()
cantidad_letra = subcadena.lower().count(primera_letra)
print("la letra",primera_letra, "aparece", cantidad_letra, "veces en la cadena", subcadena)