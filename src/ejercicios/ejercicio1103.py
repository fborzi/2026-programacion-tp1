"""El codigo realiza operaciones matematicas con dos numeros enteros"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = a + b
print("La suma de", a, "y", b, "es:", suma)

resultado_divisor = False
resultado_division = 0.0

if b != 0:
    resultado_division = a / b
    resultado_divisor = b % a == 0
else:
    print("No es posible dividir por cero")
    resultado_division = 0.0
    resultado_divisor = False

print("La division de", a, "y", b, "es:", resultado_division)
print("Es divisor:", resultado_divisor)

porcentaje = b * a / 100
if porcentaje.is_integer():
    porcentaje = int(porcentaje)

print("El", b, "% de", a, "es:", porcentaje)
#Para mostrar el resultado con decimales seria:
#print("El", b, "% de", a, "es:", f"{porcentaje:.2f}")
#print("El precio es $" + str(a))
