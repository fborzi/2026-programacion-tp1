a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
SUMA = 0
DIVISION = 0.0
PORCENTAJE = 0
DIVISOR = False

SUMA = a+b 
DIVISION = a/b
PORCENTAJE= a//b 
DIVISOR = a % b == 0 


print("La suma de", a , "y",b, "es:", SUMA)
print("La division de", a , "y" , b , "es:", DIVISION)
print("Es divisor:", DIVISOR )
print("El 10% de",a,"es:", PORCENTAJE)