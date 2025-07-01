"""19. Leer un número entero y mostrar en pantalla su tabla de multiplicar."""

n = int(input("Ingrese un número entero: "))
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")