print("""
1. CALCULADORA DE PROMEDIO CON RETROALIMENTACIÓN
      """)

nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))

promedio = (nota_1 + nota_2 + nota_3) / 3
print(f"Promedio: {promedio:.2f}")

ha_aprobado = True

if promedio >= 90:
    print("Excelente")
elif promedio >= 80:
    print("Bueno")
elif promedio >= 70:
    print("Regular")
else:
    print("Deficiente")
    _aprobacion = False

if ha_aprobado:
    print("Aprobó")
else:
    print("Reprobó")
