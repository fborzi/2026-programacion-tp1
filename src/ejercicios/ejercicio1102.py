cadena1 = input ("ingrese primer cadena: ")
cadena2 = input ("ingrese segunda cadena: ")
letra = cadena1[0].lower()
cantidad = cadena2.count(cadena1)

print("Cantidad de veces que aparece: ", cantidad)
print("Concatenacion: ", cadena1.lower() + cadena2.lower()) 
print("La letra", letra, "aparece ", 
      cadena2.lower().count(letra), "veces en la cadena 'hola mundo hacia el horizonte' ")