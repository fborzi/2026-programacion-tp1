"""
Programa para realizar operaciones matemáticas básicas y porcentajes.
"""

num1 = input()
num2 = input()

n1 = int(num1)
n2 = int(num2)

suma = n1 + n2
print(f"La suma de {n1} y {n2} es: {suma}")

if n2 == 0:
    print(f"La división de {n1} y {n2} es: 0.0")
    print("Es divisor: False")
else:
    division = n1 / n2
    es_divisor = (n1 % n2 == 0)
    print(f"La división de {n1} y {n2} es: {division}")
    print(f"Es divisor: {es_divisor}")


porcentaje = n1 * (n2 / 100)
print(f"El {n2}% de {n1} es: {int(porcentaje)}")
