"""a. Utilicé find() para buscar cuántas veces aparece la segunda cadena
dentro de la primera cadena y un while para repetir la búsqueda
hasta que no existan más coincidencias.

b. Utilicé lower() para convertir las cadenas a minúsculas
y luego concatenarlas en una nueva variable.

c. Guardé la primera letra de la primera cadena en una variable,
utilicé un for para recorrer la segunda cadena y lower() para
comparar las letras sin importar mayúsculas o minúsculas.
Cada vez que encontraba coincidencias aumentaba el contador."""


cadena1 = input("ingrese la primera cadena: ")
cadena2 = input("ingrese la segunda cadena: ")

contador_cadena = 0
cantidad = cadena2.find(cadena1)

while cantidad != -1:
    contador_cadena += 1
    cantidad = cadena2.find(cadena1, cantidad + 1)
print("Cantidad de veces que aparece:", contador_cadena)

cadena_nueva = cadena1.lower() + cadena2.lower()
print("Concatenación:", cadena_nueva)

primera_letra = cadena1[0]
contador_letras = 0

for letra in cadena2:
    if letra.lower() == primera_letra.lower(): 
        contador_letras += 1   

print("La letra: '" + primera_letra + "' aparece " +  str(contador_letras)  + " veces en la cadena '" + cadena2 + "'")
