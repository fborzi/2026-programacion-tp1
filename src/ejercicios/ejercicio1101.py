cadena = input("ingrese una cadena: ")
print("Cadena ingresada:", cadena)
print("la longitud de la cadena es:", len(cadena))
if "la" in cadena:
    print("contiene 'la': si")
else:    print("contiene 'la': no")
print("la cadena en mayusculas es:", cadena.upper())
vocales = 0
for letra in cadena:
    if letra in "aeiou":
        vocales += 1
print("vocales en minusculas:", vocales)
