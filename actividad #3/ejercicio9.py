print("""
9. Contador de vocales
      """)

contador = 0

frase = input("Ingrese una frase: ").lower()

for letra in frase:
    if letra in "aeiouáéíóúü":
        contador += 1

print(f"Esa frase tiene {contador} vocales.")