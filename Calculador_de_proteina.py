import time

def calcular_proteina(peso, objetivo):
    if objetivo == "VOLUMEN":
        return peso * 2.0
    elif objetivo == "DEFINICION":
        return peso * 2.2
    else:
        return peso * 1.4

print("Hola, este es el calculador que te ayuda a saber cuanta proteina necesitas.")
print("A continuacion, ingrese los siguientes datos: ")

nombre = input("INTRODUZCA SU NOMBRE: ")
peso = float(input("INTRODUZCA SU PESO EN KG: "))
objetivo = input("INTRODUZCA SU OBJETIVO (DEFINICION/VOLUMEN/MANTENIMIENTO): ").upper()

time.sleep(1.5)

proteina = calcular_proteina(peso, objetivo)

print(f"Gracias por preferirnos {nombre}, los gramos de proteina que deberias ingerir diariamente son: {proteina:.0f} gramos")