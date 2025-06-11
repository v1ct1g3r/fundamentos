"""Ejercicio 1: Suma de números pares
Escribe un programa que sume todos los números pares del 1 al 50 e imprima el resultado."""

suma = 0

for num in range(2, 50 + 1):  # Empieza desde el 2 para omitir el 0 y el 1. 50 + 1 para incluir el 50.
    if num % 2 == 0:
        suma += num

print(suma)