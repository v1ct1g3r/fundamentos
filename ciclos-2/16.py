"""16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos."""

x = int(input("x: "))
y = int(input("y: "))

promedio = 0
for i in range(1, x + 1):
    promedio += 2*i
promedio /= x

es_mayor = True
for j in range(1, y + 1):
    if promedio < 5*j:
        es_mayor = False
        break

print("Es mayor") if es_mayor else print("No es mayor")