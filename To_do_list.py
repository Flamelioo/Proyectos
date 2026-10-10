amy_tareas = []

while True:
    print("Hola, use las opciones con los numeros del 1-4")
    print("Opcion 1: ver las tareas")
    print("Opcion 2: Agregar tareas")
    print("Opcion 3: Eliminar tareas")
    print("Opcior 4: Salir del sistema")

    opcion = int(input("Seleccione su opcion: "))
    if opcion == 1:
        print(amy_tareas)

    elif opcion == 2:
        tarea = str(input("Diga la tarea: ")).strip()
        if tarea == " ":
            print("Eso es un espacio")
        else:
            amy_tareas.insert(0, tarea)

    elif opcion == 3:
        print(amy_tareas)
        borrar = (input("Ingrese la tarea que desee eliminar: "))
        amy_tareas.remove(borrar)
    else:
        print("Gracias por usar el sistema. UwU")
        break