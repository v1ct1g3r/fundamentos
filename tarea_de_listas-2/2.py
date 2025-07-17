"""2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído."""

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
max_par = numeros[0]
for i in range(1, len(numeros)):
    if numeros[i] > max_par and numeros[i] % 2 == 0:
        max_par = numeros[i]
print(f"El mayor número par está en la posición {numeros.index(max_par)} (del 0 al 9)")