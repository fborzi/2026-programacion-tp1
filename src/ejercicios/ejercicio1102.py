""" En este programa se busca trabajar con el manejo y procesamiento de cadenas de caracteres en Python.
Se analizan dos cadenas ingresadas por el usuario, se buscan y se cuentan  palabras o letras dentro de una cadena.
Se unen dos cadenas para formar una nueva, en la que la primera letra de la segunda comienza con minusculas y se
cuentan las veces que aparace una letra especifica dentro de la cadena"""

print("Ingrese la primer cadena:")
cadena1= input()
print("Ingrese la segunda cadena:")
cadena2 = input ()
cantidad = cadena2.count (cadena1)
print("La cantidad de veces que aparece:",cantidad)

NuevaCadena = cadena1 + " " + cadena2[0].lower() + cadena2[1:]
print("La nueva cadena es:", NuevaCadena) 

letra = cadena1[0]
cantidad_letra = cadena2.count(letra)

print ("La letra", letra, "aparece", cantidad_letra, "veces en la cadena" ,cadena2)
