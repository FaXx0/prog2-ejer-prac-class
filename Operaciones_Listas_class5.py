                            # Autor: Fabrizzio Lora (FaXx0)
                            # Descripción: Este programa cuenta las ocurrencias de un elemento en una lista.  
                            # El usuario puede ingresar el elemento a buscar y el programa le indica cuántas veces aparece en la lista.
def contar_ocurrencias(lista, elemento_buscado):  # Función para contar ocurrencias de un elemento en una lista
    contador = 0 # Inicializa el contador en 0  
    for elemento in lista: # Itera sobre cada elemento de la lista    
        if elemento == elemento_buscado: # Si el elemento es igual al elemento buscado
            contador += 1 # Incrementa el contador en 1
    return contador  # Retorna el contador  # Fin de la función      

mis_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
elemento_buscado = 10 # Elemento a buscar en la lista
resultado = contar_ocurrencias(mis_numeros, elemento_buscado) # Llama a la función contar_ocurrencias() con los parámetros correspondientes
print (f"El elemento {elemento_buscado} aparece {resultado} veces en la lista.") # Imprime el resultado de la función contar_ocurrencias()
#################################################################################
###############################################################
##################
lista_invertida = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]    # Lista original
print ("Lista original:", lista_invertida)
lista_invertida.reverse() # Invierte la lista original
print("Lista invertida:", lista_invertida) # Imprime la lista invertida
#################################################################################
print("************OPERACIONES CON LISTAS*************")
##################################################################################
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero
    return acumulador_suma

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
resultado = sumar_elementos(mi_lista)

print (f"La suma de los elementos de la lista es: {resultado}")

##################################################################################
print("(-Con assert-)")
##################################################################################
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero
    return acumulador_suma
assert sumar_elementos([1, 2, 3, 4, 5]) == 15
print("Prueba 1 pasada = 15")
assert sumar_elementos([10, 20, 30, 40, 50]) == 150
print("Prueba 2 pasada = 150")
assert sumar_elementos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 70
print("Prueba 3 pasada = 70")
assert sumar_elementos([10, -2, 5]) == 13
print("Prueba 4 pasada = 13")
assert sumar_elementos([]) == 0
print("Prueba 5 pasada = 0")
assert sumar_elementos([100]) == 100
print("Prueba 6 pasada = 100")
print (" Todas las pruebas pasaron.")
 ####################################################################################################################################################
print("encontrar el número más grande en una lista")

def encontrar_maximo(ingresa_los_numeros):
    if len(ingresa_los_numeros) == 0:
        return None  # Mejor explicito

    maximo = ingresa_los_numeros[0]
    for numero in ingresa_los_numeros:
        if numero > maximo:
            maximo = numero
    return maximo  # Fuera del bucle

print("\nProbando encontrar_maximo")
assert encontrar_maximo([1, 9, 2, 8, 3, 7]) == 9
print("Prueba 1 pasada = 9")
assert encontrar_maximo([-1, -9, -2, -8]) == -1
print("Prueba 2 pasada = -1")
assert encontrar_maximo([42, 42, 42]) == 42
print("Prueba 3 pasada = 42")