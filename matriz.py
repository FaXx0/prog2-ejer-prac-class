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