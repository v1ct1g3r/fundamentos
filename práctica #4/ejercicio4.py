"""Ejercicio 4: Validación con while — Contraseña correcta"""

contraseña = "python123"

while True:
    entrada = input("Ingresa la contraseña: ")
    
    if entrada != contraseña:
        print("Contraseña incorrecta")
    else:
        print("Contraseña correcta")
        break