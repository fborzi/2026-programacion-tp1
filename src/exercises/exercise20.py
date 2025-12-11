texto: str = input("Escribe un texto: ").casefold()

print("La longitud de la cadena es: ", len(texto))
print("El texto contiene 'la':", "Si" if 'la' in texto else "No")
print("El texto en mayúsculas es:", texto.upper())
vocales: int = 0
for i in texto:
    if i in 'aeiouáéíóú':
        vocales+=1
print("La cantidad de vocales es:", vocales)
