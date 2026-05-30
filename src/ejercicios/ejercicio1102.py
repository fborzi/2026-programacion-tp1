"""El codigo implementa búsqueda de cadenas, concatenación y 
conteo de caracteres"""

cadena1 = input("Ingrese una palabra: ")
cadena2 = input("Ingrese una palabra: ")

cantidad = cadena2.lower().count(cadena1.lower())
print("Cantidad de veces que aparece:", cantidad)

concatenacion = (cadena1 + cadena2).lower()
print("Concatenacion:", concatenacion)

letra = cadena1[0].lower()
veces = cadena2.lower().count(letra)
print("Le letra", letra, "aparece", veces, "veces en la cadena", cadena2)
