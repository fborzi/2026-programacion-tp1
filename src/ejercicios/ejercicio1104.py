a = ""
anio = ""
mes = ""
dia = ""
a = input("Ingrese la fecha (dd/mm/aaaa): ")
anio = a[8:]
mes = a[3:5]
dia = a[0:2]
print("Formato:",anio+"-"+mes+"-"+dia)
print("El dia es:",dia)
print("El mes es:",mes)
print("El año es:",a[6:])