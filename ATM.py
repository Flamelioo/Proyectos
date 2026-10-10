balance_usuario = 500

while True:
    print("==========Bienvenido al ATM==========")
    print("1. Balance de cuenta")
    print("2. Retiro")
    print("3. Deposito")
    print("4. Salir")
    print("=====================================")

    try:
        uso = int(input("Seleccione el uso: "))

        if uso == 1:
            print(f"Su balance es {balance_usuario}")
        elif uso == 2:
            retiro = int(input("Seleccione el monto a retirar: "))
            if retiro <= 0:
                print("El retiro debe ser mayor a 0")
            elif retiro > balance_usuario:
                print(f"El saldo de su cuenta es menor al retiro, su saldo es {balance_usuario}")
            else:
                balance_usuario = balance_usuario - retiro
                print(f"Su retiro fue exitoso, su nuevo balance es {balance_usuario}")
        elif uso == 3:
            deposito = int(input("Ingrese la cantidad que desea depositar: "))
            if deposito <= 0:
                print("El monto debe ser mayor a 0")
            else:
                balance_usuario = balance_usuario + deposito
                print(f"Su deposito fue exitoso, su nuevo balance es {balance_usuario}")
        elif uso == 4:
            print("Gracias por usar el ATM")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Introdujo un valor incorrecto, intentelo nuevamente")


   