primerNumero = int(input("ingrese el primer numero: "))
segundoNumero = int(input("ingrese el segundo numero: "))

suma = primerNumero + segundoNumero
print("la suma de ", primerNumero, "y", segundoNumero, "es:", suma)

if segundoNumero != 0:
    division = primerNumero / segundoNumero
    print("La division de", primerNumero, "y", segundoNumero, "es:", division)
else:
    print("no se puede dividir por cero")

if segundoNumero !=0:
    esDivisor = primerNumero % segundoNumero == 0
else:
    esDivisor = False
    
print(esDivisor)

porcentaje = primerNumero * segundoNumero /100
print(porcentaje)