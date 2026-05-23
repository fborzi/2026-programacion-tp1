cadena = input()

print("cadena ingresada:", cadena)
print(len(cadena))

if "la" in cadena:
    print('contiene "la": si')
else:
    print('contiene "la": no')
    
print("cadena en mayusculas:", (cadena.upper()))


contador = 0
for letra in cadena:
    if letra in "aeiou":
        contador = contador + 1
print("vocales en minusculas:",contador) 