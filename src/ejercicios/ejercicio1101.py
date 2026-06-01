""""comentario: este ejercicio te permite ingresar una cadena de un texto,
cuenta la longuitud del texto, verifica si cintiene X palabra y lo convierte en mayuscula"""

cadena = input("ingrese una cadena:")

print(cadena)
print("la longitud de la cadena es: ",len(cadena)) 

if "la" in cadena:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la': No")

print("cadena en mayuscula: ", cadena.upper())
vocales = "aeiou" 
print("vocales en minuscula: ", sum(1 for letra in cadena if letra in vocales) )  
    















