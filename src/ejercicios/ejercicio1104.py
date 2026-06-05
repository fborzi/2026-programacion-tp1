fecha = input("Ingrese una fecha con formato dd/mm/aaaa: ")

dia = fecha[0:2]
mes = fecha[3:5]
anio = fecha[6:10]

anio_corto = anio[2:4]

fecha_nueva = anio_corto + "-" + mes + "-" + dia

print("Formato:", fecha_nueva) 

print("El dia es:", dia)
print("El mes es:", mes)
print("El año es:", anio)