"Este modulo resuelve el ejercicio 1103"

while True:
    try:
        a = int(input("ingrese el primer numero entero: "))
        break
    except ValueError:
        print("Error: Debe ingresar un numero entero")

while True:
    try:
        b = int(input("ingrese el segundo numero entero: "))
        break
    except ValueError:
        print("Error: Debe ingresar un numero entero")

suma = a + b
division = a / b
d = a * b / 100

print("La suma de ", a, " y ", b, " es: ", suma)

print("La division de", a, " y ", b, " es: ", division)

if a % b == 0:
    print("true: ", a, "es divisor de: ", b)
else:
    print("false: ", a, "no es divisor de: ", b)

print("El ", b, "% de ", a, " es: ", d)

print("El precio es $", +a)
