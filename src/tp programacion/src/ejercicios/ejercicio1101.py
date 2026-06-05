# Análisis de una cadena

# Leer cadena desde teclado
cadena = input("Ingrese una cadena de caracteres: ")

# a) Mostrar la cadena ingresada
print("\nCadena ingresada:")
print(cadena)

# Diferencia entre intérprete y archivo .py
print("\nDiferencia:")
print("En el intérprete, Python muestra automáticamente el resultado.")
print("En un archivo .py es necesario usar print() para mostrarlo.")

# b) Mostrar la longitud
print("\nLongitud de la cadena:")
print(len(cadena))

# c) Indicar si existe la palabra 'la'
if "la" in cadena:
    print("\nLa palabra 'la' existe en la cadena.")
else:
    print("\nLa palabra 'la' NO existe en la cadena.")

# d) Convertir a mayúsculas
print("\nCadena en mayúsculas:")
print(cadena.upper())

# e) Contar vocales minúsculas
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra in vocales:
        contador += 1

print("\nCantidad de vocales minúsculas:")
print(contador)# Análisis de una cadena

# Leer cadena desde teclado
cadena = input("Ingrese una cadena de caracteres: ")

# a) Mostrar la cadena ingresada
print("\nCadena ingresada:")
print(cadena)

# Diferencia entre intérprete y archivo .py
print("\nDiferencia:")
print("En el intérprete, Python muestra automáticamente el resultado.")
print("En un archivo .py es necesario usar print() para mostrarlo.")

# b) Mostrar la longitud
print("\nLongitud de la cadena:")
print(len(cadena))

# c) Indicar si existe la palabra 'la'
if "la" in cadena:
    print("\nLa palabra 'la' existe en la cadena.")
else:
    print("\nLa palabra 'la' NO existe en la cadena.")

# d) Convertir a mayúsculas
print("\nCadena en mayúsculas:")
print(cadena.upper())

# e) Contar vocales minúsculas
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra in vocales:
        contador