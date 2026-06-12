cadena ="Hola"
print(cadena)
print("La longitud de la cadena es:", len(cadena))
if "la" in cadena:
    print("Contiene 'la': SI")
else:
    print("Contiene 'la': NO")
print("Cadena en mayúsculas:","Hola".upper())
vocales = 0
for letra in cadena:
    if letra in "aeiou":
        vocales +=1
print("Vocales minusculas:", vocales)