"""Ejercicio 1103 - Operaciones matemáticas y formato."""
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print("La suma de", a, "y", b, "es:", a + b)
print("La división de", a, "y", b, "es:", a / b)
print("Es divisor:", a % b == 0)
print("El " + str(b) + "% de " + str(a) + " es:", int(a * b / 100))
