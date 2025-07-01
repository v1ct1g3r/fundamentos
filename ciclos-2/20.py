"""20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído."""

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

n = int(input("Ingrese un número entero: "))
sumatoria = 0
for i in range(1, n + 1):
    sumatoria += factorial(i)
print(sumatoria)