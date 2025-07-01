"""3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído."""

n = int(input("Ingrese un número entero: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')