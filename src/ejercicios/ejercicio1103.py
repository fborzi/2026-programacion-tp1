"""El codigo realiza operaciones matematicas con dos numeros enteros"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = a + b
print("La suma de", a, "y", b, "es:", suma)

if b != 0:
    division = a / b
    es_divisor = (b % a == 0)
else:
    print("No es posible dividir por cero")
    division = 0.0
    es_divisor = False

print("La division de", a, "y", b, "es:", division)
print("Es divisor:", es_divisor)

porcentaje = b * a / 100
if porcentaje.is_integer():
    porcentaje = int(porcentaje)

print("El", b, "% de", a, "es:", porcentaje)

#Para mostrar el resultado con decimales seria: 
#print("El", b, "% de", a, "es:", f"{porcentaje:.2f}")

#print("El precio es $" + str(a))