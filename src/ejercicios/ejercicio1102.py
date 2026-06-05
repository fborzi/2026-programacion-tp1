"""
 en este ejercicio se pide ingresar dos cadenas para ver cuantas veces aparece la primer cadena en la
 segunda, generar una nueva cadena concatenando ambas y que la segunda cadena arranque en minuscula 
 y por ultimo contar cuantas veces aparece la primera letra de la primer cadena en la segunda
 """
cadena1 = input ("ingrese primer cadena: ")
cadena2 = input ("ingrese segunda cadena: ")
letra = cadena1[0].lower()
cantidad = cadena2.count(cadena1)
print("Cantidad de veces que aparece: ", cantidad)
print("Concatenacion: ", cadena1.lower() + cadena2.lower())
print("La letra", letra, "aparece ",
      cadena2.lower().count(letra), "veces en la cadena 'hola mundo hacia el horizonte' ")
