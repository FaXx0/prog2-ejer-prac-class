"""import random # Importa el módulo random para generar números aleatorios
import json # Importa el módulo json para guardar y cargar datos en formato JSON
import os # Importa el módulo os para manejar archivos y directorios
# ---------------------- USUARIOS ----------------------
ARCHIVO_USUARIOS = "usuarios.json" # Define el nombre del archivo para guardar los usuarios
ARCHIVO_PARTIDA = "partida.json" # Define el nombre del archivo para guardar la partida


def cargar_usuarios(): # Función para cargar los usuarios desde el archivo JSON
    if os.path.exists(ARCHIVO_USUARIOS): # Si el archivo existe, lo abre y carga los datos
        with open(ARCHIVO_USUARIOS, "r") as f: # Abre el archivo en modo lectura
            return json.load(f) # Carga los datos del archivo en formato JSON
    return {} # Si el archivo no existe, retorna un diccionario vacío


def guardar_usuarios(usuarios): # Función para guardar los usuarios en el archivo JSON
    with open(ARCHIVO_USUARIOS, "w") as f: # Abre el archivo en modo escritura
        json.dump(usuarios, f, indent=4) # Guarda los datos en formato JSON con indentación de 4 espacios


def registrar_usuario(): # Función para registrar un nuevo usuario
    usuarios = cargar_usuarios() # Carga los usuarios existentes
    nombre = input("Ingresa nuevo nombre de usuario: ") # Solicita el nombre del usuario
    if nombre in usuarios: # Si el nombre ya está registrado, muestra un mensaje de error
        print("El nombre ya está registrado.") # Mensaje de error
        return None # Retorna None para indicar que no se registró el usuario
    contraseña = input("Crea una contraseña: ") # Solicita la contraseña del usuario
    usuarios[nombre] = {"contraseña": contraseña} # Guarda la contraseña del usuario en el diccionario de usuarios
    guardar_usuarios(usuarios) # Guarda los usuarios en el archivo JSON
    print("Registro exitoso.") # Mensaje de éxito
    return nombre     # Retorna el nombre del usuario registrado    


def iniciar_sesion(): # Función para iniciar sesión con un usuario existente
    usuarios = cargar_usuarios() # Carga los usuarios existentes
    nombre = input("Nombre de usuario: ") # Solicita el nombre del usuario
    if nombre not in usuarios: # Si el nombre no está registrado, muestra un mensaje de error
        print("Usuario no registrado.") # Mensaje de error
        return None # Retorna None para indicar que no se inició sesión
    contraseña = input("Contraseña: ") # Solicita la contraseña del usuario     
    if usuarios[nombre]["contraseña"] != contraseña: # Si la contraseña no coincide, muestra un mensaje de error
        print("Contraseña incorrecta.") # Mensaje de error
        return None # Retorna None para indicar que no se inició sesión
    print(f"Bienvenido, {nombre}") # Mensaje de bienvenida
    return nombre # Retorna el nombre del usuario que inició sesión


# ---------------------- UTILIDADES ----------------------
def crear_tablero(): # Función para crear un tablero de 4x4 con agua (~)
    return [["~" for _ in range(4)] for _ in range(4)] # BatallaNaval_mejorada.py


def mostrar_tablero(tablero): # Función para mostrar el tablero en la consola
    print() # Salto de línea
    for fila in tablero: # Itera sobre cada fila del tablero
        print(" ".join(fila)) # Imprime la fila con un espacio entre cada elemento


def pedir_coordenadas(nombre): # Función para pedir coordenadas al usuario
    while True:  # Bucle hasta que el usuario ingrese coordenadas válidas
        try: # Intenta convertir las entradas del usuario a enteros
            fila = int(input(f"{nombre}, ingresa fila (1-4): ")) - 1 # Solicita la fila y resta 1 para convertirla a índice
            col = int(input(f"{nombre}, ingresa columna (1-4): ")) - 1  # Solicita la columna y resta 1 para convertirla a índice
            if 0 <= fila <= 3 and 0 <= col <= 3: # Si las coordenadas están dentro del rango, retorna las coordenadas
                return fila, col # Retorna las coordenadas
            else: # Si las coordenadas están fuera del rango, muestra un mensaje de error
                print("Coordenadas fuera de rango. Intenta de nuevo.") # Mensaje de error
        except ValueError: # Si las entradas no son números válidos, muestra un mensaje de error
            print("Entrada inválida. Usa solo números del 1 al 4.") # Mensaje de error


# ---------------------- GUARDADO ----------------------
def guardar_partida(datos): # Función para guardar la partida en el archivo JSON
    with open(ARCHIVO_PARTIDA, "w") as f: # Abre el archivo en modo escritura
        json.dump(datos, f) # Guarda los datos en formato JSON


def cargar_partida(): # Función para cargar la partida desde el archivo JSON
    if os.path.exists(ARCHIVO_PARTIDA): # Si el archivo existe, lo abre y carga los datos
        with open(ARCHIVO_PARTIDA, "r") as f: # Abre el archivo en modo lectura
            return json.load(f) # Carga los datos del archivo en formato JSON
    return None # Si el archivo no existe, retorna None


def borrar_partida(): # Función para borrar la partida guardada
    if os.path.exists(ARCHIVO_PARTIDA): # Si el archivo existe, lo borra
        os.remove(ARCHIVO_PARTIDA) # Borra el archivo


# ---------------------- MODO VS COMPUTADORA ----------------------
def jugar_vs_computadora(jugador): # Función para jugar contra la computadora
    print("\n=== Modo: Jugador vs Computadora ===") # Mensaje de bienvenida
    tablero = crear_tablero() # Crea un tablero de 4x4 con agua (~)

    print(f"{jugador}, coloca tu barco:") # Solicita al usuario que coloque su barco
    barco_jugador = pedir_coordenadas(jugador) # Pide las coordenadas del barco del usuario
    barco_pc = (random.randint(0, 3), random.randint(0, 3)) # Genera las coordenadas del barco de la computadora

    while True: # Bucle hasta que alguien gane
        mostrar_tablero(tablero) # Muestra el tablero en la consola
        print(f"\n{jugador}, intenta adivinar el barco de la computadora:") # Solicita al usuario que adivine el barco de la computadora
        fila, col = pedir_coordenadas(jugador) # Pide las coordenadas del ataque del usuario
        if tablero[fila][col] != "~": # Si el usuario ya atacó ahí, muestra un mensaje de error
            print("Ya atacaste ahí. Intenta otra vez.") # Mensaje de error
            continue # Continúa con la siguiente iteración del bucle # Si el usuario acertó el barco de la computadora, muestra un mensaje de victoria

        if (fila, col) == barco_pc: # Si el usuario acertó el barco de la computadora, muestra un mensaje de victoria
            tablero[fila][col] = "X" # Marca el barco de la computadora en el tablero
            mostrar_tablero(tablero) # Muestra el tablero en la consola
            print(f"\n¡{jugador} ganó! Hundiste el barco de la computadora.") # Mensaje de victoria
            borrar_partida() # Borra la partida guardada
            break # Termina el bucle
        else: # Si el usuario falló el ataque, muestra un mensaje de error
            tablero[fila][col] = "O" # Marca el fallo del usuario en el tablero
            print("Fallaste. Turno de la computadora.") # Mensaje de error

        fila_pc = random.randint(0, 3) # Genera la fila del ataque de la computadora
        col_pc = random.randint(0, 3) # Genera la columna del ataque de la computadora
        print(f"La computadora atacó la posición ({fila_pc+1}, {col_pc+1})") # Muestra el ataque de la computadora

        if (fila_pc, col_pc) == barco_jugador: # Si la computadora acertó el barco del usuario, muestra un mensaje de derrota
            print("La computadora acertó. Perdiste.") # Mensaje de derrota
            borrar_partida() # Borra la partida guardada
            break # Termina el bucle
        else: # Si la computadora falló el ataque, muestra un mensaje de error
            print("La computadora falló.") # Mensaje de error # Guarda la partida en el archivo JSON
 
        datos = { # Guarda la partida en el archivo JSON
            "modo": "vs_pc", # Guarda el modo de juego
            "jugador": jugador, # Guarda el nombre del jugador
            "tablero": tablero, # Guarda el tablero
            "barco_jugador": barco_jugador,    # Guarda las coordenadas del barco del jugador
            "barco_pc": barco_pc 
        } # Guarda las coordenadas del barco de la computadora
        guardar_partida(datos) # Guarda la partida en el archivo JSON


def reanudar_vs_computadora(datos): # Función para reanudar la partida contra la computadora
    jugador = datos["jugador"]  # Carga el nombre del jugador desde los datos guardados    
    tablero = datos["tablero"] # Carga el tablero desde los datos guardados
    barco_jugador = tuple(datos["barco_jugador"]) # Carga las coordenadas del barco del jugador desde los datos guardados
    barco_pc = tuple(datos["barco_pc"]) # Carga las coordenadas del barco de la computadora desde los datos guardados

    print("\n=== Reanudando partida contra la computadora ===")

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
            borrar_partida()
            break
        else:
            tablero[fila][col] = "O"
            print("Fallaste. Turno de la computadora.")

        fila_pc = random.randint(0, 3)
        col_pc = random.randint(0, 3)
        print(f"La computadora atacó la posición ({fila_pc+1}, {col_pc+1})")

        if (fila_pc, col_pc) == barco_jugador:
            print("La computadora acertó. Perdiste.")
            borrar_partida()
            break
        else:
            print("La computadora falló.")

        datos["tablero"] = tablero
        guardar_partida(datos)


# ---------------------- MODO 2 JUGADORES ----------------------
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
                borrar_partida()
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
                borrar_partida()
                break
            else:
                tablero1[f][c] = "O"
                print("Fallaste.")

        turno += 1

        datos = {
            "modo": "2_jugadores",
            "jugador1": jugador1,
            "jugador2": jugador2,
            "tablero1": tablero1,
            "tablero2": tablero2,
            "barco1": barco1,
            "barco2": barco2,
            "turno": turno
        }
        guardar_partida(datos)


def reanudar_2_jugadores(datos):
    jugador1 = datos["jugador1"]
    jugador2 = datos["jugador2"]
    tablero1 = datos["tablero1"]
    tablero2 = datos["tablero2"]
    barco1 = tuple(datos["barco1"])
    barco2 = tuple(datos["barco2"])
    turno = datos["turno"]

    print("\n=== Reanudando partida 2 jugadores ===")

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
                borrar_partida()
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
                borrar_partida()
                break
            else:
                tablero1[f][c] = "O"
                print("Fallaste.")

        turno += 1

        datos_actualizados = {
            "modo": "2_jugadores",
            "jugador1": jugador1,
            "jugador2": jugador2,
            "tablero1": tablero1,
            "tablero2": tablero2,
            "barco1": barco1,
            "barco2": barco2,
            "turno": turno
        }
        guardar_partida(datos_actualizados)


# ---------------------- MENÚ PRINCIPAL ----------------------
def menu():
    usuario_actual = None

    while not usuario_actual:
        print("\n=== Iniciar sesión ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario_actual = iniciar_sesion()
        elif opcion == "2":
            usuario_actual = registrar_usuario()
        elif opcion == "3":
            print("Adiós.")
            return
        else:
            print("Opción inválida.")

    while True:
        print(f"\n=== Menú de Batalla Naval ({usuario_actual}) ===")
        print("1. Jugar contra la computadora")
        print("2. Jugar 2 jugadores")
        print("3. Continuar partida guardada")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar_vs_computadora(usuario_actual)
        elif opcion == "2":
            jugar_2_jugadores()
        elif opcion == "3":
            datos = cargar_partida()
            if datos:
                if datos["modo"] == "vs_pc" and datos[
                        "jugador"] == usuario_actual:
                    reanudar_vs_computadora(datos)
                elif datos["modo"] == "2_jugadores":
                    reanudar_2_jugadores(datos)
                else:
                    print("No tienes permiso para continuar esta partida.")
            else:
                print("No hay partida guardada.")
        elif opcion == "4":
            print("Saliendo del juego.")
            break
        else:
            print("Opción inválida.")


# Iniciar programa
menu()"""
#----------------------------------------------------------#
#----------------------------------------------------------#
"""import random

FILAS = 4
COLUMNAS = 2
BARCOS = 3

# Crear un tablero vacío
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Mostrar el tablero
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == 1:
                fila_mostrar.append("0")
            elif celda == 0:
                fila_mostrar.append("0")
            elif celda == 1:
                fila_mostrar.append("1")
            elif celda == 2:
                fila_mostrar.append("X")
            elif celda == 3:
                fila_mostrar.append("*")
        print(letra + " " + " ".join(fila_mostrar))

# Convertir coordenada tipo "A3" a índices [fila][columna]
def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna

# Colocar barcos aleatoriamente
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

# Ejecutar disparo
def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    fila, columna = coord_a_indices(coord)
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print(f"{nombre} hizo ¡Tocado!")
    elif tablero_objetivo[fila][columna] in [0]:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print(f"{nombre} disparó al agua.")
    else:
        print("Ya se disparó allí.")

# Comprobar si quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False

# Guardar puntuación
def guardar_puntuacion(nombre):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida.\n")

# Menú principal del juego
def juego():
    print("=== Batalla Naval ===")
    print("1. Jugar contra la CPU")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona modo (1 o 2): ")

    if modo == "1":
        nombre_jugador = input("Tu nombre: ")
        nombre_cpu = "CPU"

        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()

        colocar_barcos(tablero_jugador, BARCOS)
        colocar_barcos(tablero_cpu, BARCOS)

        turno = 1
        while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
            print(f"\n--- Turno {turno} ---")
            print("Tu tablero:")
            mostrar_tablero(tablero_jugador)
            print("Tus disparos:")
            mostrar_tablero(disparos_jugador)

            coord = input("Dispara (ej. A3): ")
            disparar(tablero_cpu, disparos_jugador, coord, nombre_jugador)

            # Turno CPU
            while True:
                fila_cpu = random.randint(0, FILAS - 1)
                col_cpu = random.randint(0, COLUMNAS - 1)
                if tablero_jugador[fila_cpu][col_cpu] in [0, 1]:
                    break
            coord_cpu = f"{chr(ord('A') + fila_cpu)}{col_cpu + 1}"
            print(f"{nombre_cpu} dispara a {coord_cpu}")
            disparar(tablero_jugador, disparos_cpu, coord_cpu, nombre_cpu)
            turno += 1

        if quedan_barcos(tablero_jugador):
            print(f"¡{nombre_jugador} gana!")
            guardar_puntuacion(nombre_jugador)
        else:
            print("¡La CPU gana!")

    elif modo == "2":
        nombre1 = input("Nombre del Jugador 1: ")
        nombre2 = input("Nombre del Jugador 2: ")

        tablero1 = crear_tablero()
        tablero2 = crear_tablero()
        disparos1 = crear_tablero()
        disparos2 = crear_tablero()

        colocar_barcos(tablero1, BARCOS)
        colocar_barcos(tablero2, BARCOS)

        turno = 1
        while quedan_barcos(tablero1) and quedan_barcos(tablero2):
            print(f"\n--- Turno {turno} ---")

            print(f"{nombre1}, este es tu turno")
            mostrar_tablero(disparos1)
            coord = input("Dispara (ej. A3): ")
            disparar(tablero2, disparos1, coord, nombre1)

            if not quedan_barcos(tablero2):
                break

            print(f"\n{nombre2}, este es tu turno")
            mostrar_tablero(disparos2)
            coord = input("Dispara (ej. A3): ")
            disparar(tablero1, disparos2, coord, nombre2)

            turno += 1

        if quedan_barcos(tablero2):
            print(f"¡{nombre1} gana!")
            guardar_puntuacion(nombre1)
        else:
            print(f"¡{nombre2} gana!")
            guardar_puntuacion(nombre2)
    else:
        print("Opción inválida. Reinicia el programa.")

# Ejecutar juego
juego()"""
#----------------------------------------------------------#
#----------------------------------------------------------#
#----------------------------------------------------------#
import random
import json
import os

# Configuración del juego
FILAS = 4
COLUMNAS = 4
NUM_BARCOS = 3
ARCHIVO_PARTIDA = "batalla_naval_save.json"

def crear_tablero():
    """Crea un tablero vacío"""
    return [["🌊" for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_tablero(tablero, ocultar_barcos=False):
    """Muestra el tablero con formato"""
    print("\n  " + " ".join(str(i+1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        print(chr(65+i) + " ", end="")
        for celda in fila:
            if ocultar_barcos and celda == "⛵":
                print("🌊 ", end="")
            else:
                print(celda + " ", end="")
        print()

def colocar_barcos(tablero, modo, jugador=""):
    """Coloca barcos en el tablero según el modo seleccionado"""
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
    """Realiza un disparo en el tablero"""
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
    """Verifica si quedan barcos en el tablero"""
    for fila in tablero:
        if "⛵" in fila:
            return True
    return False

def guardar_partida(partida):
    """Guarda la partida en un archivo"""
    with open(ARCHIVO_PARTIDA, 'w') as f:
        json.dump(partida, f)
    print("Partida guardada correctamente")

def cargar_partida():
    """Carga una partida desde un archivo"""
    if not os.path.exists(ARCHIVO_PARTIDA):
        return None

    try:
        with open(ARCHIVO_PARTIDA, 'r') as f:
            return json.load(f)
    except:
        return None

def jugar_vs_cpu():
    """Modo de juego contra la computadora"""
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

        # Verificar victoria CPU
        if not quedan_barcos(tablero_jugador):
            print("\n¡LA CPU GANA! 😢")
            return

def jugar_2_jugadores():
    """Modo de juego para dos jugadores"""
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
    """Continúa una partida guardada"""
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
    """Menú principal del juego"""
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
#----------------------------------------------------------#

import random
import json
import os

# ---------------------- CONFIGURACIÓN ----------------------
ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_PARTIDA = "partida.json"
FILAS = 4
COLUMNAS = 4
BARCOS = 3

# ---------------------- USUARIOS ----------------------
def cargar_usuarios():
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def registrar_usuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingresa nuevo nombre de usuario: ")
    if nombre in usuarios:
        print("El nombre ya está registrado.")
        return None
    contraseña = input("Crea una contraseña: ")
    usuarios[nombre] = {"contraseña": contraseña}
    guardar_usuarios(usuarios)
    print("Registro exitoso.")
    return nombre

def iniciar_sesion():
    usuarios = cargar_usuarios()
    nombre = input("Nombre de usuario: ")
    if nombre not in usuarios:
        print("Usuario no registrado.")
        return None
    contraseña = input("Contraseña: ")
    if usuarios[nombre]["contraseña"] != contraseña:
        print("Contraseña incorrecta.")
        return None
    print(f"Bienvenido, {nombre}")
    return nombre

# ---------------------- TABLERO ----------------------
def crear_tablero():
    return [["~" for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("\n  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == "B":
                fila_mostrar.append("~")
            elif celda == "~":
                fila_mostrar.append("~")
            elif celda == "B":
                fila_mostrar.append("B")
            elif celda == "X":
                fila_mostrar.append("X")
            elif celda == "O":
                fila_mostrar.append("O")
        print(letra + " " + " ".join(fila_mostrar))

def coord_a_indices(coord):
    try:
        fila = ord(coord[0].upper()) - ord('A')
        columna = int(coord[1:]) - 1
        if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            return fila, columna
        return None
    except (ValueError, IndexError):
        return None

def colocar_barcos_manual(tablero, nombre):
    print(f"\n{nombre}, coloca tus {BARCOS} barcos:")
    barcos = []
    for i in range(BARCOS):
        while True:
            mostrar_tablero(tablero)
            coord = input(f"Barco {i+1} (ej. A1): ")
            pos = coord_a_indices(coord)
            if not pos:
                print("Coordenada inválida. Formato: LetraNúmero (ej. A1)")
                continue
            fila, col = pos
            if tablero[fila][col] == "B":
                print("Ya hay un barco en esa posición.")
                continue
            tablero[fila][col] = "B"
            barcos.append((fila, col))
            break
    return barcos

def colocar_barcos_aleatorio(tablero):
    barcos = []
    for _ in range(BARCOS):
        while True:
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            if tablero[fila][col] != "B":
                tablero[fila][col] = "B"
                barcos.append((fila, col))
                break
    return barcos

def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    pos = coord_a_indices(coord)
    if not pos:
        print("Coordenada inválida. Formato: LetraNúmero (ej. A1)")
        return False

    fila, col = pos
    if tablero_disparos[fila][col] in ["X", "O"]:
        print("Ya disparaste aquí.")
        return False

    if tablero_objetivo[fila][col] == "B":
        tablero_objetivo[fila][col] = "X"
        tablero_disparos[fila][col] = "X"
        print(f"¡{nombre} hizo TOCADO!")
        return True
    else:
        tablero_objetivo[fila][col] = "O"
        tablero_disparos[fila][col] = "O"
        print(f"¡{nombre} falló!")
        return False

def quedan_barcos(tablero):
    for fila in tablero:
        if "B" in fila:
            return True
    return False

# ---------------------- GUARDADO ----------------------
def guardar_partida(datos):
    with open(ARCHIVO_PARTIDA, "w") as f:
        json.dump(datos, f)

def cargar_partida():
    if os.path.exists(ARCHIVO_PARTIDA):
        with open(ARCHIVO_PARTIDA, "r") as f:
            return json.load(f)
    return None

def borrar_partida():
    if os.path.exists(ARCHIVO_PARTIDA):
        os.remove(ARCHIVO_PARTIDA)

# ---------------------- MODO VS COMPUTADORA ----------------------
def jugar_vs_computadora(jugador):
    print("\n=== Modo: Jugador vs Computadora ===")

    # Crear tableros
    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    disparos_jugador = crear_tablero()

    # Colocar barcos
    barcos_jugador = colocar_barcos_manual(tablero_jugador, jugador)
    barcos_cpu = colocar_barcos_aleatorio(tablero_cpu)

    turno = 0
    while True:
        turno += 1
        print(f"\n--- Turno {turno} ---")

        # Turno jugador
        print(f"\n{jugador}, tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("\nTus disparos:")
        mostrar_tablero(disparos_jugador, ocultar_barcos=True)

        while True:
            coord = input("\nDispara (ej. A1): ")
            if disparar(tablero_cpu, disparos_jugador, coord, jugador):
                break

        if not quedan_barcos(tablero_cpu):
            print(f"\n¡{jugador} ganó! Hundiste todos los barcos de la computadora.")
            borrar_partida()
            return

        # Turno computadora
        print("\nTurno de la computadora...")
        while True:
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            coord_cpu = f"{chr(ord('A') + fila)}{col + 1}"
            if disparar(tablero_jugador, tablero_jugador, coord_cpu, "Computadora"):
                print(f"La computadora disparó a {coord_cpu} y ¡ACERTÓ!")
                break
            elif tablero_jugador[fila][col] == "O":
                continue
            else:
                print(f"La computadora disparó a {coord_cpu} y falló.")
                break

        if not quedan_barcos(tablero_jugador):
            print("\n¡La computadora ganó! Hundió todos tus barcos.")
            borrar_partida()
            return

        # Guardar partida
        datos = {
            "modo": "vs_pc",
            "jugador": jugador,
            "tablero_jugador": tablero_jugador,
            "tablero_cpu": tablero_cpu,
            "disparos_jugador": disparos_jugador,
            "barcos_jugador": barcos_jugador,
            "barcos_cpu": barcos_cpu,
            "turno": turno
        }
        guardar_partida(datos)

def reanudar_vs_computadora(datos):
    jugador = datos["jugador"]
    tablero_jugador = datos["tablero_jugador"]
    tablero_cpu = datos["tablero_cpu"]
    disparos_jugador = datos["disparos_jugador"]
    barcos_jugador = [tuple(barco) for barco in datos["barcos_jugador"]]
    barcos_cpu = [tuple(barco) for barco in datos["barcos_cpu"]]
    turno = datos["turno"]

    print("\n=== Reanudando partida contra la computadora ===")

    while True:
        turno += 1
        print(f"\n--- Turno {turno} ---")

        # Turno jugador
        print(f"\n{jugador}, tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("\nTus disparos:")
        mostrar_tablero(disparos_jugador, ocultar_barcos=True)

        while True:
            coord = input("\nDispara (ej. A1): ")
            if disparar(tablero_cpu, disparos_jugador, coord, jugador):
                break

        if not quedan_barcos(tablero_cpu):
            print(f"\n¡{jugador} ganó! Hundiste todos los barcos de la computadora.")
            borrar_partida()
            return

        # Turno computadora
        print("\nTurno de la computadora...")
        while True:
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            coord_cpu = f"{chr(ord('A') + fila)}{col + 1}"
            if disparar(tablero_jugador, tablero_jugador, coord_cpu, "Computadora"):
                print(f"La computadora disparó a {coord_cpu} y ¡ACERTÓ!")
                break
            elif tablero_jugador[fila][col] == "O":
                continue
            else:
                print(f"La computadora disparó a {coord_cpu} y falló.")
                break

        if not quedan_barcos(tablero_jugador):
            print("\n¡La computadora ganó! Hundió todos tus barcos.")
            borrar_partida()
            return

        # Actualizar guardado
        datos_actualizados = {
            "modo": "vs_pc",
            "jugador": jugador,
            "tablero_jugador": tablero_jugador,
            "tablero_cpu": tablero_cpu,
            "disparos_jugador": disparos_jugador,
            "barcos_jugador": barcos_jugador,
            "barcos_cpu": barcos_cpu,
            "turno": turno
        }
        guardar_partida(datos_actualizados)

# ---------------------- MODO 2 JUGADORES ----------------------
def jugar_2_jugadores():
    print("\n=== Modo: Jugador vs Jugador ===")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")

    # Crear tableros
    tablero1 = crear_tablero()
    tablero2 = crear_tablero()
    disparos1 = crear_tablero()
    disparos2 = crear_tablero()

    # Colocar barcos
    print(f"\n{jugador1}, coloca tus barcos:")
    barcos1 = colocar_barcos_manual(tablero1, jugador1)

    print(f"\n{jugador2}, coloca tus barcos:")
    barcos2 = colocar_barcos_manual(tablero2, jugador2)

    turno = 0
    while True:
        turno += 1
        print(f"\n--- Turno {turno} ---")

        # Turno jugador 1
        print(f"\nTurno de {jugador1}")
        print(f"\n{jugador1}, tu tablero:")
        mostrar_tablero(tablero1)
        print(f"\nTus disparos contra {jugador2}:")
        mostrar_tablero(disparos1, ocultar_barcos=True)

        while True:
            coord = input(f"\n{jugador1}, dispara (ej. A1): ")
            if disparar(tablero2, disparos1, coord, jugador1):
                break

        if not quedan_barcos(tablero2):
            print(f"\n¡{jugador1} ganó! Hundiste todos los barcos de {jugador2}.")
            borrar_partida()
            return

        # Turno jugador 2
        print(f"\nTurno de {jugador2}")
        print(f"\n{jugador2}, tu tablero:")
        mostrar_tablero(tablero2)
        print(f"\nTus disparos contra {jugador1}:")
        mostrar_tablero(disparos2, ocultar_barcos=True)

        while True:
            coord = input(f"\n{jugador2}, dispara (ej. A1): ")
            if disparar(tablero1, disparos2, coord, jugador2):
                break

        if not quedan_barcos(tablero1):
            print(f"\n¡{jugador2} ganó! Hundiste todos los barcos de {jugador1}.")
            borrar_partida()
            return

        # Guardar partida
        datos = {
            "modo": "2_jugadores",
            "jugador1": jugador1,
            "jugador2": jugador2,
            "tablero1": tablero1,
            "tablero2": tablero2,
            "disparos1": disparos1,
            "disparos2": disparos2,
            "barcos1": barcos1,
            "barcos2": barcos2,
            "turno": turno
        }
        guardar_partida(datos)

def reanudar_2_jugadores(datos):
    jugador1 = datos["jugador1"]
    jugador2 = datos["jugador2"]
    tablero1 = datos["tablero1"]
    tablero2 = datos["tablero2"]
    disparos1 = datos["disparos1"]
    disparos2 = datos["disparos2"]
    barcos1 = [tuple(barco) for barco in datos["barcos1"]]
    barcos2 = [tuple(barco) for barco in datos["barcos2"]]
    turno = datos["turno"]

    print("\n=== Reanudando partida 2 jugadores ===")

    while True:
        turno += 1
        print(f"\n--- Turno {turno} ---")

        # Turno jugador 1
        print(f"\nTurno de {jugador1}")
        print(f"\n{jugador1}, tu tablero:")
        mostrar_tablero(tablero1)
        print(f"\nTus disparos contra {jugador2}:")
        mostrar_tablero(disparos1, ocultar_barcos=True)

        while True:
            coord = input(f"\n{jugador1}, dispara (ej. A1): ")
            if disparar(tablero2, disparos1, coord, jugador1):
                break

        if not quedan_barcos(tablero2):
            print(f"\n¡{jugador1} ganó! Hundiste todos los barcos de {jugador2}.")
            borrar_partida()
            return

        # Turno jugador 2
        print(f"\nTurno de {jugador2}")
        print(f"\n{jugador2}, tu tablero:")
        mostrar_tablero(tablero2)
        print(f"\nTus disparos contra {jugador1}:")
        mostrar_tablero(disparos2, ocultar_barcos=True)

        while True:
            coord = input(f"\n{jugador2}, dispara (ej. A1): ")
            if disparar(tablero1, disparos2, coord, jugador2):
                break

        if not quedan_barcos(tablero1):
            print(f"\n¡{jugador2} ganó! Hundiste todos los barcos de {jugador1}.")
            borrar_partida()
            return

        # Actualizar guardado
        datos_actualizados = {
            "modo": "2_jugadores",
            "jugador1": jugador1,
            "jugador2": jugador2,
            "tablero1": tablero1,
            "tablero2": tablero2,
            "disparos1": disparos1,
            "disparos2": disparos2,
            "barcos1": barcos1,
            "barcos2": barcos2,
            "turno": turno
        }
        guardar_partida(datos_actualizados)

# ---------------------- MENÚ PRINCIPAL ----------------------
def menu():
    usuario_actual = None

    while not usuario_actual:
        print("\n=== Batalla Naval ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario_actual = iniciar_sesion()
        elif opcion == "2":
            usuario_actual = registrar_usuario()
        elif opcion == "3":
            print("Adiós.")
            return
        else:
            print("Opción inválida.")

    while True:
        print(f"\n=== Menú Principal ({usuario_actual}) ===")
        print("1. Jugar contra la computadora")
        print("2. Jugar 2 jugadores")
        print("3. Continuar partida guardada")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar_vs_computadora(usuario_actual)
        elif opcion == "2":
            jugar_2_jugadores()
        elif opcion == "3":
            datos = cargar_partida()
            if datos:
                if datos["modo"] == "vs_pc" and datos["jugador"] == usuario_actual:
                    reanudar_vs_computadora(datos)
                elif datos["modo"] == "2_jugadores":
                    reanudar_2_jugadores(datos)
                else:
                    print("No tienes permiso para continuar esta partida.")
            else:
                print("No hay partida guardada.")
        elif opcion == "4":
            print("Saliendo del juego.")
            break
        else:
            print("Opción inválida.")

# Iniciar programa
if __name__ == "__main__":
    menu()