"""El codigo implementa búsqueda de cadenas, concatenación y 
conteo de caracteres"""

cadena1 = input("Ingrese una palabra: ")
cadena2 = input("Ingrese una palabra: ")

cantidad = cadena2.count(cadena1)
print("Cantidad de veces que aparece:", cantidad)

concatenacion = cadena1 + cadena2
print("Concatenacion:", concatenacion)

letra = cadena1[0]
veces = cadena2.count(letra)
print("Le letra", letra, "aparece", veces, "veces en la cadena", cadena2)
