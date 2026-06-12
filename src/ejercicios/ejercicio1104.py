fecha = input("Ingrese una fecha:")
              
formato = fecha[8:] + "-" + fecha[3:5] + "-" + fecha[0:2] 
print("Formato:", formato)

día = fecha[0:2]
print("El día es:", día)

mes = fecha[3:5]
print("El mes es:", mes)

año = fecha[6:10]
print("El año es:", año)

print("La fecha invertida es:", formato)
