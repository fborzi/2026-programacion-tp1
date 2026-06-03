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
d = a * b / 100,
dint = int(d[0])
print("La suma de ", a, " y ", b, " es: ", suma)

print("La división de", a, " y ", b, " es: ", division)

if a % b == 0:
    print("Es divisor: True")
else:
    print("Es divisor: False")

print("El ", b, "% de ", a, " es: ", dint)
