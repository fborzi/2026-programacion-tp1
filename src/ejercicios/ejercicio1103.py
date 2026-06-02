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
numero1 = int(input("Ingrese primer numero entero:"))
numero2 = int(input("Ingrese segundo numero entero:"))
print("la suma de ", numero1, " y ", numero2, " es:", numero1 + numero2)

if numero2 != 0:
    print("la division de", numero1 , "y",  numero2, "es:", numero1/numero2)
else:
    print("la division de", numero1, "y", numero2, "es:", 0.0)
    print("No se puede dividir por cero")
if numero2 != 0 and numero1 != 0:
    print("Es divisor:",numero1%numero2==0)
else:
    print("Es divisor:",False)
print("El", numero2,"% de", numero1,"es:", int(numero1*numero2/100))
#print("El ", numero2, "% " "de ",numero1, "es", "{:.2f}".format(numero1 * (numero2/100)))
#print("El precio es $", numero1)
