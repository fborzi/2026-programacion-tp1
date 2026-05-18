fecha = input("Ingrese una fecha: ")

dia = fecha[0:2]
print("El dia es:", dia)

mes = fecha[3:5]
print("El mes es:", mes)

año = fecha[6:10]
print("El año es:", año)

print("La fecha invertida es:", año + "/" + mes + "/" + dia)
