date: str = input("Ingrese una fecha con el formato dd/mm/aaaa: ")

day: str = date[0:2]
month: str = date[3:5]
year: str = date[6:10]
print(f"Fecha formateada: {year[2:4]}-{month}-{day}")