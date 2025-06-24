lista_tareas = []
proximo_id_tarea = 1# Inicializamos el próximo ID de tarea
    # Función para agregar una tarea a la lista de tareas
def agregar_tarea(descripcion, prioridad="media"):
    global proximo_id_tarea # Declaramos la variable global
    tarea = { # Creamos un diccionario con los datos de la tarea
        "id": proximo_id_tarea, # Asignamos el próximo ID de tarea
        "titulo": titulo, # Asignamos el título de la tarea
        "descripcion": descripcion, # Asignamos la descripción de la tarea
        "completada": False # Asignamos el estado de la tarea como no completada
    }
    lista_tareas.append(tarea) # Agregamos la tarea a la lista de tareas
    proximo_id_tarea += 1# Incrementamos el próximo ID de tarea
    print(f"Tarea '{titulo}' agregada con éxito.") # Mostramos un mensaje de éxito
def mostrar_tareas():
    print("\n---Lista de tareas: ---")
    if not lista_tareas:
        print("No hay tareas en la lista.")
        return

    for tarea in lista_tareas:
      estado = "Completada" if tarea["completada"] else "Pendiente"
      print(f"{estado} ID: {tarea['id']} | {tarea['Descripcion']} {tarea['prioridad']}{tarea['titulo']} - {estado}")
#pruebas
agregar_tarea ("Estudiar para el examen de Calculo")
agregar_tarea ("Hacer la compra de supermercado", "alta")
agregar_tarea ("Llamar al médico", "baja")
    # Mostrar tareas  
mostrar_tareas() # Mostramos la lista de tareas
    # Fin del programa