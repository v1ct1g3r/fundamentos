"""10. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista."""

numeros = list(map(int, input("Ingrese 10 números enteros separados por espacios: ").split()))
dividendo = int(input("Ingrese un número entero: "))
total = 0
for divisor in numeros:
    if dividendo % divisor == 0:
        total += 1
print(f"Hay {total} de los 10 números ingresados que dividen al {dividendo}.")