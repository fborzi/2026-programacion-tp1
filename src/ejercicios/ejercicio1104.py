"""
Leer desde teclado una cadena de caracteres conteniendo una expresión
del tipo 'dd/mm/aaaa' e informar:
a. El día es: dd
b. El mes es: mm
c. El año es: aaaa
Luego informar la fecha leída con el formato:'aa-mm-dd'
(donde aa son los ultimos dos digitos de aaaa)
Restricción: No es posible utilizar el metodo split().
"""

fecha_entrada = input("Ingresa la fecha (formato dd/mm/aaaa):")
dia = fecha_entrada[0:2]
mes = fecha_entrada[3:5]
anio = fecha_entrada[6:10]

print(f"Formato: {anio}-{mes}-{dia}")
print(f"El día es: {dia}")
print(f"El mes es: {mes}")
print(f"El año es: {anio}")
