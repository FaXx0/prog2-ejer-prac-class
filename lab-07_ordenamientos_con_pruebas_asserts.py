def ordenamiento_de_burbuja(lista):
  n = len(lista)
  for i in range(n):
      hubo_intercambio = False
      for j in range(n - 1 - i):
          if lista[j] > lista[j + 1]:
              lista[j], lista[j + 1] = lista[j + 1], lista[j]
              hubo_intercambio = True
      if not hubo_intercambio:
          break
  return lista


def probar_ordenamiento_burbuja():
  # ✅ Caso 1: lista pequeña sin orden
  assert ordenamiento_de_burbuja([4, 2, 7, 1]) == [1, 2, 4, 7]

  # ✅ Caso 2: lista ya ordenada
  assert ordenamiento_de_burbuja([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

  # ✅ Caso 3: lista con números repetidos
  assert ordenamiento_de_burbuja([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

  # ✅ Caso 4: lista con números negativos
  assert ordenamiento_de_burbuja([-2, 5, 0, -10, 3]) == [-10, -2, 0, 3, 5]

  # ⚠️ Caso Borde: lista vacía
  assert ordenamiento_de_burbuja([]) == []

  print("✅ Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
  # Prueba visual
  numeros = [64, 34, 25, 12, 22, 11, 90]
  print("Antes:", numeros)
  ordenamiento_de_burbuja(numeros)
  print("Después:", numeros)

  # Pruebas con assert
  probar_ordenamiento_burbuja()



#-------------------------------#
# ordenamiento_insercion 
#-------------------------------#
def ordenamiento_por_insercion(lista):
 for i in range(1, len(lista)):
     valor_actual = lista[i] 
     posicion_actual = i

#Desplazar elementos mayores hacia la derecha 
#mientras la posicion sea valida y el elemento de la izquierda sea mayor que el actual
     while posicion_actual > 0 and lista[posicion_actual - 1]      > valor_actual:
           lista[posicion_actual] = lista[posicion_actual -              1]#Desplazamiento
           posicion_actual -= 1


    # Insertar el valor actual en su posicion correcta
     lista[posicion_actual] = valor_actual    
 return lista



# Caso 1: Lista desordenada
lista1 = [6, 3, 8, 2, 5]
ordenamiento_por_insercion(lista1)
assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"

# Caso 2: Lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
ordenamiento_por_insercion(lista2)
assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"

# Caso 3: Lista ordenada a la inversa (peor caso)
lista3 = [5, 4, 3, 2, 1]
ordenamiento_por_insercion(lista3)
assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"

# Caso 4: Lista con duplicados
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_por_insercion(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4"

# Caso borde: Lista vacía
assert ordenamiento_por_insercion([]) == [], "Fallo en lista vacía"

# Caso borde: Lista con un solo elemento
assert ordenamiento_por_insercion([42]) == [42], "Fallo en lista con un solo elemento"

print("¡Todas las pruebas del ordenamiento por inserción pasaron! ✅")