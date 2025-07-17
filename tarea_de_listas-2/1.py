"""1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído."""

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
print(f"El mayor número está en la posición {numeros.index(max(numeros))} (del 0 al 9).")