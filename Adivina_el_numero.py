import random

numero = random.randint(1, 100)
intentos = 0
print("Adivina el numero")
while True:
    guess = int(input("Dime un numero: "))

    if numero > guess:
        print("Tu intento es mas bajo que el numero")
        intentos += 1
    elif numero < guess:
        print("Tu intento es mas mas alto que el numero")
        intentos += 1
    else:
        print("Ganaste el numero era", numero)
        break