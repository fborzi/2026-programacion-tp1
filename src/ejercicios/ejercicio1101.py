"""
Vamos a trabajar con el ejercicio de Python 1101, donde se ingresara lo siguinte: un 
codigo donde se le solicite al usuario que ingrese el texto que desea 
y luego se guarde en una variable llamada cadena. En la terminal se va a ver
la cadena ingresada y va detallar la longitud de la misma. Luego se pide verificar 
si en la cadena que se ingreso se encuentra 'la'. Luego se convertira la cadena completa en mayuscula.
Y finalizamos contando la cantidad de vocales que tiene la cadena ingresada.
"""
texto = input("Ingrese texto: ")
vocales = 0
vocales = (texto.count("a") + texto.count("e") + texto.count("i") + texto.count("o") + texto.count("u"))

print("La longitud de la cadena es: ", len(texto))
if "la" in texto:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la': No")
print("Cadena en mayúscula: ", texto.upper())
print("Vocales en minúsculas: ", vocales)
