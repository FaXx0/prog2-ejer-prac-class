import random

def crear_tablero():
    return [["~" for _ in range(4)] for _ in range(4)]

def mostrar_tablero(tablero):
    print()
    for fila in tablero:
        print(" ".join(fila))

def pedir_coordenadas(nombre):
    while True:
        try:
            fila = int(input(f"{nombre}, ingresa fila (1-4): ")) - 1
            col = int(input(f"{nombre}, ingresa columna (1-4): ")) - 1
            if 0 <= fila <= 3 and 0 <= col <= 3:
                return fila, col
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Usa solo números del 1 al 4.")

def jugar_vs_computadora():
    print("\n=== Modo: Jugador vs Computadora ===")
    jugador = input("Nombre del jugador: ")
    tablero = crear_tablero()

    print(f"{jugador}, coloca tu barco:")
    barco_jugador = pedir_coordenadas(jugador)
    barco_pc = (random.randint(0, 3), random.randint(0, 3))

    while True:
        mostrar_tablero(tablero)
        print(f"\n{jugador}, intenta adivinar el barco de la computadora:")
        fila, col = pedir_coordenadas(jugador)

        if tablero[fila][col] != "~":
            print("Ya atacaste ahí. Intenta otra vez.")
            continue

        if (fila, col) == barco_pc:
            tablero[fila][col] = "X"
            mostrar_tablero(tablero)
            print(f"\n¡{jugador} ganó! Hundiste el barco de la computadora.")
            break
        else:
            tablero[fila][col] = "O"
            print("Fallaste. Turno de la computadora.")

        # Turno de la computadora
        fila_pc = random.randint(0, 3)
        col_pc = random.randint(0, 3)
        print(f"La computadora atacó la posición ({fila_pc+1}, {col_pc+1})")

        if (fila_pc, col_pc) == barco_jugador:
            print("La computadora acertó. Perdiste.")
            break
        else:
            print("La computadora falló.")

def jugar_2_jugadores():
    print("\n=== Modo: Jugador vs Jugador ===")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")

    tablero1 = crear_tablero()
    tablero2 = crear_tablero()

    print(f"\n{jugador1}, coloca tu barco:")
    barco1 = pedir_coordenadas(jugador1)

    print(f"\n{jugador2}, coloca tu barco:")
    barco2 = pedir_coordenadas(jugador2)

    turno = 1
    while True:
        if turno % 2 == 1:
            print(f"\nTurno de {jugador1}")
            mostrar_tablero(tablero2)
            f, c = pedir_coordenadas(jugador1)
            if tablero2[f][c] != "~":
                print("Ya atacaste ahí. Intenta otra vez.")
                continue
            if (f, c) == barco2:
                tablero2[f][c] = "X"
                mostrar_tablero(tablero2)
                print(f"\n¡{jugador1} ganó! Hundiste el barco de {jugador2}.")
                break
            else:
                tablero2[f][c] = "O"
                print("Fallaste.")
        else:
            print(f"\nTurno de {jugador2}")
            mostrar_tablero(tablero1)
            f, c = pedir_coordenadas(jugador2)
            if tablero1[f][c] != "~":
                print("Ya atacaste ahí. Intenta otra vez.")
                continue
            if (f, c) == barco1:
                tablero1[f][c] = "X"
                mostrar_tablero(tablero1)
                print(f"\n¡{jugador2} ganó! Hundiste el barco de {jugador1}.")
                break
            else:
                tablero1[f][c] = "O"
                print("Fallaste.")
        turno += 1

def menu():
    while True:
        print("\n=== Menú de Batalla Naval ===")
        print("1. Jugar contra la computadora")
        print("2. Jugar 2 jugadores")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar_vs_computadora()
        elif opcion == "2":
            jugar_2_jugadores()
        elif opcion == "3":
            print("Saliendo del juego.")
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")

# Iniciar el programa
menu()
