# Primero definimos la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ahora sí podemos obtener dimensiones y recorrer
num_filas = len(matriz)         # 3 filas
num_columnas = len(matriz[0])   # 3 columnas

# Recorremos usando índices
for i in range(num_filas):              # i = 0, 1, 2
    for j in range(num_columnas):       # j = 0, 1, 2
        elemento = matriz[i][j]
        print(f"Elemento en ({i},{j}) es {elemento}")

# Recorremos cada fila
for fila_actual in matriz:
    # Recorremos cada elemento dentro de la fila actual
    for elemento in fila_actual:
        print(elemento, end=" ")  # Imprime en la misma línea, separado por espacios
    print()  # Salto de línea al final de cada fila
print ("Fabrizzio Lora (FaXx0)")
#---------------------------------------------------------#
#---------------------------------------------------------#
#Laboratorio de matrices 
#Ejercicio 1: Imprimir una matriz
# 1. Crear la matriz 3x3 que representa el teclado numérico
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Imprimir la matriz completa
print("Matriz completa:")
for fila in teclado:
    print(fila)

# 3. Acceder e imprimir elementos específicos
print("\nNúmero en el centro:", teclado[1][1])  # El 5 (fila 1, columna 1)
print("Número en la esquina inferior derecha:", teclado[2][2])  # El 9 (fila 2, columna 2)

# 4. Modificar el número en la esquina superior izquierda (1 por 0)
teclado[0][0] = 0

# 5. Imprimir la matriz modificada
print("\nMatriz después de la modificación:")
for fila in teclado:
    print(fila) 
print("Fabrizzio Lora (FaXx0)")
#---------------------------------------------------------#
#---------------------------------------------------------#
#Laboratorio de matrices(Analicis matricial)
# Definimos la función que suma todos los elementos de una matriz
def sumar_total_matriz(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y retorna la suma total de todos sus elementos.
    Ejemplo:
    matriz = [[1, 2], [3, 4]]
    resultado = 10
    """
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total
 # Función para probar que sumar_total_matriz funciona correctamente
def probar_suma_total():
    print("Probando sumar_total_matriz...")
    # Caso 1: matriz normal
    m1 = [[1, 2, 3], [4, 5, 6]]
    assert sumar_total_matriz(m1) == 21  # 1+2+3+4+5+6 = 21
    # Caso 2: matriz con negativos y ceros
    m2 = [[-1, 0, 1], [10, -5, 5]]
    assert sumar_total_matriz(m2) == 10  # -1+0+1+10-5+5 = 10
    # ✅ Casos borde o límites
    assert sumar_total_matriz([[]]) == 0       # Matriz con una fila vacía
    assert sumar_total_matriz([]) == 0         # Matriz completamente vacía
    assert sumar_total_matriz([[42]]) == 42    # Matriz de un solo elemento
    print("¡Pruebas para sumar_total_matriz pasaron! (matricial)✅")
 # Llamamos a la función de pruebas
probar_suma_total() 

#----------------------------------------------------------#
#----------------------------------------------------------#
#Laboratorio de matrices(Suma por filas)
 # Definimos la función que suma los elementos por cada fila de la matriz
def sumar_por_filas(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y devuelve una lista con la suma de cada fila.
    Ejemplo:
    matriz = [[1, 2, 3], [4, 5, 6]]
    resultado = [6, 15]
    """
    resultado = []
    for fila in matriz:
        suma_fila = sum(fila)  # Suma todos los elementos de la fila
        resultado.append(suma_fila)
    return resultado
 # Función de prueba para verificar que sumar_por_filas funciona correctamente
def probar_suma_por_filas():
    print("\nProbando sumar_por_filas...")
    # Caso 1: matriz con 3 filas y 3 columnas
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_por_filas(m1) == [6, 15, 24]  # 1+2+3, 4+5+6, 7+8+9
    # Caso 2: matriz con pares repetidos
    m2 = [[10, 10], [20, 20], [30, 30]]
    assert sumar_por_filas(m2) == [20, 40, 60]
    # Caso borde: matriz vacía
    assert sumar_por_filas([]) == []  # No hay filas que sumar
    print("¡Pruebas para sumar_por_filas pasaron! ✅")
 # Llamamos a la función para ejecutar las pruebas
probar_suma_por_filas()

#----------------------------------------------------------#
#----------------------------------------------------------#
#Laboratorio de matrices(Suma de la diagonal principal))
 # Definimos la función que suma los elementos de la diagonal principal de una matriz cuadrada (misma cantidad de filas y columnas) y retorna la suma de los elementos en su diagonal principal. Ejemplo: matriz = [[1, 2],[3, 4]] diagonal principal: 1 y 4 → suma = 5
   
def sumar_diagonal_principal(matriz):
    """
    Esta función recibe una matriz cuadrada (misma cantidad de filas y columnas)
    y retorna la suma de los elementos en su diagonal principal.
    Ejemplo:
    matriz = [[1, 2],
              [3, 4]]
    diagonal principal: 1 y 4 → suma = 5
    """
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]  # Accede al elemento en la posición (i, i)
    return suma
 # Función de prueba para verificar que sumar_diagonal_principal funciona correctamente
def probar_suma_diagonal_principal():
    print("\nProbando sumar_diagonal_principal...")
    # Caso 1: matriz 3x3 con números consecutivos
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_diagonal_principal(m1) == 15  # 1 + 5 + 9
    # Caso 2: matriz 2x2 con ceros y valores definidos
    m2 = [[10, 0], [0, 20]]
    assert sumar_diagonal_principal(m2) == 30  # 10 + 20
    # Caso borde: matriz 1x1
    m3 = [[5]]
    assert sumar_diagonal_principal(m3) == 5  # Solo un elemento en la diagonal
    print("¡Pruebas para sumar_diagonal_principal pasaron! ✅")
 # Llamamos a la función para ejecutar las pruebas
probar_suma_diagonal_principal()
#print(f"sumar_diagonal_principal(m1) = {sumar_diagonal_principal( m1)}")

#----------------------------------------------------------#
#----------------------------------------------------------#
#Laboratorio de matrices(ejercicio adicional suma diagonal secundaria))))
 # Definimos la función que suma los elementos de la diagonal secundaria de una matriz cuadrada
def sumar_diagonal_secundaria(matriz):
    #Esta función recibe una matriz cuadrada (misma cantidad de filas y columnas) y retorna la suma de los elementos en su diagonal secundaria.Ejemplo: matriz = [[1, 2],[3, 4]] diagonal secundaria: 2 y 3 → suma = 5
        # Definimos la función que suma los elementos de la diagonal secundaria de una matriz cuadrada
    suma = 0  # Inicializamos la suma en 0
    n = len(matriz)  # Obtenemos la dimensión de la matriz (número de filas o columnas)
    for i in range(n):  # Iteramos sobre el rango de la dimensión de la matriz
        suma += matriz[i][n - 1 - i]  # Accedemos al elemento en la posición (i, n - 1 - i)
    return suma  # Retornamos la suma de los elementos de la diagonal secundaria

    # Función de prueba para verificar que sumar_diagonal_secundaria funciona correctamente
def probar_suma_diagonal_secundaria():
    print("\nProbando sumar_diagonal_secundaria...")
        # Caso 1: matriz 3x3 con números consecutivos
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_diagonal_secundaria(m1) == 15  # 3 + 5 + 7
        # Caso 2: matriz 2x2 con ceros y valores definidos
    m2 = [[10, 0], [0, 20]]
    assert sumar_diagonal_secundaria(m2) == 20  # 0 + 20
        # Caso borde: matriz 1x1
    m3 = [[5]]
    assert sumar_diagonal_secundaria(m3) == 5  # Solo un elemento en la diagonal
print("¡Pruebas para sumar_diagonal_secundaria pasaron! ✅")    # Llamamos a la función para ejecutar las pruebas
#----------------------------------------------------------#
#segunda_opcion
def sumar_diagonal_secundaria2(matriz_cuadrada):
    #Calcula la suma de los elementos en la diagonal secundaria de una matriz cuadrada.
    #La diagonal secundaria es la que va desde la esquina superior derecha hasta la esquina inferior      izquierda.
    
    #Parámetros:
    #matriz_cuadrada (list[list]): Matriz cuadrada (N x N) de números
    #Retorna:
    #int/float: Suma de los elementos en la diagonal secundaria
    #Lanza:
    #ValueError: Si la matriz no es cuadrada
    
    # Verificar si la matriz es cuadrada
    n = len(matriz_cuadrada)
    for fila in matriz_cuadrada:
        if len(fila) != n:
            raise ValueError("La matriz debe ser cuadrada (mismo número de filas y columnas)")

    # Calcular suma de diagonal secundaria
    suma = 0
    for i in range(n):
        j = n - 1 - i  # Índice de columna para la diagonal secundaria
        suma += matriz_cuadrada[i][j]

    return suma

# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

resultado = sumar_diagonal_secundaria2(matriz)
print(f"Suma de la diagonal secundaria2: {resultado}")  # Salida: 15 (3 + 5 + 7) # Llamamos a la función para ejecutar las pruebas y ejecutamos las pruebas de la función sumar_diagonal_secundaria2 con la matriz de ejemplo
