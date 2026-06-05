"Este modulo opera con dos enteros: suma, division, divisibilidad y porcentaje."
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
print(f"La suma de {a} y {b} es: {suma}")
if b == 0:
    print(f"La división de {a} y {b} es: 0")
    print("Es divisor: False")
    print(f"El {b}% de {a} es: 0")
else:
    division = a / b
    dint = int(a * b / 100)
    print(f"La división de {a} y {b} es: {division}")
    if a % b == 0:
        print("Es divisor: True")
    else:
        print("Es divisor: False")
    print(f"El {b}% de {a} es: {dint}")
