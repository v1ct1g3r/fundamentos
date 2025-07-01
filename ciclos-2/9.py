"""9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205."""

for i in range(25, 206):
    if i % 10 == 6:
        print(i, end=' ')