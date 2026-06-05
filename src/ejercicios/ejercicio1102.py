"Este modulo lee una cadena de texto y muestra la cantidad de veces que aparece una subcadena, la concatenación de ambas cadenas y la cantidad de veces que aparece la primera letra de la primer cadena en la segunda cadena."

a = input("Introduzca una cadena de caracteres: ")
b = input("Introduzca una nueva cadena de caracteres: ")

cantidaddeveces = b.count(a)
primeraletra = a[0]
cantidad2 = b.lower().count(primeraletra.lower())

print("Cantidad de veces que aparece:", cantidaddeveces)
print(f"Concatenación: {a.lower()}{b.lower()}")

if cantidad2 == 1:
    print(
        f"La letra '{primeraletra}' aparece {cantidad2} vez en la cadena '{b}'")
else:
    print(
        f"La letra '{primeraletra}' aparece {cantidad2} veces en la cadena '{b}'")
