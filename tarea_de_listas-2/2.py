""" 2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número par leído."""

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
for num in numeros:
    if num % 2 == 0:
        max_par = num
        break
else:
    max_par = "n/a"

if max_par == "n/a":
    print("No se ingresó ningún número par.")
else:
    for num in numeros:
        if num > max_par and num % 2 == 0:
            max_par = num
    print(f"El mayor número par está en la posición {numeros.index(max_par)} (del 0 al 9).")