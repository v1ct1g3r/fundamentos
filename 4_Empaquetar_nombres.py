def formatear(nombres):
    return list(nombre.strip().title() for nombre in nombres.split(","))


def main():
    print(formatear(input("Ingrese nombres separados por comas: ")))


main()