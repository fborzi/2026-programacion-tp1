""""comentario: este ejercicio te permite ingresar una cadena de un texto,
cuenta la longuitud del texto, verifica si cintiene X palabra y lo convierte en mayuscula"""

cadena = input("ingrese una cadena:")  
print("la cadena es: ", cadena)
longitud = len(cadena)
print("la longitud de la cadena es: ", longitud) 
print("contiene 'la' :", 'la' in cadena)
print("cadena en mayuscula: ", cadena.upper())
vocales = "aeiou" 
print("vocales en minuscula: ", sum(1 for letra in cadena if letra in vocales) )  
    















