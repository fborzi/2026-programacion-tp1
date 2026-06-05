"""ingresar los numeros, la suma de esos numeros es el resultado de C, luego cambia a dividir y C obtiene 
nuevo resultado, te dice si es divisor o no y luego saca el porcentaje"""
a = int(input())
b = int(input())
c = a + b
print("La suma de", a, "y", b, "es:", c)

division_c = a / b
print("La división de", a, "y", b, "es:", division_c)
es_divisor = (b % a == 0)
print("Es divisor:", es_divisor)
porcentaje = a * b / 100
print("El", str(b) + "%", "de", a, "es:", porcentaje)