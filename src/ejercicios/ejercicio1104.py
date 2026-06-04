fecha = input("Ingrese la fecha (dd/mm/aaaa): ")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

anio_corto = fecha[8:10]

print("Formato:", f"{anio_corto}-{mes}-{dia}")
print("dia:", dia)
print("mes:", mes)
print("año:", anio)