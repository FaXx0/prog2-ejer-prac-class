def crear_sala(filas, columnas):
    """Crea una matriz de asientos inicialmente libres"""
    return [['L' for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    """Muestra la sala de cine de forma visual"""
    print("\n" + "="*50)
    print("SALA DE CINE".center(50))
    print("="*50)

    # Imprimir encabezado de columnas
    print("   ", end="")
    for j in range(len(sala[0])):
        print(f"{j+1:2}", end=" ")
    print("\n" + "-" * (4 + 3*len(sala[0])))

    # Imprimir filas con asientos
    for i, fila in enumerate(sala):
        print(f"{i+1:2} |", end=" ")
        for asiento in fila:
            if asiento == 'L':
                print("\033[92m" + asiento + "\033[0m", end="  ")  # Verde para libres
            else:
                print("\033[91m" + asiento + "\033[0m", end="  ")  # Rojo para ocupados
        print()

def ocupar_asiento(sala, fila, columna):
    """Intenta ocupar un asiento si está disponible"""
    # Convertir a índices internos (restar 1)
    fila_idx = fila - 1
    col_idx = columna - 1

    # Validar coordenadas
    if not (0 <= fila_idx < len(sala) or not (0 <= col_idx < len(sala[0])):
        print("\033[91mError: Asiento fuera de rango\033[0m")
        return False

    # Verificar disponibilidad
    if sala[fila_idx][col_idx] == 'L':
        sala[fila_idx][col_idx] = 'O'
        print(f"\033[92mAsiento {fila},{columna} ocupado con éxito!\033[0m")
        return True
    else:
        print("\033[91mError: Asiento ya ocupado\033[0m")
        return False

def contar_asientos_libres(sala):
    """Cuenta los asientos disponibles"""
    return sum(fila.count('L') for fila in sala)

# Programa principal
if __name__ == "__main__":
    # Crear sala de cine (5 filas x 8 columnas)
    sala_cine = crear_sala(5, 8)

    while True:
        # Mostrar estado actual de la sala
        mostrar_sala(sala_cine)

        # Mostrar menú
        print("\nOPCIONES:")
        print("1. Ocupar asiento")
        print("0. Salir")
        print(f"Asientos libres:
        \033[92m{contar_asientos_libres(sala_cine)}\033[0m")

        # Obtener selección del usuario
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("\033[91mError: Ingrese un número válido\033[0m")
            continue

        # Procesar opción
        if opcion == 0:
            print("¡Gracias por usar el sistema de reservas!")
            break
        elif opcion == 1:
            try:
                fila = int(input("Ingrese número de fila: "))
                columna = int(input("Ingrese número de columna: "))
                ocupar_asiento(sala_cine, fila, columna)
            except ValueError:
                print("\033[91mError: Ingrese números válidos\033[0m")
        else:
            print("\033[91mOpción no válida. Intente nuevamente.\033[0m")