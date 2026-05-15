palabra="Programacion"
print(palabra)
len(palabra)
print("La longitud de la cadena es:", len(palabra))
if palabra.find("la") != -1: 
    print('Contiene "la": Si')
else:
    print('Contiene "la": No')
print('Cadena en mayusculas :', palabra.upper())
print("Vocales en minuscula:", palabra.count('a') + palabra.count('e') + palabra.count('i') + palabra.count('o') + palabra.count('u'))