"""7. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista."""

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
print(f"El promedio entero de los datos de la lista es {sum(numeros) // len(numeros)}.")