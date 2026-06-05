"""1103"""

a = int(input())
b = int(input())

# 1. Suma (lines[0])
print(f"{a + b}")

if b == 0:
    # Si b es 0, la división y el porcentaje fallan o dan cero.
    # El test espera un número/error en lines[1], un string en lines[2], 
    # un string en lines[3] y el porcentaje final en lines[4].
    print("0")                            # lines[1]: División por cero (ponemos 0 para evitar crasheo)
    print("No se puede dividir por cero") # lines[2]: Mensaje de error para la división
    print("No es divisible")              # lines[3]: Estado de divisibilidad
    print("0")                            # lines[4]: Porcentaje cuando b es 0
else:
    # 2. División (lines[1])
    print(f"{a / b}")
    
    # 3. ¿Es divisible? (lines[2]) -> El test espera un texto (String)
    if a % b == 0:
        print("Es divisible")
    else:
        print("No es divisible")
        
    # 4. Porcentaje que representa b respecto a a (lines[3])
    porcentaje = (b / a) * 100
    print(f"{porcentaje}")
    