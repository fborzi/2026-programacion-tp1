palabra=input("Ingrese una palabra: ")
print(palabra)
print("La longitud de la cadena es: ",len(palabra))
if "la" in palabra:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la':No")
print('Cadena en mayúsculas :', palabra.upper())
contador = 0
for letra in palabra:
    if letra.lower() in "aeiou":
        contador += 1
print("Vocales en minuscula: ",contador)