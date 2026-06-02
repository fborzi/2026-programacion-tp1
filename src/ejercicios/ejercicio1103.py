"""ingresar los numeros, la suma de esos numeros es el resultado de C, luego cambia a dividir y C obtiene 
nuevo resultado, te dice si es divisor o no y luego saca el porcentaje"""
A=input("ingrese un numero para A: ")
B=input("ingrese un numero para B: ")

A=int(A)
B=int(B)

C = A + B 

print("La suma de", A, "y", B, "es:", C)
if B != 0:
    C = A / B
else:
    C = 0

print("La división de", A, "y", B, "es:", C)

print("Es divisor:", B % A == 0)

C = (A * B) // 100
print("el",B,"%", "de", A , "es:", C)
print("El precio es $" + str(A))