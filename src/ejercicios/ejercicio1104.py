fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]
aa = anio[-2]
print("Formato:", aa + "-" + mes + "-" + dia)
print("El dia es:", dia)
print("El mes es:", mes)
print("El anio es:", anio)
