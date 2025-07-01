"""2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído."""

n = int(input("Ingrese un número entero: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=' ')