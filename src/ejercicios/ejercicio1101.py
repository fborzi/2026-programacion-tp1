"""
Respuesta a: la diferencia en el interprete; es la impresion
del resultado, en el archivo .py; se debe mostrar el resultado con print()

en el ejercicio b Utilicé len(frase) para obtener la longitud de la cadena.
en el ejercicio c utilice frase.lower() para obtener la longitud de la cadena
utilice frase.upper() para convertir la cadena en mayuscula
en el ejercicio d inicialice el contador en 0 para que contara cada vez que se encuentra una vocal,
asi mismo declare la variable vocales para despues buscarlas en el for y contar cuantas veces se encuentra
en la frase ingresada."""

frase = input("Ingrese una frase: ")

print("La longitud de la cadena es:", len(frase))

if "la" in frase.lower():
    print("Contiene 'la': Si")


print("Cadena en mayúsculas:", frase.upper())

VOCALES = "aeiou"
contador = 0

for letra in frase.lower():
    if letra in VOCALES:
        contador += 1

print("vocales en minúsculas:", contador)
