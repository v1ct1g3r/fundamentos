"""Ejercicio 2: Condicional if — Número positivo, negativo o cero"""

N = float(input("Ingresa un número: "))

if N < 0:
    print("El numero es negativo")
elif N > 0:
    print("El numero es positivo")
else:
    print("El numero es cero")