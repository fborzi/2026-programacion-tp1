cadena = input("ingrese una cadena: ") 

print("la longitud de la cadena es:", len(cadena))
if "la" in cadena:
    print("la cadena contiene la palabra 'la'")
else:
    print("la cadena no contiene la palabra 'la'")
    
    
print("la cadena en mayusculas es:", cadena.upper())

vocales = 0
for letra in cadena:
 if letra in "aeiou":
    vocales += 1

    
print("vocales en minusculas:", vocales)







