cadena = input("Ingrese una frase: ")

a=cadena.count('a')
e=cadena.count('e')
i=cadena.count('i')
o=cadena.count('o')
u=(cadena.count('u'))
vocalesEnCadena = a+e+i+o+u

print("La frase ingresada es:", cadena)
print("La longitud de la cadena es: ", len(cadena))
print("Contiene 'la' la cadena ingresada?", 'la' in cadena )
print(cadena.upper())
print("La cadena tiene: ", vocalesEnCadena, "vocales")
