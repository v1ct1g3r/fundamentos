import random


print("""
7. Juego: Piedra, papel o tijera
      
» Elige: ¿Piedra, papel o tijera?
      """)

opciones = ("piedra", "papel", "tijera")

usuario = input("Usuario >> ").lower()

computadora = opciones[random.randint(0,2)]
print(f"Computadora >> {computadora}")

if usuario == computadora:
    print("¡Empate!")

elif usuario == "piedra" and computadora == "tijera":
    print("¡Usuario gana!")

elif usuario == "tijera" and computadora == "piedra":
    print("¡Computadora gana!")

elif usuario == "papel" and computadora == "piedra":
    print("¡Usuario gana!")

elif usuario == "piedra" and computadora == "papel":
    print("¡Computadora gana!")

elif usuario == "tijera" and computadora == "papel":
    print("¡Usuario gana!")

elif usuario == "papel" and computadora == "tijera":
    print("¡Computadora gana!")