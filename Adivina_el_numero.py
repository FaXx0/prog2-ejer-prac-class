# Ejercicio 3: Adivina el número
                # Autor: Fabrizzio Aguilera (FaXx0)
                # Descripción: Juego en el que el usuario debe adivinar un número secreto.
                # El programa le indica si el número ingresado es demasiado alto o demasiado bajo.
                # El juego continúa hasta que el usuario adivine el número secreto.
                # El número secreto es un número fijo (7) y el usuario tiene que adivinarlo.   

# Variable para almacenar el número secreto (entre 1 y 10)
numero_secreto = 7  # Número secreto fijo 
intento = int(input("Adivina el número secreto (entre 1 y 10): ")) # Solicita al usuario que ingrese un número
    # Bucle hasta que el usuario adivine el número secreto 
    # Compara el número ingresado por el usuario con el número secreto
    # Si el número ingresado es igual al número secreto, el juego termina
    # Si el número ingresado es mayor al número secreto, el programa le indica que el número es demasiado alto
    # Si el número ingresado es menor al número secreto, el programa le indica que el número es demasiado bajo
while intento != numero_secreto: 
    if intento > numero_secreto:   # Comparación de datos
        print("Demasiado alto.")    # Mensaje de error
    else:    # Si el número ingresado es menor al número secreto
        print("Demasiado bajo.")     # Mensaje de error
    intento = int(input("Intenta otra vez: ")) # Solicita al usuario que ingrese otro número
    # Mensaje de éxito al adivinar el número
print(f"¡Correcto! El número era {numero_secreto}.") # Mensaje de éxito
print("Fabrizzio Lora (FaXx0)")
    # Fin del programa