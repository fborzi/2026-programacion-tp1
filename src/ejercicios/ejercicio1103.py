primerNumero = int(input("ingrese el primer numero: "))
segundoNumero = int(input("ingrese el segundo numero: "))

suma = primerNumero + segundoNumero
print("la suma de ", primerNumero, "y", segundoNumero, "es:", suma)

if segundoNumero != 0:
    division = primerNumero / segundoNumero
    print("La division de", primerNumero, "y", segundoNumero, "es:", division)
else:
    print("La division de", primerNumero, "y", segundoNumero, "es: No se puede dividir por cero")

esDivisor = segundoNumero != 0 and primerNumero / 100
print("es divisor", esDivisor)

porcentaje = int(primerNumero * segundoNumero / 100)
print("El", segundoNumero, "% de", primerNumero, "es:" , porcentaje)

print("el precio es $" + str(primerNumero))