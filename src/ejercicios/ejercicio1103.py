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

suma = a + b
print("La suma de", a, "y", b, "es:", suma)

division = a / b
print("La división de", a, "y", b, "es:", division)

es_divisor = a % b == 0
print("Es divisor:", es_divisor)

porcentaje = (a * b) / 100
print("El", b, "% de", a, "es:", porcentaje)
#el resultado cuando uso / , la division ya devuelve un numero decimal(float) aunque el resultado sea exacto.

#print("El precio es $"+a) da error porque a es un número y no se puede concatenar directamente con texto.
#lo que le falta es covertir el numero a cadena para que se puedan concatenar, con str().
print("El precio es $" + str(a))