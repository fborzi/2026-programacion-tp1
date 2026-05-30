"""
Vamos a trabajar con el ejercicio de Python 1102, donde se solicitara que 
se ingrese una primer cadena, luego una segunda cadena. Luego pedimos que 
se verifique cuantas veces se encuentra lo que se ingresa en la segunda cadena 
dentro de la primera. Despues pedimos que ambas cadenas se junten. Y por ultimo buscamos 
cuantas veces aparece la letra H en la segunda cadena.
"""
cantidad = 0

texto1 = input("Ingrese la primer cadena: ")
texto2 = input("Ingrese la segunda cadena: ").lower()
concatenando = texto1.lower() + texto2.lower()
cantidad = texto2.count(texto1)

print("Cantidad de veces que aparece: ", cantidad)
print("Concatenacion: ", concatenando)
print("la letra 'H' aparece", texto2.count("h"), "veces en la cadena", 'texto2')
