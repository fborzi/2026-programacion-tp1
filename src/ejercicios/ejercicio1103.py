"""ingresar los numeros, la suma de esos numeros es el resultado de C, luego cambia a dividir y C obtiene 
nuevo resultado, te dice si es divisor o no y luego saca el porcentaje"""
a = int(input("ingrese valor de a:"))
b = int(input("ingrese valor de b:"))

c = a + b
print("La suma de", a, "y", b, "es:", c)

if b != 0:
    division_c = a / b
    print("La división de", a, "y", b, "es:", division_c)
    es_divisor = (a % b == 0)
    print("Es divisor:", es_divisor)
else:
    print("No se puede dividir por cero")

porcentaje = a * b / 100
print("El", str(b) + "%", "de", a, "es:", porcentaje)