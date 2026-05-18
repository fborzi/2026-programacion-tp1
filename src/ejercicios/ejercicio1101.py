cadena ="Hola, me llamo Brisa y estoy aprendiendo a usar Visual Studio"
print(cadena)
print("La longitud de la cadena es:", len(cadena))
if "la" in cadena:
    print("la subcadena 'la' se encuentra en la cadena")
print("Hola, me llamo Brisa y estoy aprendiendo a usar Visual Studio".upper())
vocales = 0
for letra in cadena:
    if letra in "aeiou":
        vocales +=1
print("Cantidad de vocales minusculas:", vocales)