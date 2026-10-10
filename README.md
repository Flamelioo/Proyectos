# Ejercicios de Python

Proyectos pequeños que hice mientras aprendo Python. Todos funcionan en la terminal y no necesitan instalar librerías extra.

## Proyectos

| Archivo | Descripción | Conceptos que practico |
|---|---|---|
| `ATM.py` | Cajero automático con menú: consultar balance, retirar y depositar. | `while`, `if/elif/else`, validaciones |
| `To do list.py` | Lista de tareas: ver, agregar y eliminar tareas. | listas, `.strip()`, `.remove()` |
| `Adivina el numero.py` | Juego donde se adivina un número entre 1 y 100 con pistas. | `random`, `while`, contador de intentos |
| `Calculador de proteina.py` | Calcula la proteína diaria según el peso y el objetivo (definición, volumen o mantenimiento). | funciones, `input`, f-strings |
| `notas de presentacion.py` | Calcula el promedio de tres notas e indica si aprobó. | funciones, operadores, f-strings |

## Cómo ejecutarlos

1. Tener [Python 3](https://www.python.org/downloads/) instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el archivo que quieras. Como los nombres tienen espacios, van entre comillas:

```bash
python "ATM.py"
python "Adivina el numero.py"
```

## Mejoras pendientes

- Manejar errores cuando el usuario escribe letras en vez de números (`try` / `except`).
- ATM y To-Do: agregar una opción de salida propia y un mensaje de "opción no válida".
- To-Do: avisar si la tarea que se quiere eliminar no existe y mostrar las tareas numeradas.
- Adivina el número: mostrar el total de intentos al ganar y poner un límite de intentos.
- Guardar los datos en archivos para que no se pierdan al cerrar el programa.

## Autor

Eddw Vasquez, estudiante de Desarrollo de Software.
