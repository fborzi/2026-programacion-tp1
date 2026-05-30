""" En este programa se busca trabajar con operaciones matemáticas básicas en Python 
utilizando números enteros ingresados por el usuario. 
El programa:

Solicita dos números.
Realiza cálculos matemáticos con ellos.
Muestra resultados usando mensajes formateados.
Verifica condiciones lógicas usando operadores.
Calcula porcentajes.
"""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = 0
division = 0.0
es_divisible = False
porcentaje = 0

suma = a + b


if b != 0:
    division = a / b
    es_divisible = a % b == 0
    porcentaje = (a * b) // 100
else:
    print("No se puede dividir por cero")


print("La suma de", a, "y", b, "es:", a + b)
print("La división de", a, "y", b, "es:", division)
print("Es divisor:", es_divisible)
print("El", str(b) + "% de", a, "es:", porcentaje)
#print(f"El {b}% de {a} es {porcentaje:.2f}")

#print("El precio es $"+a) da error porque a es un número y no se puede concatenar directamente con texto.
#lo que le falta es covertir el numero a cadena para que se puedan concatenar, con str().
#el ultimo print me devuelve un numero con dos decimales
