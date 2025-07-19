""" 6. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos."""

numeros = input("Ingrese 10 enteros separados por espacios: ").split()
posiciones = []
for i in range(len(numeros)):
    if len(numeros[i]) > 3:
        posiciones.append(i)
print(f"Los números con más de 3 dígitos se encuentran en las posiciones {", ".join(str(pos) for pos in posiciones)} (del 0 al 9).")