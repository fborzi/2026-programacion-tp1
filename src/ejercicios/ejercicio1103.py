a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
SUMA = 0
DIVISION = 0.0
PORCENTAJE = 0
DIVISOR = False

SUMA = a+b 
if b != 0:
 DIVISION = a/b
 DIVISOR = a % b == 0 
else:
 print("No es posible dividir por cero")
PORCENTAJE = a//10


print("La suma de", a , "y",b, "es:", SUMA)
print("La división de", a , "y" , b , "es:", DIVISION)
print("Es divisor:", DIVISOR )
print("El 10% de",a,"es:", PORCENTAJE)