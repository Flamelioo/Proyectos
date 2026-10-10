
print("Calculador de notas de presentacion")
print("A continuacion, proceda a poner sus notas y su nombre")

Nombre = input("Introduzca su nombre: ")
nota1 = int(input("Introduzca su calificacion de 4to: "))
nota2 = int(input("Introduzca su calificacion de 5to: "))
nota3 = int(input("Introduzca su calificacion de 6to: "))

Promedio = (nota1+nota2+nota3)/3

def indicar_si_aprobo(Promedio):
    if Promedio >= 70:
        return "Has aprobado"
    else:
        return "Has desaprobado"
    
estado = indicar_si_aprobo(Promedio)
print (f"Hola {Nombre}, tu promedio es {Promedio:.1f} y tu {estado}")

resultado = Promedio < 70
print(resultado)