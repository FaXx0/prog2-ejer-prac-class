# Verificador de Edad para Película con recomendaciones

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("¡Puedes ver películas clasificadas R!")
    print("🎥 Recomendadas: John Wick, Joker, Deadpool")
elif edad >= 13:
    print("Puedes ver películas clasificadas PG-13.")
    print("🎥 Recomendadas: Spider-Man, The Hunger Games, Jurassic World")
elif edad >= 0:
    print("Te recomendamos películas clasificadas G o PG.")
    print("🎥 Recomendadas: Coco, Toy Story, Moana")
else:
    print("Edad no válida.")
