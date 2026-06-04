texto= input("Ingrese una texto: ")
print("la longitud de la cadena es:", len(texto))
if "la" in texto:
    print("contiene 'la': si")
else:
    print("contiene 'la': no")
print("cadena en mayuscula:", texto.upper())
vocales = 0
for letra in texto:
    if letra in "aeiou":
        vocales += 1
print("vocales en minusculas:",vocales)