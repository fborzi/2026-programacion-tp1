""" En este programa se busca trabajar con operaciones matemáticas básicas en Python 
utilizando números enteros ingresados por el usuario. 
El programa:

Solicita dos números.
Realiza cálculos matemáticos con ellos.
Muestra resultados usando mensajes formateados.
Verifica condiciones lógicas usando operadores.
Calcula porcentajes.
Se convierte un numero en cadena."""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("La suma de", a, "y", b, "es:", a + b)

if b != 0:
    division = a / b
else:
    division = 0.0
    print("No se puede dividir por cero")

print("La división de", a, "y", b, "es:", division)

if b != 0:
    es_divisible = a % b == 0
else:
    es_divisible = False

print("Es divisor:", es_divisible)

if b != 0:
    porcentaje = (a * b) // 100
else:
    porcentaje = 0

print("El", str(b) + "% de", a, "es:", porcentaje)


#print("El precio es $"+a) da error porque a es un número y no se puede concatenar directamente con texto.
#lo que le falta es covertir el numero a cadena para que se puedan concatenar, con str().
