"""Ejercicio 5: Condicional + while — Adivina el número
"""

import random


N = random.randint(1, 10)

intentos = 1

print("Adivina el número (1 al 10):")
while True:
    entrada = int(input("Entrada: "))
    
    if entrada < N:
        print("Muy bajo.")
        intentos += 1
    elif entrada > N:
        print("Muy alto.")
        intentos += 1
    else:
        print("¡Correcto! Lo lograste en 3 intentos.")
        break