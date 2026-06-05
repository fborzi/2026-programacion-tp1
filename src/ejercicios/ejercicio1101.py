"""Este ejercicio se trata de ingresar una cadena desde el teclado 
y luego realizar varias operaciones con ella, como calcular su longitud,ver si tiene un caracter espe
cifico,convertirla a mayusculas,etc."""

palabra=input()

print("La longitud de la cadena es: ",len(palabra))


if "la" in palabra:
    print("Contiene 'la': Si")
else:
    print("Contiene 'la': No") 
print('Cadena en mayúsculas :',palabra.upper())


contador = 0
for letra in palabra:
    if letra in "aeiou":
        contador += 1
print("Vocales en minúscula: ",contador)
