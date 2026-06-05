"""
Este codigo permite ingresar una cadena de caracteres y mostrarla en pantalla,
muestra la longitud de esta, si contiene la subcadena 'la', reescribe en mayusculas
y muestra la cantidad de vocales minusculas de la cadena.
"""
a = ""
contador = 0
a = input("Ingrese una cadena: ")
print("Longitud de la cadena:",len(a))
if ("la" in a) is True:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la': No")
print("Cadena en mayusculas:",a.upper())
for letra in a:
    if letra in "aeiouàèìòù":
        contador = contador + 1
print("Cantidad de vocales minusculas:",contador)
