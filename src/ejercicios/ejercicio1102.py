""" En este programa se busca trabajar con el manejo y procesamiento de cadenas de caracteres en Python.
Se analizan dos cadenas ingresadas por el usuario, se buscan y se cuentan  palabras o letras dentro de una cadena.
Se unen dos cadenas para formar una nueva, en la que la primera letra de la segunda comienza con minusculas y se
cuentan las veces que aparace una letra especifica dentro de la cadena"""

cadena1 = input("Ingrese la primer cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
cantidad = cadena2.count(cadena1)
print("La cantidad de veces que aparece:",cantidad)

Nueva_Cadena = cadena1.lower() + cadena2.lower()
print("La nueva cadena es:", Nueva_Cadena)

letra = cadena1[0].lower()
cantidad_letra = cadena2.lower().count(letra)

print ("La letra", letra, "aparece", cantidad_letra, "veces en la cadena" ,cadena2)
