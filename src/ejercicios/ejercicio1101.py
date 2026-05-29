"Este modulo resuelve el ejercicio 1101"

cadena = input("ingrese una cadena de texto: ")

print("la longitud de la cadena es: ", len(cadena))

if "la" in cadena.lower():
    print("Contiene 'la: si")
else:
    print("No contiene 'la': no")

print("Cadena en mayúsculas", cadena.upper())

vocales = 0

for letra in cadena:
    if letra in "aeiou":
        vocales = vocales + 1
print("Vocales en minusculas", vocales)
