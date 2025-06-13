# busqueda_binaria_con_pruebas.py

def busqueda_binaria(lista, objetivo): # Función para realizar búsqueda binaria en una lista ordenada
    """
    Realiza búsqueda binaria en una lista ordenada. # Descripción de la función # Parámetros de la función # Retorno de la función # Fin de la función

    Args: # Parámetros de la función
        lista (list): Lista ordenada de elementos.     # Descripción del parámetro lista
        objetivo (int): Elemento que se desea encontrar. # Descripción del parámetro objetivo

    Returns: # Retorno de la función
        int: Índice del elemento si se encuentra, -1 si no. # Descripción del retorno de la función
    """ 
    inicio = 0 # Inicializa el índice inicial
    fin = len(lista) - 1  # Inicializa el índice final

    while inicio <= fin: # Bucle hasta que el índice inicial sea mayor al índice final
        medio = (inicio + fin) // 2 # Calcula el índice medio
        valor_medio = lista[medio] # Obtiene el valor del índice medio # Compara el valor del índice medio con el objetivo # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio, actualiza el índice inicial # Si el objetivo no se encuentra en la lista, retorna -1 # Fin de la función
        if valor_medio == objetivo: # Si el valor del índice medio es igual al objetivo # Compara el valor del índice medio con el objetivo # Si el valor del índice medio es igual al objetivo, retorna el índice medio
            return medio # Retorna el índice medio # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio, actualiza el índice inicial # Si el objetivo no se encuentra en la lista, retorna -1 # Fin
        elif objetivo < valor_medio: # Si el objetivo es menor al valor del índice medio # Compara el valor del índice medio con el objetivo # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio, actualiza el índice inicial # Si el objetivo no se encuentra en la lista, retorna -1 # Fin
            fin = medio - 1 # Actualiza el índice final # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio
        else: # Si el objetivo es mayor al valor del índice medio # Compara el valor del índice medio con el objetivo # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio, actualiza el índice inicial # Si el objetivo no se encuentra en la lista, retorna -1 # Fin
            inicio = medio + 1 # Actualiza el índice inicial # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio # Si el objetivo no se encuentra en la lista, retorna -1 # Fin
    return -1  # Retorna -1 si el objetivo no se encuentra en la lista # Si el valor del índice medio es igual al objetivo, retorna el índice medio # Si el objetivo es menor al valor del índice medio, actualiza el índice final # Si el objetivo es mayor al valor del índice medio # Si el objetivo no se encuentra en la lista, retorna -1 # Fin
def probar_busqueda_binaria(): # Función para probar la función busqueda_binaria # Pruebas para la función busqueda_binaria usando assert # Pruebas exitosas (elemento está en la lista) # Pruebas fallidas (elemento no está en la lista) # Fin de la función # Fin de la función
    """
    Pruebas para la función busqueda_binaria usando assert. # Pruebas exitosas (elemento está en la lista) # Pruebas fallidas (elemento no está en la lista) # Fin de la función # Fin de la función
    """
    lista = [1, 3, 5, 7, 9, 11, 13, 15] # Lista ordenada para pruebas # Pruebas exitosas (elemento está en la lista) # Pruebas fallidas (elemento no está en la lista) # Fin de la función # Fin de la función

    # Pruebas exitosas (elemento está en la lista) 
    assert busqueda_binaria(lista, 1) == 0 # Prueba 1
    assert busqueda_binaria(lista, 5) == 2 # Prueba 2
    assert busqueda_binaria(lista, 15) == 7 # Prueba 3

    # Pruebas fallidas (elemento no está en la lista)
    assert busqueda_binaria(lista, 0) == -1 # Prueba 4
    assert busqueda_binaria(lista, 6) == -1 # Prueba 5
    assert busqueda_binaria(lista, 20) == -1 # Prueba 6

    print("✅ Todas las pruebas pasaron correctamente.") # Mensaje de éxito # Fin de la función # Fin de la función


# Ejecutar pruebas solo si se corre este archivo directamente
if __name__ == "__main__": # Si el archivo se ejecuta directamente, ejecuta la función probar_busqueda_binaria() # Fin de la función # Fin de la función  
    probar_busqueda_binaria() # Ejecuta la función probar_busqueda_binaria() # Fin de la función # Fin de la función 
