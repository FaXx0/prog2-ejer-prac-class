# Verificador de Edad para Película

# 1. Pedir al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# 2. Evaluar la edad
if edad >= 18:
    print("¡Puedes ver películas clasificadas R!")
elif edad >= 13:
    print("Puedes ver películas clasificadas PG-13.")
elif edad >= 0:
    print("Te recomendamos películas clasificadas G o PG.")
else:
    print("Edad no válida.")