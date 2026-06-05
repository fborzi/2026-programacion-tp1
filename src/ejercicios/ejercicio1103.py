SUMA = 0
DIVISION = 0.0
PORCENTAJE = 0.0 

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))

print("La suma de", a , "y", b ,"es:", a + b)

if b != 0:
  print("La division de", a ,"y", b , "es:", a / b)
  print("Es divisor:", a % b == 0)
else:
 print("No es posible dividir por cero")
 print("La división de", a, "y", b ,"es:", 0.0)
 print("Es divisor:", False)

print("El", b, "% de", a, "es:", int(a * b / 100))