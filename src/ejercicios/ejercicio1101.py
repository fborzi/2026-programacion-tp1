texto = input("Ingrese una texto: ")

# Si la salida esperada pide solo los valores limpios:
print(len(texto))

if "la" in texto:
    print("si")
else:
    print("no")

print(texto.upper())
print("vocales en minusculas:", sum(1 for letra in texto if letra in "aeiou"))