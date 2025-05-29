print("""
2. CONVERSOR DE UNIDADES
      """)

distancia = float(input("Ingrese una cantidad en kilómetros: "))

print("""
1. Digite 'millas' para convertir a millas.
2. Digite 'metros' para convertir a metros.
3. Digite 'centimetros' para convertir a centimetros.
      """)

convertir_a = input(">> ").lower()

if convertir_a == "millas":
    print(f"{distancia:.2f} kilométros equivalen a {distancia*0.621371:.2f} millas")
elif convertir_a == "metros":
    print(f"{distancia:.2f} kilométros equivalen a {distancia*1000:.2f} metros")
elif convertir_a == "centimetros":
    print(f"{distancia:.2f} kilométros equivalen a {distancia*100000:.2f} centímetros")