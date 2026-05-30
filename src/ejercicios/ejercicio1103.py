"""El codigo realiza operaciones matematicas con dos numeros enteros"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = a + b
print("La suma de", a, "y", b, "es:", suma)

division = a / b 
print("La division de", a, "y", b, "es:", division) 

es_divisor = (a % b == 0) 
print("Es divisor:", es_divisor)

porcentaje = (b * a) / 100
if porcentaje.is_integer():
    porcentaje = int(porcentaje)
print("El", b, "% de", a, "es:", porcentaje)
#Para mostrar el resultado con decimales seria: 
#print("El", b, "% de", a, "es:", f"{porcentaje:.2f}")

print("El precio es $" + str(a))