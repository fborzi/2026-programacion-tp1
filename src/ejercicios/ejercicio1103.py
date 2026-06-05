"""ingresar los numeros, la suma de esos numeros es el resultado de C, luego cambia a dividir y C obtiene 
nuevo resultado, te dice si es divisor o no y luego saca el porcentaje"""
A=input("ingrese un numero para A: ")
B=input("ingrese un numero para B: ")
A=int(A)
B=int(B)
C = A + B 
print("La suma de", A, "y", B, "es:", C)
if B == 0:
    print("No es posible dividir por cero")
    print("La división de", A, "y", B, "es:", 0.0)
    print("Es divisor:", False)
else:
    print("La división de", A, "y", B, "es:", A / B)
    print("Es divisor:", A % B == 0)
print(f"El {B}% de {A} es: {(A * B) // 100}")
