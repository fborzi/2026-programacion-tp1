# Leer una cadena desde el teclado
cadena = input()

# Mostrar la longitud de la cadena
print("La longitud de la cadena es", len(cadena))

# Verificar si contiene la palabra "la"
if "la" in cadena:
    print("Contiene 'la': si")
else:
    print("Contiene 'la': no")

# Convertir la cadena a mayúsculas
print("Cadena en mayuscula:", cadena.upper())

# Contar vocales minúsculas
vocales = 0

for letra in cadena:
    if letra in "aeiou":
        vocales += 1

print("Vocales en minuscula:", vocales)
