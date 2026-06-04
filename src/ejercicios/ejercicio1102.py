#Este programa evalua 2 cadenas de caracteres y traabaja a partir de ellas
#Utiliza diferentes metodos para contar y Convertir en minusculas o mayusculas.

cadena1=""
cadena2=""
letra1=[]

cadena1= input()
cadena2= input()
letra1= cadena1[0]

print("Cantidad de veces que aparece:", cadena1.count(cadena2))
print("Concatenacion:", cadena1 + cadena2.casefold())
print("La letra", letra1, "aparece", cadena2.count(letra1), "veces en la cadena", cadena2  )