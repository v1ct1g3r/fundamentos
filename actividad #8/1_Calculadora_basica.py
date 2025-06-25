def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return a / b


def potenciacion(a, b):
    return a**b


def main():
    print("""Calculadora básica
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Potenciación""")
    
    opcion = input("> ")

    if opcion == "1" or opcion.lower() == "suma":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if a - int(a) == 0 and b - int(b) == 0:
            print(int(suma(a, b)))
        else:
            print(suma(a, b))
    
    if opcion == "2" or opcion.lower() == "resta":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if a - int(a) == 0 and b - int(b) == 0:
            print(int(resta(a, b)))
        else:
            print(resta(a, b))

    if opcion == "3" or opcion.lower() == "multiplicacion" or opcion.lower() == "multiplicación":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if a - int(a) == 0 and b - int(b) == 0:
            print(int(multiplicacion(a, b)))
        else:
            print(multiplicacion(a, b))

    if opcion == "4" or opcion.lower() == "division" or opcion.lower() == "división":
        a = float(input("Ingrese el dividendo: "))
        b = float(input("Ingrese el divisor: "))

        if a - int(a) == 0 and b - int(b) == 0:
            print(int(division(a, b)))
        else:
            print(division(a, b))
    

    if opcion == "5" or opcion.lower() == "potenciacion" or opcion.lower() == "potenciación":
        a = float(input("Ingrese la base: "))
        b = float(input("Ingrese el exponente: "))

        if a - int(a) == 0 and b - int(b) == 0:
            print(int(potenciacion(a, b)))
        else:
            print(potenciacion(a, b))


main()