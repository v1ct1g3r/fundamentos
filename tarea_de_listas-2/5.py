"""5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares."""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

numeros = input("Ingrese 10 enteros separados por espacios: ").split()
digitos_pares_por_numero = []
for num in numeros:
    if es_primo(int(num)):
        digitos_pares = 0
        for digito in num:
            if int(digito) % 2 == 0:
                digitos_pares += 1
        digitos_pares_por_numero.append(digitos_pares)
    else:
        digitos_pares_por_numero.append(-1)

if all(x == -1 for x in digitos_pares_por_numero):
    print("No se ingresó ningún número primo")
else:
    print(f"El número primo con mayor cantidad de dígitos pares está en la posición {digitos_pares_por_numero.index(max(digitos_pares_por_numero))} (del 0 al 9)")