import random

numero_secreto = random.randint(1, 10)

print("""
4. Adivina el número
      """)

_numero = int(input("Ingrese un número entero entre 1 y 10: "))
while True:
    if numero_secreto < _numero:
        print("El número secreto es menor.")
    elif numero_secreto > _numero:
        print("El número secreto es mayor.")
    else:
        print("¡Acertaste!")
        break
    _numero = int(input("Ingrese otro número entero entre 1 y 10: "))
