a= int(input("Ingrese el primer numero:"))
b= int(input("Ingrese el segundo numero:"))

suma = 0
division = 0.0
porcentaje = 0
divisor = False

suma = a + b
division = a / b
porcentaje = a // b 
divisor = a % b == 0 


print("La suma de", a , "y",b, "es:", suma )
print("La division de", a , "y" , b , "es:", division)
print("Es divisor:", divisor )
print("El 10% de",a,"es:", porcentaje)