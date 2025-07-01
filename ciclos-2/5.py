"""5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos."""

n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número entero: "))
for i in range(n, m + 1):
    if i % 10 == 4:
        print(i, end=' ')