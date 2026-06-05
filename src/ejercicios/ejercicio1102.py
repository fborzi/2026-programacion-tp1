# Leer las dos cadenas
cadena1 = input()
cadena2 = input()

# A) Cantidad de veces que aparece la primera cadena en la segunda
print("Cantidad de veces que aparece:", cadena2.count(cadena1))

# B) Concatenación
cadena2 = cadena2[0].lower() + cadena2[1:]
print("Concatenacion:", cadena1 + cadena2)

# C) Contar la primera letra de la primera cadena en la segunda
letra = cadena1[0]
cantidad = cadena2.count(letra)

print(f'La letra "{letra}" aparece {cantidad} veces en la cadena \'{cadena2}\'')
