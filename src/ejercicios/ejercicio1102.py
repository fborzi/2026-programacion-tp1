cadena1= input("ingrese la primer cadena:")
cadena2= input("ingrese la segunda cadena: ")

print("la cantidad de veces que se encuentra la cadena 2 en la cadena 1 es:", cadena1.count(cadena2))

cadena3= cadena1+cadena2
print("la suma de las cadenas es:", cadena3.lower())

letra= cadena1[0]
veces= cadena2.count(letra)

print("La letra", letra, "aparece", veces, "veces en la cadena 2")
