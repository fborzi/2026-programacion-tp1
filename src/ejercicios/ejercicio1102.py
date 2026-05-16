"""a. Utilicé find() para buscar cuántas veces aparece la segunda cadena
dentro de la primera cadena y un while para repetir la búsqueda
hasta que no existan más coincidencias.

b. Utilicé lower() para convertir las cadenas a minúsculas
y luego concatenarlas en una nueva variable.

c. Guardé la primera letra de la primera cadena en una variable,
utilicé un for para recorrer la segunda cadena y lower() para
comparar las letras sin importar mayúsculas o minúsculas.
Cada vez que encontraba coincidencias aumentaba el contador."""


cadena1 = input("ingrese la primera cadena:")
cadena2 = input("ingrese la segunda cadena:")

contador = 0
cantidad = cadena1.find(cadena2)

while cantidad != -1:
    contador += 1
    cantidad = cadena1.find(cadena2, cantidad + 1)

print("Cantidad de veces que aparece:", contador)


cadenaNueva = cadena1.lower() + cadena2.lower()
print("Concatenación:", cadenaNueva)


primera_letra = cadena1[0]
contador = 0

for x in cadena2:
    if x.lower() == primera_letra.lower(): 
        contador += 1   

   
print("La letra: " + primera_letra + " aparece " +  str(contador)  + " veces en la cadena " + cadena2)
