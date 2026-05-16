"""
Este programa analiza una cadena de caracteres ingresada
por el usuario.

El programa:
1) Muestra la cadena ingresada.
2) Informa su longitud.
3) Verifica si contiene la palabra "la".
4) Convierte el texto a mayúsculas.
5) Cuenta cuántas vocales minúsculas tiene.
"""
cadena = input("Ingresá una cadena de caracteres: ")
print(cadena)

print("Cadena ingresada:")
print(cadena)


print("Longitud de la cadena:")
print(len(cadena))

if "la" in cadena:
    print("La palabra 'la' existe en la cadena.")
else:
    print("La palabra 'la' NO existe en la cadena.")


print("Cadena en mayúsculas:")
print(cadena.upper())


contador = 0

for letra in cadena:
    if letra in "aeiou":
        contador += 1

print("Cantidad de vocales minúsculas:")
print(contador)