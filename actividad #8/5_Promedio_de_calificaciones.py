def promedio(calificaciones):
    calificaciones = list(map(float, calificaciones.split()))
    return sum(calificaciones) / len(calificaciones)


def main():
    calificaciones = input("Ingrese las calificaciones separadas por espacios: ")
    print(f"{promedio(calificaciones):.2f}")


main()