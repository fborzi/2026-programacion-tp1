"""
en este ejercicio se pide ingresar dos cadenas por teclado que tienen que ser numero y 
se realiza la suma, la division, si es divisor y luego la resta
"""
SUMA = 0
DIVISION = 0.0
PORCENTAJE = 0.0

numero1 = int(input("ingrese un numero entero: "))
numero2 = int(input("ingrese el segundo numero entero: "))

suma = numero1+numero2
print ("La suma de", numero1, "y", numero2, "es:", suma)

if numero2 != 0:
    print("La division de", numero1, "y", numero2, "es:", numero1/numero2)
    print("Es divisor:", numero1 % numero2 == 0)
else:
    print("No se puede dividir por cero")
    print("La division de", numero1, "y", numero2, "es:", 0.0)
    print("Es divisor:", False)

print("El", numero2, "% de", numero1, "es:", int(numero1 * numero2 / 100))