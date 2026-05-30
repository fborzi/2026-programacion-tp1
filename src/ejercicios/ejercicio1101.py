"""El codigo analiza una cadena de textopara calcular su longitud, 
buscar una cadena, convertirla a mayusculas y contar sus vocales 
minusculas"""

cadena = input("Ingrese una cadena: ")

longitud = len(cadena)
print("La longitud de la cadena es:", longitud)

contiene_la = 'la' in cadena
if contiene_la:
    resultado_la = "Si"
else:
    resultado_la = "No"

print("Contiene 'la':", resultado_la)

cadena_mayusculas = cadena.upper()
print("Cadena en mayusculas:", cadena_mayusculas)

vocales = 0
for letra in cadena:
    if letra in "aeiou":
        vocales += 1

print("Vocales en minusculas:", vocales)

