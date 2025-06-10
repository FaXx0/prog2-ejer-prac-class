"""
Ejercicio: Verificador de Edad para Películas usando Funciones
Autor: Fabrizzio Aguilera (FaXx0)
Descripción: Clasifica el tipo de películas recomendadas según la edad ingresada.
""

def clasificar_pelicula(edad):
    ""
    Clasifica el tipo de películas que una persona puede ver según su edad.

    Parámetros:
    edad (int): Edad del usuario

    Retorna:
    str: Mensaje de clasificación o error
    """
    if edad < 0:
        return "Edad no válida."
    elif edad >= 18:
        return "¡Puedes ver películas clasificadas R!\n🎥 Recomendadas: John Wick, Joker, Deadpool"
    elif edad >= 13:
        return "Puedes ver películas clasificadas PG-13.\n🎥 Recomendadas: Spider-Man, The Hunger Games, Jurassic World"
    else:
        return "Te recomendamos películas clasificadas G o PG.\n🎥 Recomendadas: Coco, Toy Story, Moana"

# Programa principal
if __name__ == "__main__":
    try:
        edad_usuario = int(input("Ingresa tu edad: "))
        resultado = clasificar_pelicula(edad_usuario)
        print(resultado)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Pruebas    (asserts)      
assert clasificar_pelicula(20).startswith("¡Puedes ver películas clasificadas R")
assert clasificar_pelicula(15).startswith("Puedes ver películas clasificadas PG-13")
assert clasificar_pelicula(10).startswith("Te recomendamos películas clasificadas G o PG")
assert clasificar_pelicula(-5) == "Edad no válida."
