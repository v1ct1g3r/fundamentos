cantidad_de_notas = 1
suma_de_notas = 0

while True:
    suma_de_notas += int(input("Ingrese una nota: "))
    salir = input("¿Desea salir? S/N: ")
    
    if salir.upper() == 'S':
        print(f"El promedio de notas es {suma_de_notas // cantidad_de_notas}")
        break
    elif salir.upper() == 'N':
        cantidad_de_notas += 1