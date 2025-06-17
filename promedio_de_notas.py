print("""
      --CALCULADORA DE PROMEDIO DE NOTAS--
      """)

while True:
    nombre = input("Nombre del estudiante: ")
    matricula = input("Matrícula: ")
    notas = []

    for i in range(4):
        nota = input(f"Nota {i + 1}: ")
        while float(nota) < 0 or float(nota) > 100 or not nota.isdigit():
            print("La nota solo puede ser un número mayor o igual que 0 y menor o igual que 100")
            nota = input(f"Nota {i + 1}: ")
        notas.append(float(nota))

    promedio = sum(notas) / 4
    print(f"El promedio de las notas de {nombre} es {promedio}")
    
    salida = input("¿Desea calcular el promedio de otro estudiante? (S/N): ").upper()
    while salida != "S" and salida != "N":
        salida = input("¿Desea calcular el promedio de otro estudiante? (S/N): ").upper()
    if salida == "S":
        continue
    elif salida == "N":
        break
