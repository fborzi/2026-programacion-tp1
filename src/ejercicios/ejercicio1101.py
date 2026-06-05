cadena=input("ingrese una cadena:")
print(cadena)

print("la longitud de la cadena es:", len(cadena))

if "la" in cadena: print("la cadena contiene la palabra la")
else: print("la palabra no se encuentra en la cadena")

print("cadena en mayusculas:", cadena.upper())

vocales= 0
for letra in cadena:
    if letra in "aeiou":
        vocales += 1

print("Vocales en minusculas", vocales)
