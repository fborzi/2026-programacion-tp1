"""
Leer desde teclado una cadena de caracteres y luego

a. Mostrar en pantalla la cadena ingresada. ¿Qué diferencia hay entre mostrarla en el intérprete y mostrarla dentro de un archivo .py?
b. Mostrar la longitud de la misma
c. Indicar si existe en la misma la palabra 'la'.
d. Convertir la cadena a mayúsculas y mostrarla en pantalla.
e. Informar cuántas vocales en minúsculas tiene.
"""

cadena = input("Escribir cadena:")

print("La cantidad de caracteres es: ", len(cadena))

if "la" in cadena:
    print("Contiene 'la': Si")
else: 
    print("Contiene 'la': No")

print(cadena.upper())

vocales = "aeiou"
aux = 0

for letra in vocales:
    if letra in cadena:
        aux += 1

print("Se encontraron ",aux,"vocales.")