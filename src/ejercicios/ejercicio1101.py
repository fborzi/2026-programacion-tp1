"""
en este ejercicio se realizara el ingreso por teclado de una cadena y 
se dira la longuitud de la misma, si dicha cadena contiene 'la', las vocales en minusculas que tiene y
se pasara la cadena a mayuscula
"""
cadena = input("ingrese cadena: ")

print("la longitud de la cadena es: ", len(cadena))
print("contiene 'la' :" , "la" in cadena)
print("cadena en mayuscula: ", cadena.upper())
print("vocales en minuscula: ", cadena.count ("a") + cadena.count ("e") +
    cadena.count ("i") + cadena.count ("o") + cadena.count ("u"))