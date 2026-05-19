"""a. Utilicé operadores aritméticos para realizar la suma de ambos números
y mostrar el resultado utilizando f-strings.

b. Utilicé el operador de división para mostrar el resultado de dividir
ambos números y una validación para evitar dividir por cero.

c. Utilicé el operador módulo (%) para verificar si el primer número
es divisor del segundo.

d. Utilicé una fórmula porcentual para calcular el porcentaje del segundo
número respecto al primero y :.2f para mostrar el resultado con dos decimales. el formato de salida
del ejercicio era un int pero nos sabia donde querias la respuesta cuando lo transformas a decimales

e. Si a es una variable que contiene uno de los números ingresados, ¿qué le falta a la siguiente 
instrucción para que muestre el texto sin errores? print("el precio es$"+a) : deberia convertir la a en en una cadena 
de texto utilizando str porque no se puede concatenar un int y un str, quedaria: print("el precio es$"+str(a))"""

a = int(input("ingrese el primer número entero: "))
b = int(input("ingrese el segundo número entero: "))

print(f"La suma de {a} y {b} es: {a + b}")

if b != 0:
    print(f"La división de {a} y {b} es: {a / b}")
else:
    print("No se puede dividir por cero.")

if a != 0:
    print(f"Es divisor: {b % a == 0}")
else:
    print("No se puede calcular divisibilidad con cero")

print(f"El {b}% de {a} es: {a * b / 100:.2f}")

