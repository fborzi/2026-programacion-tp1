"""
Vamos a trabajar con el ejercicio de Python 1101, donde se ingresara lo siguinte: un codigo donde se le
solicite al usuario que ingrese una cadena y luego se guarde en una variable llamada cadena. En la terminal se va a ver
la cadena ingresada y va detallar la longitud de la misma. Luego se pide verificar si en la cadena que se 
ingreso se encuentra 'la'. Luego se convertira la cadena completa en mayuscula. Y finalizamos contando la cantidad de
vocales que tiene la cadena ingresada.
"""
cadena = input ("Ingrese cadena")
print ("Cadena ingresada: ", cadena)
print ("La longitud de la cadena es: ", len (cadena))
if "la" in cadena: 
    print ("Contiene 'la': Si")
else :
    print ("Contiene 'la': No") 
print (cadena.upper()) 
Vocales = (cadena.count ("a") + cadena.count ("e") + cadena.count ("i") + cadena.count ("o") + cadena.count ("u"))
print (Vocales)