"""4. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo."""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

numeros = input("Ingrese 10 enteros separados por espacios: ").split()
total = 0
for num in numeros:
    if es_primo(int(num[0])):
        total += 1
print(f"Hay {total} números que comienzan en dígito primo")