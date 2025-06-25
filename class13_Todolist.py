"""lista_tareas = []
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
    # Fin del programa"""
#------------------------------------#
#------------------------------------#
lista_tareas = []
proximo_id_tarea = 1  # Inicializamos el próximo ID de tarea
# Función para agregar una tarea a la lista de tareas
def agregar_tarea(descripcion, prioridad="media"):
    global proximo_id_tarea  # Declaramos la variable global
    tarea = {  # Creamos un diccionario con los datos de la tarea
        "id": proximo_id_tarea,
        "titulo": descripcion,  # Usamos la descripción como título
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }
    lista_tareas.append(tarea)
    proximo_id_tarea += 1
    print(f"Tarea '{descripcion}' agregada con éxito.")
# Función para mostrar las tareas
def mostrar_tareas():
    print("\n--- Lista de tareas ---")
    if not lista_tareas:
        print("No hay tareas en la lista.")
        return
    for tarea in lista_tareas:
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"ID: {tarea['id']} | {tarea['titulo']} ({tarea['prioridad']}) - {estado}")
# Pruebas
agregar_tarea("Estudiar para el examen de Cálculo")
agregar_tarea("Hacer la compra de supermercado", "alta")
agregar_tarea("Llamar al médico", "baja")
# Mostrar tareas
mostrar_tareas()
def buscar_tarea_por_id(id_buscado):
    for tarea in lista_tareas:
        if tarea["id"] == id_buscado:
            return tarea
    return None
#Despues de agregar las tareas con ID 1 Y 2
tarea_encontrada = buscar_tarea_por_id(1)
if tarea_encontrada:
    print(f"\nBusqueda exitosa: {tarea_encontrada['descripcion']}")
else:
    print("\nBusqueda fallida: Tarea no encontrada.")
tarea_fantasma = buscar_tarea_por_id(99)
if not tarea_fantasma:
    print("Busqueda de tarea inexistente funciono correctamente. ")
def marcar_tarea_completada(id_tarea):
    # ¡Reutilizamos nuestra función de búsqueda!
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea: # Si la búsqueda devolvió un diccionario (no None)
        tarea["completada"] = True
        print(f"✅ Tarea '{tarea['descripcion']}' marcada como completada.")
    else:
        print(f"❌ Error: No se encontró la tarea con ID {id_tarea}.")
def eliminar_tarea(id_tarea):
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea:
        lista_tareas.remove(tarea)
        print(f"✅ Tarea '{tarea['descripcion']}' eliminada.")
    else:
        print(f"❌ Error: No se encontró la tarea con ID {id_tarea}.")
mostrar_tareas()
marcar_tarea_completada(1)
mostrar_tareas() # Debería mostrar la tarea 1 como completada
eliminar_tarea(2) 
mostrar_tareas() # La tarea 2 ya no debería aparecer
marcar_tarea_completada(99) # Probar con un ID que no existe
# ... (definiciones de funciones y pruebas aquí arriba) ...
 # ¡Puedes comentar o eliminar las pruebas para tener un programa limpio!
while True:
    print("\n===== MENÚ TO-DO LIST =====")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("0. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        desc = input("Descripción de la nueva tarea: ")
        prio = input("Prioridad (alta, media, baja): ")
        agregar_tarea(desc, prio)
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        id_t = int(input("ID de la tarea a completar: "))
        marcar_tarea_completada(id_t)
    elif opcion == '4':
        id_t = int(input("ID de la tarea a eliminar: "))
        eliminar_tarea(id_t)
    elif opcion == '0':
        print("¡Hasta pronto!")
        break # Rompe el bucle while
    else:
        print("❌ Opción no válida. Inténtalo de nuevo.")