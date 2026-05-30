"""
Vamos a trabajar con el ejercicio de Python 1101, donde se ingresara lo siguinte: un 
codigo donde se le solicite al usuario que ingrese el texto que desea 
y luego se guarde en una variable llamada cadena. En la terminal se va a ver
la cadena ingresada y va detallar la longitud de la misma. Luego se pide verificar 
si en la cadena que se ingreso se encuentra 'la'. Luego se convertira la cadena completa en mayuscula.
Y finalizamos contando la cantidad de vocales que tiene la cadena ingresada.
"""
cadena = input("Ingrese cadena: ")
print("La longitud de la cadena es: ", len(cadena))
print("Contiene 'la' :" , "la" in cadena)
print("cadena en mayuscula: ", cadena.upper())
print("vocales en minuscula: ", cadena.count("a") + cadena.count("e") + cadena.count("i") + cadena.count("o") + cadena.count("u"))
