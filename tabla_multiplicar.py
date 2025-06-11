# Tabla de multiplicar del 1 al 10
# Autor: Fabrizzio Lora (FaXx0)
# Descripción: Imprime las tablas de multiplicar del 1 al 10.
# Tabla de multiplicar de un número dado por el usuario 

# Solicitamos al usuario que introduzca un número del 1 al 10 para mostrar su tabla de multiplicar 
numero = int(input("Introduce un número del 1 al 10: ")) # Entrada de datos 
    # Bucle para imprimir la tabla de multiplicar del número ingresado por el usuario
# Validamos que el número esté dentro del rango permitido (1-10)
if 1 <= numero <= 10:    # Validación de datos  # Condicional para validar el rango del número ingresado por el usuario
    print(f"\nTabla de multiplicar del {numero}:\n")    # Mensaje de bienvenida
    for i in range(1, 11):  # del 1 al 10 # Bucle para imprimir la tabla de multiplicar del número ingresado por el usuario # Iteración sobre el rango del 1 al 10 para multiplicar el número ingresado por el usuario
        resultado = numero * i # Cálculo del resultado de la multiplicación # Operación de multiplicación
        print(f"{numero} x {i} = {resultado}")    # Impresión del resultado de la multiplicación # Salida de datos
else:    # Si el número no está dentro del rango permitido, mostramos un mensaje de error 
    print("Número fuera de rango. Por favor, ingresa un número del 1 al 10.") # Mensaje de error 
    # Fin del programa
