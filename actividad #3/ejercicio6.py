import random
import sys

print("""
6. Simulador de cajero automático simple
   
» Para consultar su saldo, digite 'CONSULTAR'.
» Para retirar, digite 'RETIRAR'.
» Para depositar, digite 'DEPOSITAR'.
» Para salir, digite 'SALIR'.
      """)

_saldo = float(random.randint(0, 1000000))

_opcion = input(">> ").lower()

while True:
    if _opcion == "consultar":
        print(f"Su saldo actual es de RD${_saldo}")
        _opcion = input(">> ").lower()

    elif _opcion == "retirar":
        _retiro = float(input("Ingrese la cantidad que desea retirar: "))
        if _saldo - _retiro < 0:
            print("No tiene el balance suficiente")
        else:
            _saldo -= _retiro
            print("Su retiro ha sido efectuado exitosamente")
        _opcion = input(">> ").lower()

    elif _opcion == "depositar":
        _deposito = float(input("Ingrese la cantidad que desea depositar: "))
        _saldo += _deposito
        print("Su depósito ha sido efectuado exitosamente")
        _opcion = input(">> ").lower()

    elif _opcion == "salir":
        break

    else:
        # Pregunta otra vez
        _opcion = input(">> ").lower()