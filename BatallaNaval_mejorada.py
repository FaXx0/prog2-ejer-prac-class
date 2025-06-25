import random # Importa el módulo random para generar números aleatorios
import json # Importa el módulo json para guardar y cargar partidas
import os # Importa el módulo os para manejar archivos y directorios
# Configuración del juego #
FILAS = 4 # Número de filas en el tablero
COLUMNAS = 4 # Número de columnas en el tablero
NUM_BARCOS = 3 # Número de barcos por jugador
ARCHIVO_PARTIDA = "batalla_naval_save.json" # Nombre del archivo para guardar la partida
def crear_tablero(): # Función para crear un tablero vacío
    # === Crea un tablero vacío === # 
    return [["🌊" for _ in range(COLUMNAS)] for _ in range(FILAS)] # Retorna un tablero vacío
def mostrar_tablero(tablero, ocultar_barcos=False): # Función para mostrar el tablero en pantalla
    # === Muestra el tablero con formato === #
    print("\n  " + " ".join(str(i+1) for i in range(COLUMNAS))) # Imprime los números de las columnas
    for i, fila in enumerate(tablero):     # Imprime las filas del tablero
        print(chr(65+i) + " ", end="")    # Imprime la letra de la fila
        for celda in fila:                # Imprime las celdas de la fila
            if ocultar_barcos and celda == "⛵":
                print("🌊 ", end="")
            else:
                print(celda + " ", end="")
        print()
def colocar_barcos(tablero, modo, jugador=""):
    # === Coloca barcos en el tablero según el modo seleccionado === #
    if modo == "auto":
        for _ in range(NUM_BARCOS):
            while True:
                fila = random.randint(0, FILAS-1)
                col = random.randint(0, COLUMNAS-1)
                if tablero[fila][col] == "🌊":
                    tablero[fila][col] = "⛵"
                    break
        return tablero
    print(f"\n{jugador}, coloca tus {NUM_BARCOS} barcos:")
    for i in range(1, NUM_BARCOS+1):
        while True:
            try:
                print(f"Barco {i}:")
                coord = input("Ingresa coordenada (ej. A1): ").upper()
                fila = ord(coord[0]) - 65
                col = int(coord[1:]) - 1

                if not (0 <= fila < FILAS and 0 <= col < COLUMNAS):
                    print("Coordenada fuera de rango. Usa letras A-D y números 1-4")
                    continue
                if tablero[fila][col] == "🌊":
                    tablero[fila][col] = "⛵"
                    mostrar_tablero(tablero)
                    break
                else:
                    print("¡Ya hay un barco en esa posición!")
            except:
                print("Formato inválido. Usa formato como A1, B3, etc.")
    return tablero
def realizar_disparo(tablero, jugador):
    # === Realiza un disparo en el tablero === #
    while True:
        try:
            coord = input(f"{jugador}, ingresa disparo (ej. A1): ").upper()
            if coord == "GUARDAR":
                return "guardar"

            fila = ord(coord[0]) - 65
            col = int(coord[1:]) - 1

            if not (0 <= fila < FILAS and 0 <= col < COLUMNAS):
                print("Coordenada fuera de rango. Usa letras A-D y números 1-4")
                continue

            if tablero[fila][col] in ["💥", "💦"]:
                print("Ya disparaste aquí antes")
                continue

            if tablero[fila][col] == "⛵":
                tablero[fila][col] = "💥"
                print("¡Impacto! 🎯")
                return "impacto"
            else:
                tablero[fila][col] = "💦"
                print("Agua 💦")
                return "agua"
        except:
            print("Formato inválido. Usa formato como A1, B3, etc. o escribe GUARDAR para salir")
def quedan_barcos(tablero):
    # === Verifica si quedan barcos en el tablero === #
    for fila in tablero:
        if "⛵" in fila:
            return True
    return False
def guardar_partida(partida):
    # === Guarda la partida en un archivo === #
    with open(ARCHIVO_PARTIDA, 'w') as f:
        json.dump(partida, f)
    print("Partida guardada correctamente")
def cargar_partida():
    # === Carga una partida desde un archivo === #
    if not os.path.exists(ARCHIVO_PARTIDA):
        return None
    try:
        with open(ARCHIVO_PARTIDA, 'r') as f:
            return json.load(f)
    except:
        return None
def jugar_vs_cpu():
    # === Modo de juego contra la computadora === #
    nombre = input("Ingresa tu nombre: ")
    # Crear tableros
    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    # Colocar barcos
    print("\n[COLOCACIÓN DE BARCOS]")
    modo = input("¿Colocar barcos manualmente (M) o automáticamente (A)? ").upper()
    tablero_jugador = colocar_barcos(tablero_jugador, "manual" if modo == "M" else "auto", nombre)
    # Colocar barcos CPU
    tablero_cpu = colocar_barcos(tablero_cpu, "auto")
    # Historial de disparos de CPU
    disparos_cpu = []
    # Bucle principal del juego
    while True:
        # Turno del jugador
        print("\n[TU TABLERO]")
        mostrar_tablero(tablero_jugador)
        print("\n[TABLERO ENEMIGO]")
        mostrar_tablero(tablero_cpu, ocultar_barcos=True)
        resultado = realizar_disparo(tablero_cpu, nombre)
        if resultado == "guardar":
            guardar_partida({
                "modo": "cpu",
                "jugador": nombre,
                "tablero_jugador": tablero_jugador,
                "tablero_cpu": tablero_cpu,
                "disparos_cpu": disparos_cpu
            })
            return
        # Verificar victoria jugador
        if not quedan_barcos(tablero_cpu):
            print(f"\n¡{nombre} GANA! 🏆")
            return
        # Turno de la CPU
        print("\nTurno de la CPU...")
        while True:
            fila = random.randint(0, FILAS-1)
            col = random.randint(0, COLUMNAS-1)
            if (fila, col) not in disparos_cpu:
                disparos_cpu.append((fila, col))
                break
        if tablero_jugador[fila][col] == "⛵":
            tablero_jugador[fila][col] = "💥"
            print(f"La CPU disparó en {chr(65+fila)}{col+1}: ¡Impacto! 🎯")
        else:
            tablero_jugador[fila][col] = "💦"
            print(f"La CPU disparó en {chr(65+fila)}{col+1}: Agua 💦")
        # Verificar victoria CPU #
        if not quedan_barcos(tablero_jugador):
            print("\n¡LA CPU GANA! 😢")
            return
def jugar_2_jugadores():
    # === Modo de juego para dos jugadores === #
    jugador1 = input("Nombre Jugador 1: ")
    jugador2 = input("Nombre Jugador 2: ")
    # Crear tableros
    tablero1 = crear_tablero()
    tablero2 = crear_tablero()
    # Colocar barcos Jugador 1
    print(f"\n[{jugador1} COLOCA TUS BARCOS]")
    modo = input("¿Colocar barcos manualmente (M) o automáticamente (A)? ").upper()
    tablero1 = colocar_barcos(tablero1, "manual" if modo == "M" else "auto", jugador1)
    # Colocar barcos Jugador 2
    print(f"\n[{jugador2} COLOCA TUS BARCOS]")
    modo = input("¿Colocar barcos manualmente (M) o automáticamente (A)? ").upper()
    tablero2 = colocar_barcos(tablero2, "manual" if modo == "M" else "auto", jugador2)
    # Bucle principal del juego
    while True:
        # Turno Jugador 1
        print(f"\n[{jugador1} ATACA]")
        print(f"\n{jugador2}'s Tablero:")
        mostrar_tablero(tablero2, ocultar_barcos=True)
        resultado = realizar_disparo(tablero2, jugador1)
        if resultado == "guardar":
            guardar_partida({
                "modo": "2jugadores",
                "jugador1": jugador1,
                "jugador2": jugador2,
                "tablero1": tablero1,
                "tablero2": tablero2
            })
            return
        # Verificar victoria Jugador 1
        if not quedan_barcos(tablero2):
            print(f"\n¡{jugador1} GANA! 🏆")
            return
        # Turno Jugador 2
        print(f"\n[{jugador2} ATACA]")
        print(f"\n{jugador1}'s Tablero:")
        mostrar_tablero(tablero1, ocultar_barcos=True)

        resultado = realizar_disparo(tablero1, jugador2)
        if resultado == "guardar":
            guardar_partida({
                "modo": "2jugadores",
                "jugador1": jugador1,
                "jugador2": jugador2,
                "tablero1": tablero1,
                "tablero2": tablero2
            })
            return
        # Verificar victoria Jugador 2
        if not quedan_barcos(tablero1):
            print(f"\n¡{jugador2} GANA! 🏆")
            return
def continuar_partida():
    # === Continúa una partida guardada === #
    partida = cargar_partida()
    if not partida:
        print("No hay partida guardada")
        return
    if partida["modo"] == "cpu":
        print("\nContinuando partida vs CPU")
        nombre = partida["jugador"]
        tablero_jugador = partida["tablero_jugador"]
        tablero_cpu = partida["tablero_cpu"]
        disparos_cpu = partida["disparos_cpu"]
        while True:
            print("\n[TU TABLERO]")
            mostrar_tablero(tablero_jugador)
            print("\n[TABLERO ENEMIGO]")
            mostrar_tablero(tablero_cpu, ocultar_barcos=True)
            resultado = realizar_disparo(tablero_cpu, nombre)
            if resultado == "guardar":
                guardar_partida({
                    "modo": "cpu",
                    "jugador": nombre,
                    "tablero_jugador": tablero_jugador,
                    "tablero_cpu": tablero_cpu,
                    "disparos_cpu": disparos_cpu
                })
                return
            if not quedan_barcos(tablero_cpu):
                print(f"\n¡{nombre} GANA! 🏆")
                os.remove(ARCHIVO_PARTIDA)
                return
            print("\nTurno de la CPU...")
            while True:
                fila = random.randint(0, FILAS-1)
                col = random.randint(0, COLUMNAS-1)
                if (fila, col) not in disparos_cpu:
                    disparos_cpu.append((fila, col))
                    break
            if tablero_jugador[fila][col] == "⛵":
                tablero_jugador[fila][col] = "💥"
                print(f"La CPU disparó en {chr(65+fila)}{col+1}: ¡Impacto! 🎯")
            else:
                tablero_jugador[fila][col] = "💦"
                print(f"La CPU disparó en {chr(65+fila)}{col+1}: Agua 💦")
            if not quedan_barcos(tablero_jugador):
                print("\n¡LA CPU GANA! 😢")
                os.remove(ARCHIVO_PARTIDA)
                return
    else:  # Modo 2 jugadores
        print("\nContinuando partida de 2 jugadores")
        jugador1 = partida["jugador1"]
        jugador2 = partida["jugador2"]
        tablero1 = partida["tablero1"]
        tablero2 = partida["tablero2"]
        while True:
            # Turno Jugador 1
            print(f"\n[{jugador1} ATACA]")
            print(f"\n{jugador2}'s Tablero:")
            mostrar_tablero(tablero2, ocultar_barcos=True)
            resultado = realizar_disparo(tablero2, jugador1)
            if resultado == "guardar":
                guardar_partida({
                    "modo": "2jugadores",
                    "jugador1": jugador1,
                    "jugador2": jugador2,
                    "tablero1": tablero1,
                    "tablero2": tablero2
                })
                return
            if not quedan_barcos(tablero2):
                print(f"\n¡{jugador1} GANA! 🏆")
                os.remove(ARCHIVO_PARTIDA)
                return
            # Turno Jugador 2
            print(f"\n[{jugador2} ATACA]")
            print(f"\n{jugador1}'s Tablero:")
            mostrar_tablero(tablero1, ocultar_barcos=True)
            resultado = realizar_disparo(tablero1, jugador2)
            if resultado == "guardar":
                guardar_partida({
                    "modo": "2jugadores",
                    "jugador1": jugador1,
                    "jugador2": jugador2,
                    "tablero1": tablero1,
                    "tablero2": tablero2
                })
                return
            if not quedan_barcos(tablero1):
                print(f"\n¡{jugador2} GANA! 🏆")
                os.remove(ARCHIVO_PARTIDA)
                return
def menu_principal():
    # === Menú principal del juego === #
    while True:
        print("\n=== BATALLA NAVAL ===")
        print("1. Jugar vs CPU")
        print("2. Jugar 2 Jugadores")
        print("3. Continuar partida guardada")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_vs_cpu()
        elif opcion == "2":
            jugar_2_jugadores()
        elif opcion == "3":
            continuar_partida()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Intenta nuevamente")
# Iniciar el juego
if __name__ == "__main__":
    menu_principal()
#----------------------------------------------------------#
#----------------------------------------------------------#
#----------------------------------------------------------#

