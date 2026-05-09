"""Leer desde teclado una cadena de caracteres y luego:
a. Mostrar en pantalla la cadena ingresada.
 ¿ Qué diferencia hay entre mostrarla en el intérprete
y mostrarla dentro de un archivo .py?
b. Mostrar la longitud de la misma.
c. Indicar si existe en la misma la palabra 'la'.
d. Convertir la cadena a mayúsculas y mostrarla en pantalla.
e. Informar cuántas vocales en minúsculas tiene."""


frase = "Hola"

print(len(frase)) #longitud de la cadena, respuesta B.

print("la" in "Hola") # Busqueda de "la" dentro de la cadena, respuesta C.

print(frase.upper()) # Conversion en minuscula de la cadena, respuesta D.

#respuesta E
vocales = "aeiou" # Aqui defini las vocales en minuscula para luego buscarlas.
contador = 0 # para que el conteo arranque en cero.
for letra in frase: # comienzo un bucle de busqueda para encontrar las vocales.
    if letra in vocales: # condicione si la letra esta en las vocales declaradas:
        contador += 1 # si ;a consigue le sumo 1 al contador.
print("la cantidad de vocales en minuscula es:" , contador) # mostre el resultado en pantalla 

"""Respuesta a: la diferencia en el interprete; es la  impresion
del resultado, en el archivo .py; se debe mostrar el resultado con print() """
