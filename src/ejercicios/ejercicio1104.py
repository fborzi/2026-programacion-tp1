"""ingrese una fecha,se muestra la fecha desde el año hasta el dia,
luego por orden"""
fecha = input("ingrese una fecha (dd/mm/aaaa):")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

print("formato:", anio[2:4] + "-" + mes + "-" + dia)
print("El dia es:", dia)
print("El mes es:", mes)
print("El anio es:", anio)
