a = input("ingrese un numero entero:")
b = input("ingrese otro numero entero:")

c = int(a) + int(b) 
print("la suma de a y b es c",c)

c = int(a) / int(b)
print("la division de a y b es c:",c)

int(a) % int(b) == 0 
print("a es divisible por b:", int(a) % int(b) == 0)

resultado = int(a) * int(b) / 100
print("el porcentaje de a con respecto a b es:", resultado)
#Para que el resultado sea un float hay que hacer la division con una sola barra, ya que con la doble barra se obtiene un resultado entero.

print("El precio es $" + str(a))



