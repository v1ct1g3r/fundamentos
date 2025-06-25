def es_palindromo(palabra):
    palabra = palabra.lower().replace(' ', '')
    return palabra == palabra[::-1]


def main():
    palabra = input("Ingrese una texto: ")

    if es_palindromo(palabra):
        print("Es palindromo")
    else:
        print("No es palindromo")


main()