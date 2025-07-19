""" 8. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay."""

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
negativos = 0
for numero in numeros:
    if numero < 0:
        negativos += 1
print(f"Hay {negativos} números negativos.")