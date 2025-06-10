# Tabla de multiplicar del 1 al 10
# Autor: Fabrizzio Aguilera (FaXx0)
# Descripción: Imprime las tablas de multiplicar del 1 al 10.
# Tabla de multiplicar de un número dado por el usuario

numero = int(input("Introduce un número del 1 al 10: "))

# Validamos que el número esté dentro del rango permitido
if 1 <= numero <= 10:
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):  # del 1 al 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Número fuera de rango. Por favor, ingresa un número del 1 al 10.")

