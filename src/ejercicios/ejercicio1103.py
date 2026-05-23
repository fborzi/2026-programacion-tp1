primerNumero = int(input("ingrese el primer numero: "))
segundoNumero = int(input("ingrese el segundo numero: "))

suma = primerNumero + segundoNumero
print("la suma de ", primerNumero, "y", segundoNumero, "es:", suma)

division = primerNumero / segundoNumero
print("la division de ", primerNumero, "y", segundoNumero, "es:", division)

esDivisor = primerNumero != 0 and segundoNumero % primerNumero == 0
print("es divisor", esDivisor)

porcentaje = primerNumero * segundoNumero / 100
print("porcentaje es :", porcentaje)

print("el precio es $", primerNumero)