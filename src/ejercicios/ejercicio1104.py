fecha = input (" ingrese dd/mm/aaaa: ") 
dia =  fecha[0:2]
mes =  fecha[3:5]
anio = fecha[6:10]
anio_corto = fecha[8:10]
print("Formato:", anio_corto + "-" + mes + "-" + dia) 
print("El dia es:", dia)
print("El mes es:", mes)
print("El año es:", anio)

