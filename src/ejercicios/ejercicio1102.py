a = input("Ingrese la primera cadena: ")
b = input("Ingrese le segunda cadena: ")
contador = 0
print(a)
print(b)
for a in a:
    if b in a:
        contador = contador + 1
print(contador)