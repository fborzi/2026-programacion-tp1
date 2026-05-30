"""
Escribí el código que solicite el ingreso de dos números enteros y que luego:
a.Muestre en pantalla la suma de ambos números de la siguiente manera:"La suma de a y b es c" siendo a y b los números ingresados y c el resultado de la suma. Por ejemplo si se ingresaron 42 y 519 debería mostrarse 'La suma de 42 y 519 es 561'.
b.Muestre la división de ambos, usando un formato similar al del punto a.
c. Muestre True si el primero es divisor del segundo(si puede realizarse una división entera), False si no lo es.
d.Muestre el b% de a (suponiendo que a y b son los números ingresados). Por ejemplo, si se ingresaron 150 y 10, debería mostrarse 'El 10% de 150 es 15'. ¿Cómo harías para que el resultado se muestre con decimales?
e.Si a es una variable que contiene uno de los números ingresados, ¿qué le falta a la siguiente instrucción para que muestre el texto sin errores?
<<<print("El precio es $"+a)
"""



a = int(input("Escriba el numero 1:"))
b = int(input("Escriba el numero 2:"))

suma = a + b
division = a / b
porcentaje = a * b / 100

print("La suma de",a,"y", b, "es", suma)
print("La division de",a, "por",b,"es",division)

if a % b == 0:
    print("Es divisor: True")
else:
    print("Es divisor: False")

print("El", b,"% de",a,"sin decimales es:",int(porcentaje))
print("El", b,"% de",a,"con decimales es:",porcentaje)
print("El precio es $",a)