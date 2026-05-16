"""Leer desde teclado dos cadenas de caracteres y luego:
a. Imprimir la cantidad de veces que se encuentra la segunda cadena en la primera.
b. Generar una nueva cadena con la concatenación de ambas. La segunda cadena deberá
comenzar con minúscula (independientemente de cómo la haya ingresado el usuario).
c. Contar cuántas veces aparece la primera letra de la primer cadena en la segunda cadena e
informar con el siguiente formato: "La letra '.' aparece .. veces en la cadena ' ... """


cadena1 = input("ingrese la primera cadena:")
cadena2 = input("ingrese la segunda cadena:")

contador = 0
cantidad = cadena1.find(cadena2)

while cantidad != -1:
    contador += 1
    cantidad = cadena1.find(cadena2, cantidad + 1)

print("la cantidad de veces que se encuentra la segunda cadena en la primera es:" , contador)


cadenaNueva = cadena1.lower() + " " + cadena2
print(cadenaNueva)


primera_letra = cadena1[0]
contador = 0

for x in cadena2:
    if x == primera_letra: # type: ignore
        contador += 1   
else:
    print("no hay coincidencias encontradas")
   
print("La letra: " + primera_letra + " aparece " +  str(contador)  + " veces en la frase ingresada: " + cadena2)
