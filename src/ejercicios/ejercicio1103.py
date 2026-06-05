"""ingresar los numeros, la suma de esos numeros es el resultado de C, luego cambia a dividir y C obtiene 
nuevo resultado, te dice si es divisor o no y luego saca el porcentaje"""
a=int(input("ingrese valor de a:"))
b=int(input("ingrese valor de b:"))

c=a+b
print("La suma de", a, "y", b, "es:", c)

if b != 0:
    division = a / b
    entero = a % b == 0
else:
    print("No se puede dividir por cero")
    division = 0.0
    entero = False

print("La división de", a, "y", b, "es:", division)
print("Es divisor:", entero)

porcentaje = a * b / 100

if porcentaje.is_integer():
    porcentaje = int(porcentaje)
    print("El",str(b) + "%", "de", a, "es:",porcentaje)
