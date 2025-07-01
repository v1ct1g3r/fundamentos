"""12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1."""

while True:
    n = input("Ingrese un número entero de tres dígitos: ")
    if len(n) == 3:
        break

tiene_el_1 = False

for digito in n:
    if digito == '1':
        tiene_el_1 = True
        break

print("Tiene el dígito 1") if tiene_el_1 else print("No tiene el dígito 1")