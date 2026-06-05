"Este modulo lee una fecha en formato dd/mm/aaaa e informa el dia, mes, año y el formato aa-mm-dd. "
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]
anio_corto = fecha[8:10]

print("Formato:", anio_corto + "-" + mes + "-" + dia)
print("El día es:", dia)
print("El mes es:", mes)
print("El año es:", anio)
