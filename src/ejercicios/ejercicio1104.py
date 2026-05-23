""" el programa valida que la cadena ingresada tenga exactamente 10 caracteres, 
Si la longitud no es correcta, muestra un mensaje de error indicando que el formato no 
es válido
Si la entrada es correcta extraigo los datos necesarios cortando la cadena
Luego realice la trasformacion de ls fecha del formato original y cambie las posiciones"""


fecha = input("ingrese fecha en formato dd/mm/aaaa: ")
if len(fecha) == 10:
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:10]

    print(f"Formato: {anio[2:4]}-{mes}-{dia}")
    print(f"El día es: {dia}")
    print(f"El mes es: {mes}")
    print(f"El año es: {anio}")
else:
    print("Error: el formato debe ser dd/mm/aaaa (exactamente 10 caracteres)")
