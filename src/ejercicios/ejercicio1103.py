"""1103"""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print(f"La suma de {a} y {b} es: {a + b}")

if b == 0:
    print(f"La división de {a} y {b} es: 0.0")
    print("Es divisor: False")
    print(f"El {b}% de {a} es: 0")
    print("0")  
else:
    print(f"La división de {a} y {b} es: {a / b}")
    
    es_divisor = (a % b == 0)
    print(f"Es divisor: {es_divisor}")
    
    porcentaje_resultado = (b / 100) * a
    if porcentaje_resultado.is_integer():
        porcentaje_resultado = int(porcentaje_resultado)
        
    print(f"El {b}% de {a} es: {porcentaje_resultado}")
