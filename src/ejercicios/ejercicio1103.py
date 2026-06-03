"""
En este codigo vamos a realizar la actividad correspondiente al TP n°1 ejercicio 1103 en lenguaje Python desde VS code:
esto consta de ingresar dos numeros enteros, guardarlos en variables y luego empezar a trabajar sobre ellas.
primeramente sumaremos las dos variables e imprimiremos el resultado,
luego dividiremos las mismas entre si e imprimiremos el resultado,
buscaremos condicionar si la variable "a" es divisor de la variable "b" y motraremos si es verdadero o falso,
tambien mostraremos el porcentaje que corresponde a la variable "b" sobre "a" y mostraremos los resultados,
por ultimo corregiremos el codigo "print("El precio es $" + a)".
para la correcta visualizacion deberiamos cambiar el signo + por una coma, quedaria asi "print("El precio es $", a)"
y para mostrar el resultado con decimales en el ultimo punto lo lograremos de la siguiente manera:
"print("El ", numero2, "% " "de ",numero1, "es", numero1 * (numero2/100))"
"""
division = 0.0
suma = 0.0
porcentaje = 0.0
divisionPosible = False
numero1 = int(input("Ingrese primer numero entero:"))
numero2 = int(input("Ingrese segundo numero entero:"))
suma = numero1 + numero2
if numero2 != 0:
    division = numero1/numero2
    porcentaje = numero1 * numero2/100    
    divisionPosible = numero1%numero2==0
    
    
    
print("la suma de ", numero1, " y ", numero2, " es:", suma)
print("la division de", numero1 , "y",  numero2, "es:", division)
print("Es divisor:",divisionPosible)
print("El", numero2,"% de", numero1,"es:", porcentaje)
#print("El ", numero2, "% " "de ",numero1, "es", "{:.2f}".format(numero1 * (numero2/100)))
#print("El precio es $", numero1)
