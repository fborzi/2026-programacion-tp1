"""
Leer desde teclado dos cadena de caracteres y luego
a. Imprimir la cantidad de veces que se encuentra la primera cadena en la segunda.
b. Generar una nueva cadena con la concatenación de ambas. 
La segunda cadena deberá comenzar con minúscula (independientemente de cómo la haya ingresado el usuario).
c. Contar cuántas veces aparece la primera letra de la primer cadena
en la segunda cadena e informar con el siguiente formato: "La letra .. aparece .. veces en la cadena ..."
"""

cadena1 = input("Escribir la cadena 1 : ")
cadena2 = input("Escribir la cadena 2 : ")

print("Cantidad de veces que aparece: ", cadena2.count(cadena1))

concatenacion = cadena1 + cadena2.lower()
print("Concatenacion :", concatenacion)

primera_letra = cadena1[0]
cantidad = cadena2.upper().count(primera_letra.upper())

print("La letra", primera_letra, "aparece", cantidad, "veces en la cadena", cadena2)
