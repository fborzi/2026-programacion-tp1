"""Ejercicio 22
Escribe un programa que solicite al usuario ingresar dos números enteros y luego realice las
siguientes operaciones:
1. Calcule e imprima la suma de los dos números.
2. Calcule e imprima la división del primer número entre el segundo. Asegúrate de manejar la división por cero.
3. Determine e imprima si el segundo número es un divisor del primero.
4. Calcule e imprima el porcentaje que representa el segundo número del primero.
"""


num_1: int = int(input("Ingrese el numero 1: "))
num_2: int = int(input("Ingrese el numero 2: "))

suma: int = num_1 + num_2
division: float = 0.0
es_divisor: bool = False
porcentaje: int = 0


if num_2 != 0:
    division = num_1 / num_2
    es_divisor = num_1 % num_2 == 0
    porcentaje = (num_2 * num_1) // 100
else:
    print("No se puede dividir por cero.")

print("La suma de los dos numeros es:", suma)
print(f"La division de {num_1} entre {num_2} es:", division)
print("¿El numero 2 es divisor del numero 1:", es_divisor)
print(f"El {num_2} % de {num_1} es:", porcentaje, "%")
