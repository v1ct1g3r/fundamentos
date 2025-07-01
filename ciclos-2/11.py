"""11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro."""

while True:
    n = input("Ingrese un número entero de dos dígitos: ")
    if len(n) == 2:
        break

for i in range(int(n[0]), int(n[1]) + 1):
    print(i, end=' ')