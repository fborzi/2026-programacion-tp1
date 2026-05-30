"""Este programa permite ingresar dos numeros por teclado para mostrar la suma de ambos, la division del primer numero por el segundo, si es posible dividir el primer numero por el segundo y el porcentaje del segundo numero en el primero"""
a = 0
b = 0
c = 0
d = 0.0
e = 0.0
f = 0.0
a = int(input("Ingrese el primer nùmero: "))
b = int(input("Ingrese el segundo nùmero: "))
c = a + b
d = a / b
e = a % b
f = (b / 100) * a
print("La suma de",a,"y",b,"es:",c)
print("La divisiòn de",a,"y",b,"es:",d)
print("Es divisòr:",e == 0)
print("El",b,"%"" de",a,"es:",f)
print("El precio es $",+a)
print("El",b,"%"" de",a,"es:",f"{f:.2f}")