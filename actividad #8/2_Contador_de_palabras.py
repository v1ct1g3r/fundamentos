def contador(str):
    return len(str.split())


def main():
    print(f"Ese texto tiene {contador(input("Ingrese un texto: "))} palabras")


main()