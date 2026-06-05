fecha = input("Ingrese una fecha (dd/mm/aaaa): ")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

print("El día es:", dia)
print("El mes es:", mes)
print("El año es:", anio)

print("Formato:", anio[2:4] + "-" + mes + "-" + dia)
