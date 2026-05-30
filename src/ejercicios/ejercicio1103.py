"""
En el ejercicio 1103 se va a ingresar dos numeros. Se los va a sumar en la primera parte y luego se va a dividir.
Cuando se divida verificaremos si es divisor. Y por ultimo pasaremos a sacar su porcentaje.
"""

suma = 0
division = 0.0
porcentaje = 0.0

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = a + b
porcentaje = int((a * b) / 100)

if b != 0:
    division = a / b
else:
    division = 0
print("La suma de", a, "y", b, "es:", suma)
print("La division de", a, "y", b, "es:", division)
if b != 0 and a % b == 0:
    print("Es divisor: True")
else:
    print("Es divisor: False")
print("El", str(b) + "%", "de", a, "es:", porcentaje)