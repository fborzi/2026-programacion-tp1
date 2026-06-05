"""Ejercicio 1103."""

a = int(input())
b = int(input())

print("la suma de", a, "y", b, "es:", a + b)

if b != 0:
    print("la division de", a, "y", b, "es:", a / b)
    print("es divisor:", str(a % b == 0).lower())
else:
    print("la division de", a, "y", b, "es: no se puede dividir por cero")
    print("es divisor: false")

print("el", b, "% de", a, "es:", (a * b) / 100)
