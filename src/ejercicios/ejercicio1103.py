"""
En el ejercicio 1103 se va a ingresar dos numeros. Se los va a sumar en la primera parte y luego se va a dividir.
Cuando se divida verificaremos si es divisor. Y por ultimo pasaremos a sacar su porcentaje.
"""

SUMA = 0
DIVISION = 0.0
PORCENTAJE = 0.0

a = int(input("Ingrese numero: "))
b = int(input("Ingrese numero: "))

print("La suma de", a, "y", b, "es:", a + b)

if b != 0:
    print("La división de", a, "y", b, "es:", a / b)
    print("Es divisor:", a % b == 0)
else:
    print("No se puede dividir por cero")
    print("La división de", a, "y", b, "es:", 0.0)
    print("Es divisor:", False)

print("El", b, "% de", a, "es:", int(a * b / 100))
