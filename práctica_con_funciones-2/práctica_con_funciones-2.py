def saludo():
    return "¡Hola!"

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def area_rec(lado1, lado2):
    return lado1 * lado2

def par_o_impar(n):
    return "Par" if n % 2 == 0 else "Impar"

def celsius_a_fahrenheit(t):
    return 1.8 * t + 32

def max_3(n1, n2, n3):
    max_n1_n2 = n1 if n1 > n2 else n2
    return max_n1_n2 if max_n1_n2 > n3 else n3

def palindromo(string):
    string = str(string)
    return "Es palíndromo" if string == string[::-1] else "No es palíndromo"

def factorial(n):
    if n < 0:
        return float('inf')
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def contar_vocales(palabra):
    vocales = ('a','e','i','o','u')
    total = 0
    for letra in palabra:
        if letra in vocales:
            total += 1
    return total

def primo(n):
    if n < 2:
        return "No es primo"
    for i in range(2, int(n**(1/2))):
        if n % i == 0:
            return "No es primo"
    return "Es primo"