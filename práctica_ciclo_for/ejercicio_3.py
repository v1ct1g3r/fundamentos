"""Ejercicio 3: Letras al revés
Solicita una palabra al usuario e imprime cada letra en orden inverso, una por línea."""

palabra = input("Palabra: ")

for letra in palabra[::-1]:
    print(letra)