"""Este ejercicio se trata de ingresar dos numeros de 
teclado y luego realizar varias operaciones con ellos,como sumarlos,dividirlos,etc"""

numero1=input("Ingrese el primer numero: ")
numero2=input("Ingrese el segundo numero: ")

suma=int(numero1)+int(numero2)
print("La suma de ",numero1," y ",numero2," es : ",suma)

division=float(numero1)/float(numero2)
print("La division de ",numero1," y ",numero2," es : ",division)


if int(numero1)%int(numero2)==0:
    print("Es divisor: True")
else:
    print("Es divisor: False")

suma=int(numero1)+int(numero2)
porcentaje=suma*0.10
print("El 10% de ",numero1," es: ",porcentaje)