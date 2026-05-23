cadena1=input("ingresa la primera cadena:")
cadena2=input("ingresa la segunda cadena:")
cantidad=cadena1.count(cadena2)
print(cantidad)

cadena3 =(cadena1+cadena2)
print(cadena3.lower())
if cadena1:#verifica que no esta vacía
    letra = cadena1[0]
    cantidad = cadena2.count(letra)
    print(cantidad)
else:
    print(0)



