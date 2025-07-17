"""3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído."""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
max_num = numeros[0]
for num in numeros:
    if es_primo(num):
        max_num = num
        break
else:
    max_num = "n/a"

if max_num != "n/a":
    for i in range(1, len(numeros)):
        if es_primo(numeros[i]) and numeros[i] > max_num:
            max_num = numeros[i]
    print(f"El mayor número primo está en la posición {numeros.index(max_num)} (del 0 al 9)")
else:
    print("No se ingresó ningún número primo")