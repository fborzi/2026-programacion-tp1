"""
Ejercicio 20
Escribe un programa que solicite al usuario ingresar un texto y luego realice las siguientes operaciones:
1. Imprima la longitud de la cadena ingresada.
2. Verifique si la cadena contiene la palabra "la" (sin importar mayúsculas
    o minúsculas) e imprima un mensaje indicando si la contiene o no.
3. Convierta la cadena a mayúsculas y la imprima.
4. Cuente e imprima la cantidad de vocales que contiene la cadena.
"""
texto: str = input("Escribe un texto: ").casefold()

print("La longitud de la cadena es: ", len(texto))
print("El texto contiene 'la':", "Si" if 'la' in texto else "No")
print("El texto en mayúsculas es:", texto.upper())
vocales: int = 0
for i in texto:
    if i in 'aeiouáéíóú':
        vocales+=1
print("La cantidad de vocales es:", vocales)
