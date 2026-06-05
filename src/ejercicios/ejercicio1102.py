# Leer las dos cadenas
cadena1 = input()
cadena2 = input()

# Cantidad de veces que aparece la primera cadena en la segunda
cantidad = cadena2.count(cadena1)
print("cantidad de veces que aparece:", cantidad)

# Concatenación de ambas cadenas
cadena2 = cadena2[0].lower() + cadena2[1:]
print("concatenacion:", cadena1 + cadena2)

# Contar cuántas veces aparece la primera letra de la primera cadena en la segunda
letra = cadena1[0]
cantidad_letra = cadena2.count(letra)

print(f'la letra "{letra}" aparece {cantidad_letra} veces en la cadena \'{cadena2}\'')
