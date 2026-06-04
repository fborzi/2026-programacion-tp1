"""
Programa para analizar longitudes y vocales en cadenas.
"""
cadena = input()
a = cadena.count('a')
e = cadena.count('e')
i = cadena.count('i')
o = cadena.count('o')
u = cadena.count('u')
vocalesEnCadena = a + e + i + o + u


print("La longitud de la cadena es", len(cadena))
print("¿La cadena contiene 'la'?:", 'la' in cadena)
print("La cadena en mayúsculas es:" ,cadena.upper())
print("La cantidad de vocales es", int(vocalesEnCadena))
