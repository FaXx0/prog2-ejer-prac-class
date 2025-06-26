 """   # Autor: Fabrizzio Lora (FaXx0)
    # Descripción: Este programa simula una sala de cine donde se pueden reservar asientos.
    # El usuario puede ver la sala, reservar asientos y ver cuántos asientos están disponibles.
def crear_sala(filas, columnas): # Función para crear una matriz de asientos inicialmente libres
# === Crea una matriz de asientos inicialmente libres === #
    return [['L' for _ in range(columnas)] for _ in range(filas)] # Retorna una matriz de asientos inicialmente libres
def mostrar_sala(sala): # Función para mostrar la sala de cine de forma visual
    # === Muestra la sala de cine de forma visual === # 
    print("\n" + "="*50)                             # Imprime una línea de separación    
    print("SALA DE CINE".center(50))                 # Imprime el título del programa
    print("="*50)                                    # Imprime una línea de separación
    # Encabezado numérico para columnas #
    print("   ", end="") # Espacio para alinear con filas
    for j in range(len(sala[0])): # Bucle para imprimir el encabezado numérico para columnas
        print(f"{j+1:>3}", end=" ") # Imprime el encabezado numérico para columnas
    print("\n" + "-" * (4 + 4*len(sala[0]))) # Imprime una línea de separación
    # Filas con asientos #
    for i, fila in enumerate(sala): # Bucle para imprimir las filas con asientos
        print(f"{i+1:2} |", end=" ") # Imprime el número de fila
        for asiento in fila: # Bucle para imprimir los asientos de la fila
            color = "\033[92m" if asiento == 'L' else "\033[91m"  # Verde libre / Rojo ocupado
            print(f"{color}{asiento}\033[0m", end="   ") # Imprime el asiento con color
        print() # Salto de línea
    print("Leyenda: \033[92mL = Libre\033[0m, \033[91mO = Ocupado\033[0m") # Imprime la leyenda de colores
def ocupar_asiento(sala, fila, columna): # Función para ocupar un asiento si está disponible
    # === Intenta ocupar un asiento si está disponible === #
    # Validar rango de filas y columnas
    if not (1 <= fila <= len(sala)) or not (1 <= columna <= len(sala[0])): # Validación de rango de filas y columnas
        print("\033[91mError: Asiento fuera de rango\033[0m") # Mensaje de error
        return False # Retorna False si el asiento está fuera de rango
    fila_idx = fila - 1 # Índice de fila
    col_idx = columna - 1 # Índice de columna
    if sala[fila_idx][col_idx] == 'L':  # Si el asiento está libre
        sala[fila_idx][col_idx] = 'O'   # Ocupa el asiento
        print(f"\033[92mAsiento {fila},{columna} ocupado con éxito!\033[0m") # Mensaje de éxito
        return True # Retorna True si el asiento se ocupó con éxito
    else: # Si el asiento está ocupado
        print("\033[91mError: Asiento ya ocupado\033[0m")     # Mensaje de error
        return False # Retorna False si el asiento está ocupado
def contar_asientos_libres(sala): # Función para contar los asientos libres
    # === Cuenta los asientos disponibles === #
    return sum(fila.count('L') for fila in sala) # Retorna el número de asientos libres
# Programa principal #
if __name__ == "__main__": # Si el archivo se ejecuta directamente, ejecuta el programa principal
    # Crear sala de cine (5 filas x 8 columnas)
    sala_cine = crear_sala(5, 8) # Crea una matriz de asientos inicialmente libres    
    while True: # Bucle principal del programa
        mostrar_sala(sala_cine) # Muestra la sala de cine de forma visual
        libres = contar_asientos_libres(sala_cine)     # Cuenta los asientos libres
        # Mostrar menú
        print("\n" + "="*50) # Imprime una línea de separación
        print("MENÚ PRINCIPAL".center(50)) # Imprime el título del menú principal
        print("="*50)     # Imprime una línea de separación
        print(f"Asientos disponibles: \033[92m{libres}\033[0m") # Imprime el número de asientos libres
        print("\nOpciones:") # Imprime las opciones del menú principal
        print("1. Ocupar asiento") # Opción 1: Ocupar asiento
        print("0. Salir") # Opción 0: Salir del programa
        try: # Intenta convertir la entrada del usuario a un número entero
            opcion = int(input("\nSeleccione una opción: ")) # Solicita al usuario que ingrese una opción
        except ValueError: # Si la entrada no es un número válido, muestra un mensaje de error
            print("\033[91mError: Debe ingresar un número\033[0m") # Mensaje de error
            continue # Continúa el bucle principal del programa
        if opcion == 0: # Si la opción es 0, sale del programa
            print("\n¡Gracias por usar el sistema de reservas!") # Mensaje de despedida
            break # Sale del bucle principal del programa
        elif opcion == 1: # Si la opción es 1, ocupa un asiento
            try: # Intenta convertir la entrada del usuario a números enteros
                fila = int(input("Fila (1-5): ")) # Solicita al usuario que ingrese el número de fila
                columna = int(input("Columna (1-8): "))     # Solicita al usuario que ingrese el número de columna
                ocupar_asiento(sala_cine, fila, columna) # Ocupa el asiento si está disponible
            except ValueError: # Si la entrada no es un número válido, muestra un mensaje de error
                print("\033[91mError: Ingrese valores numéricos\033[0m") # Mensaje de error
        else: # Si la opción no es válida, muestra un mensaje de error
            print("\033[91mOpción no válida. Intente nuevamente.\033[0m") # Mensaje de error

        input("\nPresione Enter para continuar...") # Pausa el programa hasta que el usuario presione Enter
        print("Fabrizzio Lora (FaXx0)")
        # Fin del programa"""
#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#
# --- Funciones del sistema ---
def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    print("\n    " + "  ".join([f"C{j}" for j in range(len(sala[0]))]))
    print("   " + "---" * len(sala[0]))
    for i, fila in enumerate(sala):
        print(f"F{i} | " + "  ".join(fila))
    print()

def ocupar_asiento(sala, fila, columna):
    filas = len(sala)
    columnas = len(sala[0])
    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        print("⚠ Coordenadas fuera de rango.")
        return False
    if sala[fila][columna] == 'O':
        print("❌ Ese asiento ya está ocupado.")
        return False

    # Simulación de pago
    confirmacion = input(f"💳 El asiento F{fila} C{columna} cuesta 30 Bs. ¿Deseas pagar y reservarlo? (S/N): ").strip().upper()
    if confirmacion != 'S':
        print("ℹ Reserva cancelada.")
        return False

    sala[fila][columna] = 'O'
    print(f"✅ Asiento F{fila} C{columna} ocupado correctamente.")
    return True

# --- Programa Principal ---

sala = crear_sala(5, 8)  # Sala de 5 filas x 8 columnas

while True:
    mostrar_sala(sala)
    print("🎟  MENÚ DE OPCIONES")
    print("1. Ocupar un asiento")
    print("0. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        try:
            fila = int(input("Ingresa la fila del asiento (ej. 0 a 4): "))
            columna = int(input("Ingresa la columna del asiento (ej. 0 a 7): "))
            ocupar_asiento(sala, fila, columna)
        except ValueError:
            print("❗Por favor, ingresa números válidos.")
    elif opcion == '0':
        print("🎬 ¡Gracias por usar el sistema de cine! Hasta luego.")
        break
    else:
        print("❗Opción inválida. Intenta de nuevo.")
