# Verificador de Edad en una Película
# Autor: Fabrizzio Lora (FaXx0)
#ingresa tu edad
edad = int(input("Ingresa tu edad: ")) # Solicita la edad del usuario
#Evalu edad
if edad >= 18: # Si la edad es mayor o igual a 18 años
    print("¡Puedes ver películas clasificadas R!")     # Muestra un mensaje de recomendación
elif edad >= 13: # Si la edad es mayor o igual a 13 años y menor a 18 años
    print("Puedes ver películas clasificadas PG-13.") # Muestra un mensaje de recomendación
elif edad >= 0: # Si la edad es mayor o igual a 0 años y menor a 13 años
    print("Te recomendamos películas clasificadas G o PG.") # Muestra un mensaje de recomendación
else: # Si la edad es menor a 0 años o mayor a 120 años
    print("Edad no válida.")     # Muestra un mensaje de error
    # Fin del programa
