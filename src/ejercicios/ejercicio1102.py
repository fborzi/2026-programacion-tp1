palabra=input("Ingrese una palabra: ")
palabra2=input("Ingrese otra palabra: ")
print(palabra)
print(palabra2)
print("Cantidad de veces que aparece: ",palabra.count(palabra2))
print("Concatenacion: ",palabra + palabra2.lower()[0]+palabra2[1:])
primeraletra=palabra[0]
print("La letra '",primeraletra,"' aparece ",primeraletra.count(palabra2),"veces en la cadena",palabra+palabra2)
