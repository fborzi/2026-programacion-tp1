"""
Vamos a trabajar con el ejercicio de Python 1102, donde se solicitara que 
se ingrese una primer cadena, luego una segunda cadena. Luego pedimos que 
se verifique cuantas veces se encuentra lo que se ingresa en la segunda cadena 
dentro de la primera. Despues pedimos que ambas cadenas se junten. Y por ultimo buscamos 
cuantas veces aparece la letra H en la segunda cadena.
"""
texto1 = input("Ingrese texto: ")
texto2 = input("Ingrese texto: ")
letra = texto1[0].lower()
cantidad = texto2.lower().count(letra)

print("Cantidad de veces que aparece:", cantidad)
print("Concatenacion:", texto1.lower() + texto2.lower())
print("La letra", letra, "aparece",
    texto2.count(letra), "veces en la cadena", texto2)
