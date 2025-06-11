"""Ejercicio 2: Contar letras 'a'
Pide al usuario una palabra y cuenta cuántas veces aparece la letra 'a' (minúscula) en ella."""

palabra = input("Ingresa una palabra: ")

cantidad_de_as = 0

for letra in palabra:
    if letra == 'a':
        cantidad_de_as += 1

print(f"Cantidad de letras 'a': {cantidad_de_as}")