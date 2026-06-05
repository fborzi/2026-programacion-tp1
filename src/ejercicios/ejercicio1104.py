fecha = input("ingrese una fecha (dd/mm/aaaa):")

dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:10]

print("formato:", año[2:4] + "-" + mes + "-" + dia)
print("El dia es:", dia)
print("El mes es:", mes)
print("El año es:", año)



