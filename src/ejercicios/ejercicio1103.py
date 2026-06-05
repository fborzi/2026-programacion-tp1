"""ingresar los numeros, la suma de esos numeros es el resultado de C, luego cambia a dividir y C obtiene 
nuevo resultado, te dice si es divisor o no y luego saca el porcentaje"""
A = int(input("Ingrese un número para A: "))
B = int(input("Ingrese un número para B: "))

print(f"La suma de {A} y {B} es: {A + B}")

if B == 0:
    print("No es posible dividir por cero")
    print(f"La división de {A} y {B} es: 0.0")
    print("Es divisor: False")
    print(f"El {B}% de {A} es: 0")   # <- línea que faltaba
else:
    print(f"La división de {A} y {B} es: {A / B}")
    print(f"Es divisor: {A % B == 0}")
    print(f"El {B}% de {A} es: {(A * B) / 100}")

print(str(A) + str(B))  # concatenación
