""""comentario: este ejercicio te permite ingresar una cadena de un texto,
cuenta la longuitud del texto, verifica si cintiene X palabra y lo convierte en mayuscula"""

cadena = input("ingrese una cadena:")
longuitud = len(cadena)
print("la longitud de la cadena es: ",longuitud)
if "la" in cadena:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la': No")
    print("cadena en mayuscula: ", cadena.upper())
    vocales = ["a","e","i","o","u"]
    print("vocales en minuscula: ", sum(1 for letra in cadena if letra in vocales))
