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