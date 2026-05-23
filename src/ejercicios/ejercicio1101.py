
cadena = input()
a = cadena.count('a')
e = cadena.count('e')
i = cadena.count('i')
o = cadena.count('o')
u = cadena.count('u')
vocalesEnCadena = a + e + i + o + u


print("La longitud de la cadena es:",len(cadena))
print("Contiene 'la':",'la' in cadena)
print("Cadena en mayúsculas:",cadena.upper())
print("Vocales en minúsculas:",vocalesEnCadena)
