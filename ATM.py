balance_usuario = 500

while True:
    print("\nBienvenido al ATM")
    print("Pulse 1 para acceder al balance")
    print("Pulse 2 para hacer un retiro")
    print("Pulse 3 para hacer un deposito")
    print("Pulse 4 para salir del sistema")

    uso = int(input("Seleccione el uso: "))

    if uso == 1:
        print(f"su balance es {balance_usuario}")
    elif uso == 2:
        retiro = int(input("Seleccione el monto a retirar"))
        if retiro <= 0:
            print("El retiro debe ser mayor a 0")
        elif retiro > balance_usuario:
            print(f"El saldo de su cuenta es menos al retiro, su saldo es {balance_usuario}")
        else:
            balance_usuario = balance_usuario - retiro
    elif uso == 3:
        deposito = int(input("Ingrese la cantidad que desea depositar"))
        if deposito <= 0:
            print("El montod debe ser mayor a 0")
        else:
            balance_usuario = balance_usuario + deposito
    else:
        print("Gracias por usar el ATM")
        break