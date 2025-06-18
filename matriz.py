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
