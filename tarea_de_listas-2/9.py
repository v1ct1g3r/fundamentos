"""9. Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista."""

def factorial(n):
    if n < 0:
        return float("inf")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numeros = list(map(int, input("Ingrese 10 enteros separados por espacios: ").split()))
factoriales = [factorial(n) for n in numeros]
print(f"Los factoriales de cada número son {", ".join(str(num) for num in factoriales)}.")