# Ejercicio 3: Adivina el número

numero_secreto = 7  # Número secreto fijo
intento = int(input("Adivina el número secreto (entre 1 y 10): "))

while intento != numero_secreto:
    if intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print("Demasiado bajo.")
    intento = int(input("Intenta otra vez: "))

print(f"¡Correcto! El número era {numero_secreto}.")