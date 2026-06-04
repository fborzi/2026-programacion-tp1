a = int(input("Escriba el valor de a: "))
b = int(input("Escriba el valor de b: "))

suma = a + b
print("La suma de", a, "y", b, "es:", suma)

if b == 0:
    print("La división de", a, "y", b, "es: No se puede dividir por cero")
    print("Es divisor: False")
else:
    division = a / b
    print("La división de", a, "y", b, "es:", division)
    
    es_divisor = a % b == 0
    print("Es divisor:", es_divisor)

porcentaje = int(a * 0.10)
print("El 10% de", a, "es:", porcentaje)
