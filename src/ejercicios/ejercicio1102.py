"""
Vamos a trabajar con el ejercicio de Python 1102, donde se solicitara que se ingrese una primer cadena, luego una segunda
cadena. Luego pedimos que se verifique cuantas veces se encuentra lo que se ingresa en la segunda cadena dentro de la
priemra. Despues pedimos que ambas cadenas se junten. Y por ultimo buscamos cuantas veces aparece la letra H en la 
segunda cadena.
"""
cadena1 = input("Ingrese la primer cadena: ")
cadena2 = input("Ingrese la segunda cadena: ").lower()
concatenacion = cadena1+cadena2
print("Cantidad de veces que aparece: ", cadena2.count(cadena1))
print("Concatenacion: ",cadena1+cadena2)
print("la letra 'H' aparece", cadena2.count("h"), "veces en la cadena", 'cadena2')