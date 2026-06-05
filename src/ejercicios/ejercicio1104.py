FECHA = input()

DIA = ""
MES = ""
ANIO = ""
FORMATO =""

DIA = FECHA[0:2]
MES = FECHA[3:5]
ANIO = FECHA[6:10]

FORMATO = ANIO[2:4] + "-" + MES + "-" + DIA

print("Formato:", FORMATO)
print("El día es:", DIA)
print("El mes es:", MES)
print("El año es:", ANIO)
