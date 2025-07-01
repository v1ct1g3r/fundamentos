"""17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5."""

multiplos_de_5 = []
n = int(input("Ingrese un número: "))
while n != 0:
    if n % 10 == 5:
        multiplos_de_5.append(n)
    n = int(input("Ingrese otro número: "))

print(sum(multiplos_de_5) // len(multiplos_de_5))