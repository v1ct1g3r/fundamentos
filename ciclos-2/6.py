"""6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos."""

while True:
    n = input("Ingrese un número entero de tres dígitos: ")
    if len(n) == 3:
        break

for digito in n:
    for i in range(1, int(digito) + 1):
        print(i, end=' ')
    print()