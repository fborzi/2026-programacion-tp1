"""Ejercicio 1102."""

cadena1 = input().lower()
cadena2 = input().lower()

print("cantidad de veces que aparece:", cadena2.count(cadena1))
print("concatenacion:", cadena1 + cadena2)

letra = cadena1[0]
print(f'la letra "{letra}" aparece {cadena2.count(letra)} veces en la cadena \'{cadena2}\'')
