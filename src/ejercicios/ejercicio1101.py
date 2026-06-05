cadena = input("ingrese una cadena")

print("la longitud de la cadena es:", len(cadena))

if "la" in cadena:
    print('contiene "la": si')
else:
    print('contiene "la": no')
    
print("cadena en mayusculas:", (cadena.upper()))

contador = 0

for letra in cadena:
    if letra in "aeiou":
        contador = 0
print("vocales en minusculas:",contador) 