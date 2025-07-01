"""13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído."""

n = int(input("Ingrese un número entero: "))
for i in range(1, n + 1):
    if i % 5 == 0:
        print(i, end=' ')