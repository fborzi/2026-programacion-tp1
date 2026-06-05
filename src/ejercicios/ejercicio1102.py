"""Ejercicio 1102 - Operaciones con dos cadenas."""
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
print("Cantidad de veces que aparece:", cadena2.count(cadena1))
concatenacion = cadena1.lower() + cadena2[0].lower() + cadena2[1:]
print("Concatenación:", concatenacion)
cantidad = 0
for letra in cadena1:
    cantidad += cadena2.count(letra)
print("cantidad de letras de cadena1 que aparecen en cadena2:", cantidad)