# busqueda_lineal_desordenada.py

def busqueda_lineal(lista, objetivo, mostrar_pasos=False):
    """
    Realiza búsqueda lineal en una lista desordenada.

    Args:
        lista (list): Lista de elementos (puede estar desordenada).
        objetivo (int): Elemento que se desea encontrar.
        mostrar_pasos (bool): Si es True, muestra cada comparación.

    Returns:
        int: Índice del objetivo si se encuentra, -1 si no.
    """
    for indice in range(len(lista)):
        if mostrar_pasos:
            print(f"[Lineal] Comparando {objetivo} con lista[{indice}] = {lista[indice]}")
        if lista[indice] == objetivo:
            return indice
    return -1


def probar_busqueda_lineal():
    """
    Pruebas automáticas usando assert.
    """
    lista = [34, 12, 78, 9, 5, 21, 55]

    # Elementos que sí están
    assert busqueda_lineal(lista, 34) == 0
    assert busqueda_lineal(lista, 5) == 4
    assert busqueda_lineal(lista, 21) == 5

    # Elementos que no están
    assert busqueda_lineal(lista, 100) == -1
    assert busqueda_lineal(lista, 0) == -1
    assert busqueda_lineal(lista, -3) == -1

    print("✅ Todas las pruebas con lista desordenada pasaron correctamente.")


if __name__ == "__main__":
    # Ejecutar pruebas
    probar_busqueda_lineal()

    # Ejemplo visual paso a paso
    print("\n Ejemplo paso a paso con lista desordenada:")
    lista_ejemplo = [13, 4, 25, 7, 2, 19, 30]
    objetivo = 7

    resultado = busqueda_lineal(lista_ejemplo, objetivo, mostrar_pasos=True)
    print(f"\n Resultado final: El número {objetivo} está en la posición {resultado}" if resultado != -1 else f"\n❌ El número {objetivo} no está en la lista.")

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif objetivo < valor_medio:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1

lista = [50, 10, 70, 30, 90, 20]  #  Desordenada
print(busqueda_binaria(lista, 35))  # Resultado impredecible o -1

