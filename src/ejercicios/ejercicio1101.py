cadena=input("ingrese un texto o cadena: ")
print(cadena)
print("la longitud de la cadena es: ",len(cadena))
print("la"in cadena)
print("cadena en mayuscua:",cadena.upper())
contador = 0 
for letra in  cadena:
    if letra in "aeiou":
        contador +=1
print("cantidad de vocales minúsculas:")
print(contador)


