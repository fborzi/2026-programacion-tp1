# Ingreso de dos números enteros

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# a) Suma
suma = a + b
print("La suma de", a, "y", b, "es:", suma)

# b) División
division = a / b
print("La división de", a, "y", b, "es:", division)

# c) Verificar si el primero es divisor del segundo
es_divisor = (a % b == 0)

print("Es divisor:", es_divisor)

# d) Calcular el porcentaje
porcentaje = (a * b) / 100

print("El", b, "% de", a, "es:", porcentaje)

# e) Mostrar texto sin errores
# Hay que convertir el número a cadena usando str()

print("El precio es $" + str(a))