"""4. Leer dos números y mostrar todos los enteros comprendidos entre ellos."""

n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número entero: "))
for i in range(n, m + 1):
    print(i, end=' ')