print("""
5. Clasificador de palabras
      """)

_palabra = input("Ingrese una palabra: ").title()

if len(_palabra) < 5:
    print(f"'{_palabra}' es una palabra corta.")
elif len(_palabra) == 5:
    print(f"'{_palabra}' es una palabra media.")
else:
    print(f"'{_palabra}' es una palabra larga.")
