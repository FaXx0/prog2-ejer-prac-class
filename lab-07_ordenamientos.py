def ordenamiento_de_burbuja(lista): # Función para ordenar una lista usando el algoritmo de burbuja
    n = len(lista) # Obtiene la longitud de la lista
    for i in range(n):  # Recorre la lista
      hubo_intercambio = False # Variable para verificar si hubo intercambio
      for j in range( n - 1 - i):  # Recorre la lista
          if lista[j] > lista[j + 1]:  # Compara los elementos
            #Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]# Intercambia los elementos
                hubo_intercambio = True # Indica que hubo intercambio
      if not hubo_intercambio: # Si no hubo intercambio
          break
    return lista # opcional: tambien se puede omitir el return y solo imprimir la lista
# Main
if __name__ == "__main__": # Si el archivo se ejecuta directamente
   numeros = [6, 3, 8, 2, 5] # Lista de números desordenados
   print("Antes:", numeros) # Imprime la lista original
   ordenamiento_de_burbuja(numeros) # Llamada a la función
   print("Después:", numeros) # Imprime la lista ordenada

