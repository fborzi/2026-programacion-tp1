"""Ejercicio 1103."""

a = int(input())
b = int(input())

print("la suma de", a, "y", b, "es:", a + b)

if b != 0:
    print("la division de", a, "y", b, "es:", a / b)
    print("es divisor:", a % b == 0)
    print("el", b, "% de", a, "es:", (a * b) // 100)
else:
    print("no es posible dividir por cero")
    print("la division de", a, "y", b, "es:", 0)
    print("es divisor:", False)
    print("el", b, "% de", a, "es:", 0)
